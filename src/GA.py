import numpy as np


# Read the input data from the file
def read_input_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        capacity = float(lines[0].strip())
        num_classes = int(lines[1].strip())
        weights = np.array([float(x) for x in lines[2].strip().split(",")])
        values = np.array([int(x) for x in lines[3].strip().split(",")])
        labels = np.array([int(x) for x in lines[4].strip().split(",")])
    return capacity, num_classes, weights, values, labels


# Define the fitness function
def fitness(solution, capacity, weights, values):
    total_weight = np.dot(solution, weights)
    total_value = np.dot(solution, values)
    if total_weight > capacity:
        return 0
    return total_value


# Perform selection using tournament selection
def selection(population, capacity, weights, values):
    tournament_size = 5
    selected_population = []
    for _ in range(len(population)):
        tournament = np.random.choice(population, tournament_size, replace=False)
        tournament_fitness = np.array(
            [fitness(solution, capacity, weights, values) for solution in tournament]
        )
        winner = tournament[np.argmax(tournament_fitness)]
        selected_population.append(winner)
    return selected_population


# Perform crossover by exchanging genetic material between parents
def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, len(parent1) - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2


# Perform mutation by randomly flipping bits in the solution
def mutation(solution, mutation_rate):
    mutated_solution = solution.copy()
    for i in range(len(mutated_solution)):
        if np.random.rand() < mutation_rate:
            mutated_solution[i] = 1 - mutated_solution[i]
    return mutated_solution


# Solve the knapsack problem using genetic algorithm
def knapsack_genetic_algorithm(
    capacity,
    num_classes,
    weights,
    values,
    labels,
    population_size,
    generations,
    mutation_rate,
):
    num_items = len(weights)
    population = np.random.randint(2, size=(population_size, num_items))
    best_solution = None
    best_fitness = 0

    for _ in range(generations):
        population = selection(population, capacity, weights, values)
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = np.random.choice(population, 2, replace=False)
            child1, child2 = crossover(parent1, parent2)
            mutated_child1 = mutation(child1, mutation_rate)
            mutated_child2 = mutation(child2, mutation_rate)
            new_population.append(mutated_child1)
            new_population.append(mutated_child2)

        population = np.array(new_population)
        population_fitness = np.array(
            [fitness(solution, capacity, weights, values) for solution in population]
        )

        best_index = np.argmax(population_fitness)
        if population_fitness[best_index] > best_fitness:
            best_solution = population[best_index]
            best_fitness = population_fitness[best_index]

    selected_items = [i for i, val in enumerate(best_solution) if val == 1]
    total_value = best_fitness
    return selected_items, total_value


# Main function
def main():
    file_name = "../datasets/INPUT_1.txt"
    capacity, num_classes, weights, values, labels = read_input_file(file_name)

    population_size = 100
    generations = 100
    mutation_rate = 0.01

    selected_items, total_value = knapsack_genetic_algorithm(
        capacity,
        num_classes,
        weights,
        values,
        labels,
        population_size,
        generations,
        mutation_rate,
    )

    print("Selected items:", selected_items)
    print("Total value:", total_value)


if __name__ == "__main__":
    main()
