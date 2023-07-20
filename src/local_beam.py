from io_data import *
import itertools
import numpy as np

def generate_random(size = n):
    state = np.random.randint(2, size=size)
    return ''.join(map(str, state))

def generate_product():
    rt = []
    for x in itertools.product([1, 0], repeat=n):
        rt.append(''.join(map(str, x)))
    return rt

def generate_simple():
    zero = [0]*n
    return ''.join(map(str, zero))

def evaluate(solution: str):
    totalV = 0
    totalW = 0
    no_c = 0
    set = [0]
    for i in range(n):
        if solution[i] == '1':
            totalV += v[i]
            totalW += w[i]
            if c[i] not in set:
               set.append(c[i])
    no_c = len(set) - 1
    if totalW > W:
        totalV = 0
        no_c = 0
        
    # return totalV #non class
    return (no_c, totalV) #class

def generate_neighborhood(beam):
    neighborhood = []
    for i in range(n):
        neighbor = list(beam)
        neighbor[i] = '1' if neighbor[i] == '0' else '0'
        neighborhood.append(''.join(neighbor))
    return neighborhood
    
def LocalBeam(k: int, max_iter=1000, generate="simple"): 
    if (generate=="random"):
        #randomly
        states = [generate_random(size = n) for _ in range(k)]
    elif generate == "product":
        #product
        states = generate_product() # for _ in range(2**n)
    else:
        states = [generate_simple()]
    
    initial_solution = max(states, key=evaluate)
    
    beams = [initial_solution] * k
    best_solution = max(beams, key=evaluate)
    best_value = evaluate(best_solution)
    arr = [0] * n

    loopy = max_iter
    
    while loopy:
        neighborhood = []
        for beam in beams:
            neighborhood += generate_neighborhood(beam)
        beams = sorted(neighborhood, key=evaluate, reverse=True)[:k]
        new_best_solution = max(beams, key=evaluate)
        new_best_value = evaluate(new_best_solution)
        
        if new_best_value > best_value:
            best_solution = new_best_solution
            best_value = new_best_value
            loopy = max_iter
        else:
            loopy -= 1

    chosen_items = [i for i in range(n) if best_solution[i] == '1']
    for item in chosen_items:
        arr[item] = 1
    
    if (best_value[0] == m):
        # return best_value, arr #non_class
        return best_value[1], arr #class
    
    return 0, [0]*n
    

# maxTotalV, maxKnapsack = LocalBeam(k = 2) #nonclass
file = input("Input the number of input file: ")
W, m, w, v, c, n = read_data_from_file(file)
maxTotalV, maxKnapsack = LocalBeam(k = 2)

print(maxTotalV)
print(maxKnapsack)
write_output_to_file(maxTotalV, maxKnapsack)
