from termcolor import colored
#import pygame as pg
import numpy as np
import sys
from enum import Enum
import random

NUMBER_OF_ITERATIONS = 10
NUMBER_OF_AGENTS = 20
K_PLUS = 0.1
K_MOINS = 0.3
NA = 200
NB = 200
T_SIZE = 10
ERREUR = 0
N = 50
I = 1

matrix = np.full((N, N), '0')

agents_list = []

def fill_with(number_of_objects, object_type):
    for _ in range(number_of_objects):
        l = random.randint(0, N - 1)
        c = random.randint(0, N - 1)

        while matrix[l][c] != '0':
            l = random.randint(0, N - 1)
            c = random.randint(0, N - 1)
        
        matrix[l][c] = object_type

def fill_agent(number_of_objects):
    for _ in range(number_of_objects):
        l = random.randint(0, N - 1)
        c = random.randint(0, N - 1)

        while matrix[l][c] != '0':
            l = random.randint(0, N - 1)
            c = random.randint(0, N - 1)

        agents_list.append(Agent(l, c))
        matrix[l][c] = 'X'

def get_object(l, c):
    if l >= 0 and l < len(matrix) and c >= 0 and c < len(matrix[0]):
        return matrix[l][c]
    else:
        return 'W' # Wall

class Agent:

    t = []
    objet_porte = '0'

    def __init__(self, l, c):
        self.l = l
        self.c = c

    # return number of boxes avalaible around (N, S, E, W)
    # without considering what they have inside
    def number_of_boxes(self):
        num = 0
        if self.get_north() != 'W':
            num += 1
        if self.get_south() != 'W':
            num += 1
        if self.get_east() != 'W':
            num += 1
        if self.get_west() != 'W':
            num += 1
        return num

    # return number of boxes avalaible around (N, S, E, W)
    # considering what they have inside
    # (an agent can not move if there is already
    # an agent 'X' in the boxe
    def get_number_of_boxes_attainable(self):
        number_of_boxes_attainable = 0
        if self.get_north() != 'W' and self.get_north() != 'X' and self.get_north() != 'Y' and self.get_north() != 'Z':
            number_of_boxes_attainable += 1
        if self.get_south() != 'W' and self.get_south() != 'X' and self.get_south() != 'Y' and self.get_south() != 'Z':
            number_of_boxes_attainable += 1
        if self.get_east() != 'W' and self.get_east() != 'X' and self.get_east() != 'Y' and self.get_east() != 'Z':
            number_of_boxes_attainable += 1
        if self.get_west() != 'W' and self.get_west() != 'X' and self.get_west() != 'Y' and self.get_west() != 'Z':
            number_of_boxes_attainable += 1
        return number_of_boxes_attainable

    # return number of the object 'letter' ('A' or 'B')
    # in the boxes around (N, S, E, W)
    def get_number_of_around(self, letter):
        number_around = 0
        if letter in self.get_north():
            number_around += 1
        if letter in self.get_south():
            number_around += 1
        if letter in self.get_east():
            number_around += 1
        if letter in self.get_west():
            number_around += 1
        return number_around

    def action(self):
        self.move_randomly()
        encountered_object = self.get_encountered_object()

        if self.objet_porte == '0':
            if encountered_object != '0':
                proba_prise = self.p_prise(self.f(encountered_object))
                if self.decision(proba_prise) == True:
                    self.take_object(encountered_object)
                else:
                    if encountered_object == 'A':
                        matrix[self.l][self.c] = 'Y'
                    else:
                        matrix[self.l][self.c] = 'Z'
            else:
                matrix[self.l][self.c] = 'X'
        else:
            if encountered_object == '0':
                proba_depot = self.p_depot(self.f(self.objet_porte))
                if self.decision(proba_depot) == True:
                    self.leave_object(self.objet_porte)
                else:
                    matrix[self.l][self.c] = 'X'
            else:
                if encountered_object == 'A':
                    matrix[self.l][self.c] = 'Y'
                else:
                    matrix[self.l][self.c] = 'Z'


    def take_object(self, encountered_object):
        matrix[self.l][self.c] = 'X'
        self.objet_porte = encountered_object

    def leave_object(self, objet_porte):
        if objet_porte == 'A':
            matrix[self.l][self.c] = 'Y'
        else:
            matrix[self.l][self.c] = 'Z'
        self.objet_porte = '0'

    def decision(self, probability):
        return random.random() < probability

    def f(self, encountered_object):
        if encountered_object == 'A':
            return self.f_a()
        else:
            return self.f_b()

    def f_a(self):
        nb_a = self.t.count('A')
        nb_b = self.t.count('B')
        print("nb_a", nb_a)
        print("nb_b", nb_b)
        print("t", self.t)
        print("len(t)", len(self.t))
        return (nb_a + nb_b * ERREUR)/len(self.t)
    
    def f_b(self):
        nb_a = self.t.count('A')
        nb_b = self.t.count('B')
        print("nb_a", nb_a)
        print("nb_b", nb_b)
        print("t", self.t)
        print("len(t)", len(self.t))
        return (nb_b + nb_a * ERREUR)/len(self.t)

    def get_encountered_object(self):
        return self.t[-1]

    def move_randomly(self):
        list_of_possible_moves = self.get_possible_moves()

        if len(list_of_possible_moves) != 0:
            r = random.randint(0, len(list_of_possible_moves) - 1)
            list_of_possible_moves[r]()

    def get_possible_moves(self):
        list_of_possible_moves = []
        if self.get_north() != 'W' and self.get_north() != 'X' and self.get_north() != 'Y' and self.get_north() != 'Z':
            list_of_possible_moves.append(self.move_north)
        if self.get_south() != 'W' and self.get_south() != 'X' and self.get_south() != 'Y' and self.get_south() != 'Z':
            list_of_possible_moves.append(self.move_south)
        if self.get_east() != 'W' and self.get_east() != 'X' and self.get_east() != 'Y' and self.get_east() != 'Z':
            list_of_possible_moves.append(self.move_east)
        if self.get_west() != 'W' and self.get_west() != 'X' and self.get_west() != 'Y' and self.get_west() != 'Z':
            list_of_possible_moves.append(self.move_west)
        return list_of_possible_moves

    def get_north(self):
        return get_object(self.l - 1, self.c)

    def get_south(self):
        return get_object(self.l + 1, self.c)

    def get_east(self):
        return get_object(self.l, self.c + 1)

    def get_west(self):
        return get_object(self.l, self.c - 1)

    def move_north(self):
        self.move(self.l - 1, self.c)

    def move_south(self):
        self.move(self.l + 1, self.c)

    def move_east(self):
        self.move(self.l, self.c + 1)

    def move_west(self):
        self.move(self.l, self.c - 1)

    def move(self, l, c):
        encountred_object = get_object(l, c)
        self.t.append(encountred_object)
        if len(self.t) > T_SIZE:
            self.t.pop(0)

        if matrix[self.l][self.c] == 'X':
            matrix[self.l][self.c] = '0'
        elif matrix[self.l][self.c] == 'Y':
            matrix[self.l][self.c] = 'A'
        else:
            matrix[self.l][self.c] = 'B'

        self.l = l
        self.c = c
        matrix[self.l][self.c] = 'X'

    def p_prise(self, f):
        return pow((K_PLUS / (K_PLUS + f)), 2)

    def p_depot(self, f):
        return pow((f / (K_MOINS + f)), 2)


def convert_matrix(m):
    mat = np.zeros((N, N), int)
    for l in range(0,N):
        for c in range(0,N):
            if m[l][c] == '0':
                mat[l][c] = 0
            elif m[l][c] == 'A':
                mat[l][c] = 1
            elif m[l][c] == 'B':
                mat[l][c] = 2
            elif m[l][c] == 'X':
                mat[l][c] = 3

    return mat

def print_matrix():
    for l in matrix:
        print('|', end='')
        for c in l:
            if c == '0':
                print(' ', end='')
            elif c == 'A':
                print(colored(c, 'red'), end='')
            elif c == 'B':
                print(colored(c, 'green'), end='')
            elif c == 'X':
                print(c, end='')
        print('|')

def scheduler():
    #pg.init()
    #pg.display.set_caption('Question1')
    #screen = pg.display.set_mode((700, 700))
    #clock = pg.time.Clock()

    colors = np.array([[0, 0, 0], [255, 0, 0], [0, 0, 255], [255, 255, 255]])

    #running = True
    #while running:
    #    for event in pg.event.get():
    #        if event.type == pg.QUIT:
    #            running = False
    for _ in range(0, NUMBER_OF_ITERATIONS):

        for agent in agents_list:
            for _ in range(0, I):
                agent.action()
          #  print_matrix()

           # m = convert_matrix(matrix)
           # surface = pg.surfarray.make_surface(colors[m])
           # surface = pg.transform.scale(surface, (500, 500))  # Scaled a bit.

           # screen.fill((30, 30, 30))
           # screen.blit(surface, (100, 100))
           # pg.display.flip()
           # clock.tick(60)


def main():
    fill_with(NA, 'A')
    fill_with(NB, 'B')
    fill_agent(NUMBER_OF_AGENTS)

    print_matrix()
    print("-------------------------")
    scheduler()
    print_matrix()


if __name__ == "__main__":
    main()
