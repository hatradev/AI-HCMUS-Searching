from read_data import *
from statistics import mean
import random

bestTotalV = 0


def init_population():
    population = []
    for i in range(100):
        individual = [random.randint(0, 1) for i in range(n)]
        population.append(individual)
    return population


def evaluate_fitness(population):
    totalW = [sum(individual[i] * w[i] for i in range(n)) for individual in population]
    totalV = [sum(individual[i] * v[i] for i in range(n)) for individual in population]
    fitness_score = []
    sumOfTotalV = sum(totalV)
    for i in range(len(population)):
        if totalW[i] <= W:
            fitness_score.append(totalV[i] * 1.0 / sumOfTotalV)
        else:
            # The overweight individual has fitness_score = 0
            fitness_score.append(0)
    return fitness_score


def selection(population, pop_len, fitness_score):
    idx = 0
    k = 10
    best_fitness = 0
    for _ in range(k):
        i = random.randint(0, pop_len - 1)
        if fitness_score[i] > best_fitness:
            best_fitness = fitness_score[i]
            idx = i
        else:
            population[i] = population[random.randint(0, pop_len - 1)]
    return idx


def crossover(parent1, parent2):
    idx = random.randint(0, len(parent1) - 1)
    child1 = parent1[:idx] + parent2[idx:]
    child2 = parent2[:idx] + parent1[idx:]
    return child1, child2


def mutation(child):
    i = random.randint(0, n - 1)
    child[i] = 1 - child[i]
    return child


def display_population(population):
    for individual in population:
        print(individual)


def get_best_fitness(fitness_score):
    return fitness_score.index(max(fitness_score))


def display_individual(population, pop_len, fitness_score, idx):
    global flag, bestTotalV
    totalV = sum(population[idx][i] * v[i] for i in range(pop_len))
    totalW = sum(population[idx][i] * w[i] for i in range(pop_len))
    if totalV > bestTotalV:
        bestTotalV = totalV
    print(
        fitness_score[idx],
        totalV,
        totalW,
        population[idx],
    )


def genetic_algo():
    population = init_population()
    generations = 3000
    mutation_rate = 0.2
    count = 0
    pop_len = len(population)
    pre_best_fitness_score = 0
    for i in range(generations):
        fitness_score = evaluate_fitness(population)
        best_fitness_score = get_best_fitness(fitness_score)
        display_individual(
            population, pop_len, fitness_score, get_best_fitness(fitness_score)
        )
        # Choose two parent for crossovering to make two new children
        idx1 = selection(population, pop_len, fitness_score)
        idx2 = selection(population, pop_len, fitness_score)
        child1, child2 = crossover(population[idx1], population[idx2])
        if random.random() < mutation_rate:
            child1 = mutation(child1)
        if random.random() < mutation_rate:
            child2 = mutation(child2)
        # Replace two parent by two children
        population[random.randint(0, pop_len - 1)] = child1
        population[random.randint(0, pop_len - 1)] = child2
        # If the population doesn't have improvement after an amount of time, then increase mutation rate.
        if count > generations / 20:
            mutation_rate *= 4
            count = 0
        if best_fitness_score == pre_best_fitness_score:
            count += 1
        pre_best_fitness_score = best_fitness_score

    print("Best total V: ", bestTotalV)


genetic_algo()
