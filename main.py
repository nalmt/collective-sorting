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

class Agent:

    t_size = 10
    t = []
    def __init__(self, l, c):
        self.l = l
        self.c = c


def  main():
    fill_with(na, 'A')
    fill_with(nb, 'B')
    fill_agent(number_of_agents)
    print(matrix)
    print(agents_list)


#def scheduler():


if __name__ == "__main__":
    main()
