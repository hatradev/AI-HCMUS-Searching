from read_data import *
import itertools

def LocalBeam(k: int, max_inter=100):   
    def evaluate(solution):
        total_value = 0
        total_weight = 0
        no_c = 0
        set = [0]
        for i in range(n):
            if solution[i] == '1':
                total_value += v[i]
                total_weight += w[i]
                if c[i] not in set:
                    set.append(c[i])
        no_c = len(set) - 1
        if total_weight > W:
            total_value = 0
            no_c = 0
            
        return (no_c, total_value)
    
    def generate_neighborhood(beam):
        neighborhood = []
        for i in range(n):
            neighbor = list(beam)
            neighbor[i] = '1' if neighbor[i] == '0' else '0'
            neighborhood.append(''.join(neighbor))
        return neighborhood
    
    def solve(k, max_iterations=100):
        initial_solution = max([''.join(map(str, x)) for x in itertools.product([0, 1], repeat=n)], key=evaluate)
        beams = [initial_solution] * k
        best_solution = max(beams, key=evaluate)
        best_value = evaluate(best_solution)
        arr = [0] * n

        for i in range(max_iterations):
            neighborhood = []
            for beam in beams:
                neighborhood += generate_neighborhood(beam)
            beams = sorted(neighborhood, key=evaluate, reverse=True)[:k]
            new_best_solution = max(beams, key=evaluate)
            new_best_value = evaluate(new_best_solution)
            if new_best_value > best_value:
                best_solution = new_best_solution
                best_value = new_best_value

        chosen_items = [i for i in range(n) if best_solution[i] == '1']
        for item in chosen_items:
            arr[item] = 1
        return best_value[1], arr, best_value[0]
    
    return solve(k, max_inter)

maxTotalV, maxKnapsack, numclass = LocalBeam(k = 2)
print(maxTotalV)
print(maxKnapsack)
print(numclass == m)
