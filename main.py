import numpy as np
import random
import string
import matplotlib.pyplot as plt

POP_SIZE = 200
TARGET = "Kaliyah"
TARGET_LENGTH = len(TARGET)

def DNA():
    return [random.choice(string.printable) for i in range(TARGET_LENGTH)]

def initial_population():
    return [DNA() for i in range(POP_SIZE)]
        
def calc_fitness(element):
    fitness = 0
    for i, v in enumerate(element):
        if v == TARGET[i]:
            fitness += 1
    return fitness

def calc_pop_fitness_score(pop):
    return [calc_fitness(i) for i in pop]

def has_target_element(pop):
    for i in pop:
        if ''.join(i) == TARGET:
            return i

def cross_over(parent_1, parent_2):
    mid_point = len(parent_1) // 2
    return parent_1[:mid_point] + parent_2[mid_point:]

def cross_over_2(parent_1, parent_2):
    mid_point = random.randint(0, len(parent_1)-1)
    return parent_1[:mid_point] + parent_2[mid_point:]

def generate_pop(pop):
    pop_fitness_score = calc_pop_fitness_score(pop)
    average_fitness_score = sum(pop_fitness_score) / POP_SIZE
    distribution = np.array(pop_fitness_score) / sum(pop_fitness_score)

    new_pop = []

    for i in range(POP_SIZE):
        parents = random.choices(pop, distribution, k=2)
        #Cross Over
        child = cross_over_2(parents[0], parents[1])
        #Mutate
        for i,v in enumerate(child):
            if random.random() <= 0.01:
                child[i] = random.choice(string.printable)

        new_pop.append(child)

    return new_pop, average_fitness_score, pop[pop_fitness_score.index(max(pop_fitness_score))]


pop = initial_population()
gen = 0

x = []

while True:
    pop, average_fitness_score, best = generate_pop(pop)
    x.append((average_fitness_score / TARGET_LENGTH) * 100)
    found = has_target_element(pop)
    gen += 1
    if found:
        print(found, gen)
        break

plt.plot(range(gen), x)
plt.show()