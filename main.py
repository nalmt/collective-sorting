# TP2 SMA 
# 21/10/20
import numpy as np
from enum import Enum
import random

i = 1
number_of_agents = 20
k_plus = 0.1
k_moins = 0.3
na = 200
nb = 200

matrix = np.full((50, 50), '0')

agents_list = []

def fill_with(number_of_objects, object_type):
    for machin in range(number_of_objects):
        l = random.randint(0, 49)
        c = random.randint(0, 49)

        while matrix[l][c] != '0':
            l = random.randint(0, 49)
            c = random.randint(0, 49)
        
        matrix[l][c] = object_type

def fill_agent(number_of_objects):
    for machin in range(number_of_objects):
        l = random.randint(0, 49)
        c = random.randint(0, 49)

        while matrix[l][c] != '0':
            l = random.randint(0, 49)
            c = random.randint(0, 49)

        agents_list.append(Agent(l, c))
        matrix[l][c] = 'X'

def get_position(l, c):
    if l >= 0 and l < len(matrix) and c >= 0 and c < len(matrix[0]):
        return matrix[l][c]
    else
        return 'W' # Wall

class Agent:

    t_size = 10
    t = []
    objet_porte = '0'

    def __init__(self, l, c):
        self.l = l
        self.c = c

    def get_north(self):
        return get_position(l - 1, c)

    def get_south(self):
        return get_position(l + 1, c)

    def get_east(self):
        return get_position(l, c + 1)

    def get_west(self):
        return get_position(l, c - 1)

    def get_number_of_boxes_attainable(self):
        number_of_boxes_attainable = 0
        if self.get_north() != 'W' or not self.get_north().contains('X'):
            number_of_boxes_attainable += 1
        if self.get_south() != 'W' or not self.get_north().contains('X'):
            number_of_boxes_attainable += 1
        if self.get_east() != 'W' or not self.get_north().contains('X'):
            number_of_boxes_attainable += 1
        if self.get_west() != 'W' or not self.get_north().contains('X'):
            number_of_boxes_attainable += 1
        return number_of_boxes_attainable

    def get_number_of_around(letter, self):
        number_around = 0
        if self.get_north() == letter:
            number_around += 1
        if self.get_south() == letter:
            number_around += 1
        if self.get_east() == letter:
            number_around += 1
        if self.get_west() == letter:
            number_around += 1
        return number_around

    def action(self):
        self.move_randomly()
        encountered_object = self.get_encountered_object()

        if self.objet_porte == '0':
            if encountered_object != '0':
                p_prise = self.p_prise(self.f(encountered_object))
                if self.decision(p_prise) == True:
                    self.take_object(encountered_object)
                else:
                    matrix[self.l][self.c] = encountered_object
            else:
                matrix[self.l][self.c] = 'X'
        else:
            if encountered_object == '0':
                p_depot = self.p_depot(self.f(self.objet_porte))
                if self.decision(p_depot) == True:
                    self.leave_object(self.objet_porte)
                else:
                    matrix[self.l][self.c] = 'X'
            else:
                matrix[self.l][self.c] = encountered_object

    def take_object(self, encountered_object):
        self.objet_porte = encountered_object
        matrix[self.l][self.c] = 'X'

    def leave_object(self, objet_porte):
        matrix[self.l][self.c] = 'X'+objet_porte

    def decision(probability):
        return random.random() < probability

    def f(self, encountered_object):
        return self.get_number_of_around(encountered_object) / self.get_number_of_boxes_attainable()

    def get_encountered_object(self):
        return self.t[-1]

    def move_randomly(self):
        #TODO EMNA choose randomly between
        # possible moves
        # (can't choose an impossible move)
        # (move_north, move_south
        # move_east, move_west)

    def move_north(self):
        self.move(self.l - 1, self.c)

    def move_south(self):
        self.move(self.l + 1, self.c)

    def move_east(self):
        self.move(self.l, self.c + 1)

    def move_west(self):
        self.move(self.l, self.c - 1)

    def move(self, l, c):
        encountred_object = self.get_position(l, c)
        self.t.append(encountred_object)
        if len(self.t) > 10:
            self.t.pop(0)
        matrix[self.l][self.c] = self.t[-2]
        self.l = l
        self.c = c
        matrix[self.l][self.c] = 'X'

    def update_t(self, object):
        self.move()

    def p_prise(f):
    return (k_plus / (k_plus + f)) ^ 2

    def p_depot(f):
    return (f / (k_moins + f)) ^ 2


def scheduler():
    for _ in range(0, 10):
        for agent in agents_list:
            agent.action()
            print(matrix)

def  main():
    fill_with(na, 'A')
    fill_with(nb, 'B')
    fill_agent(number_of_agents)
    scheduler()

if __name__ == "__main__":
    main()
