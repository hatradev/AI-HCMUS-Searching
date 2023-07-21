from io_data import *
import random
import numpy as np
import signal
import time


def check_invalid_class():
    set_class = np.unique(c)
    if len(set_class) != m:
        return False
    return True


def get_min_individual_of_class(k):
    k_idx = []
    k_weights = []
    for i in range(n):
        if c[i] == k:
            k_idx.append(i)
            k_weights.append(w[i])
    return k_idx[np.argmin(k_weights)]


# Create an individual
def create_individual(min_individuals):
    W_temp = W
    individual = [0] * n
    # Ensure individual has enough m classes
    for k in range(m):
        idx = min_individuals[k]
        individual[idx] = 1
        W_temp -= w[idx]
        if W_temp < 0:
            return []

    for i in range(n):
        idx = random.randint(0, n - 1)
        if individual[idx] == 0:
            W_temp -= w[idx]
        individual[idx] = 1
        if W_temp <= 0:
            if W_temp < 0:
                individual[idx] = 0
            break

    return individual


# Calculate weight of an individual
def weight_of(individual):
    return np.dot(individual, w)


# Calculate value of an individual
def value_of(individual):
    return np.dot(individual, v)


# Calculate number of class of an individual
def class_of(individual):
    c_set = np.array(individual) * np.array(c)
    c_set = np.unique(c_set)
    if c_set[0] == 0:
        c_set = c_set[1:]
    return len(c_set)


# Init population
def init_population(num_pop):
    population = []
    min_individuals = [get_min_individual_of_class(k + 1) for k in range(m)]
    for i in range(num_pop):
        individual = create_individual(min_individuals)
        if individual:
            population.append(individual)
        else:
            return []
    return population


# Calculate fitness
def fitness_of(individual):
    return (
        value_of(individual)
        if weight_of(individual) <= W and class_of(individual) == m
        else 0
    )


# Calculate fitness scores for population
def fitness_scores_of(population):
    return np.apply_along_axis(fitness_of, 1, population).tolist()


# Selection from selected individuals
def selection(population, fitness_ratio):
    parents = np.array(population)[
        np.random.choice(len(population), size=2, replace=False, p=fitness_ratio)
    ]
    return parents.tolist()


# Crossover
def crossover(parent1, parent2):
    split_idx = random.randint(1, len(parent1) - 1)
    child1 = parent1[:split_idx] + parent2[split_idx:]
    child2 = parent2[:split_idx] + parent1[split_idx:]
    return child1, child2


# Mutation
def mutation(child, mutation_rate):
    if random.random() < mutation_rate:
        mutation_idx = random.randint(0, len(child) - 1)
        child[mutation_idx] = 1 - child[mutation_idx]
    return child


# Get best individual
def get_best_individual(population):
    fitness_scores = fitness_scores_of(population)
    best_idx = np.argmax(fitness_scores)
    best_value = value_of(population[best_idx])
    return best_value, population[best_idx]


# Genetic algorithm
def genetic_algo(x):
    global W, m, w, v, c, n
    W, m, w, v, c, n = read_data_from_file(x)
    num_pop = 100
    generations = 1000
    mutation_rate = 0.4
    count = 0
    best_value = 0
    best_individual = []
    result_value = 0
    result_individual = []
    pre_best_value = 0
    res_count = 0
    res_itr = 200 if n <= 500 else 100
    if check_invalid_class():
        population = init_population(num_pop)
        if not population:
            write_output_to_file(x, 0, [0] * n, True)
            return
    else:
        write_output_to_file(x, 0, [0] * n, True)
        return

    k = num_pop // 2
    for i in range(generations):
        new_population = []
        population.sort(key=fitness_of, reverse=True)
        new_population.extend(population[:k])
        fitness_scores = fitness_scores_of(population)
        fitness_ratio = fitness_scores / np.sum(fitness_scores)
        for _ in range(num_pop // 2):
            # Choose parents for crossovering to make two new children
            parents = selection(population, fitness_ratio)
            child1, child2 = crossover(parents[0], parents[1])
            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population
        best_value, best_individual = get_best_individual(population)
        if best_value > result_value:
            result_value = best_value
            result_individual = best_individual
            mutation_rate = 0.4
            count = 0
            res_count = 0
        # print(i, result_value, result_individual)
        if count >= 30:
            mutation_rate *= 2
            count = 0
        if best_value == pre_best_value:
            count += 1
        elif best_value > pre_best_value:
            mutation_rate = 0.4
        pre_best_value = best_value
        if res_count >= res_itr:
            break
        if best_value == result_value:
            res_count += 1
    write_output_to_file(x, result_value, result_individual, True)


def signal_handler(signum, frame):
    raise Exception("Timed out!")


if __name__ == "__main__":
    num_files = int(input("Enter number of input files: "))
    for i in range(num_files):
        st = time.time()
        signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(60 if i + 1 <= 6 else 120)
        tf = True
        try:
            genetic_algo(i + 1)
            et = time.time()
        except Exception:
            et = time.time()
            tf = False
            write_output_to_file(i + 1, 0, [], False)
        print(
            f"Execution time of Genetic algorithm for input {i + 1} with {tf}: {et - st} seconds"
        )
