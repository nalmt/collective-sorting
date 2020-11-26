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


def p_prise(k_plus, f):
    return (k_plus / (k_plus + f)) ^ 2

def p_depot(k_moins, f):
    return (f / (k_moins + f)) ^ 2

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

    def f(self):
        if self.objet_porte != '0':

    #    number_of_A = self.get_number_of_around('A')
    #    number_of_B = self.get_number_of_around('B')

    def action(self):
        self.move_randomly()


    def move_randomly(self):
        #TODO EMNA choose randomly between
        # possible moves
        # (can't choose an impossible move)
        # (move_north, move_south
        # move_east, move_west)

    def move_north(self, l, c):
        self.move(l - 1, c)

    def move_south(self):
        self.move(l + 1, c)

    def move_east(self):
        self.move(l, c + 1)

    def move_west(self):
        self.move(l, c - 1)

    def move(self, l, c):
        #TODO EMNA

    def update_t(self, object):
        self.move()

def  main():
    fill_with(na, 'A')
    fill_with(nb, 'B')
    fill_agent(number_of_agents)
    print(matrix)
    print(agents_list)


#def scheduler():


if __name__ == "__main__":
    main()
