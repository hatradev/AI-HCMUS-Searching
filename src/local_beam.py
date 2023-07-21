from io_data import *
import itertools
import numpy as np
import signal
import time


def generate_product():
    rt = []
    for x in itertools.product([1, 0], repeat=n):
        rt.append("".join(map(str, x)))
    return rt


def generate_simple():
    zero = [0] * n
    return "".join(map(str, zero))


def evaluate(solution: str):
    totalV = 0
    totalW = 0
    no_c = 0
    set = [0]
    for i in range(n):
        if solution[i] == "1":
            totalV += v[i]
            totalW += w[i]
            if c[i] not in set:
                set.append(c[i])
    no_c = len(set) - 1
    if totalW > W:
        totalV = 0
        no_c = 0

    # return totalV #non class
    return (no_c, totalV)  # class


def generate_random(size=n):
    while True:
        state = np.random.randint(2, size=size)
        rt = "".join(map(str, state))
        no_c, tv = evaluate(rt)
        if no_c != 0:
            break
    return rt


def generate_neighborhood(beam):
    neighborhood = []
    for i in range(n):
        neighbor = list(beam)
        neighbor[i] = "1" if neighbor[i] == "0" else "0"
        if evaluate("".join(map(str, neighbor))):
            neighborhood.append("".join(neighbor))
    return neighborhood


def LocalBeam(k: int, max_iter=1000, generate="random"):
    if generate == "random":
        # randomly
        states = []
        while k:
            states.append(generate_random(size=n))
            if len(states) == k:
                break
    elif generate == "product":
        # product
        states = generate_product()  # for _ in range(2**n)
    else:
        states = [generate_simple()]

    initial_solution = max(states, key=evaluate)

    beams = [initial_solution] * k
    best_solution = max(beams, key=evaluate)
    best_value = evaluate(best_solution)
    arr = [0] * n
    for _ in range(max_iter):
        neighborhood = []
        for beam in beams:
            neighborhood += generate_neighborhood(beam)
        beams = sorted(neighborhood, key=evaluate, reverse=True)[:k]
        new_best_solution = max(beams, key=evaluate)
        new_best_value = evaluate(new_best_solution)

        if new_best_value > best_value:
            best_solution = new_best_solution
            best_value = new_best_value

    chosen_items = [i for i in range(n) if best_solution[i] == "1"]
    for item in chosen_items:
        arr[item] = 1

    if best_value[0] < m:
        return 0, [0] * n  # class

    return best_value[1], arr


def signal_handler(signum, frame):
    raise Exception("Timed out!")


# maxTotalV, maxKnapsack = LocalBeam(k = 2) #nonclass
if __name__ == "__main__":
    num_files = int(input("Enter number of input files: "))
    for i in range(num_files):
        W, m, w, v, c, n = read_data_from_file(i + 1)
        st = time.time()
        signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(60 if i + 1 <= 6 else 120)
        tf = True
        try:
            maxTotalV, maxKnapsack = LocalBeam(k=5)
            et = time.time()
            write_output_to_file(i + 1, maxTotalV, maxKnapsack, True)
        except Exception:
            et = time.time()
            tf = False
            write_output_to_file(i + 1, maxTotalV, maxKnapsack, False)
        print(
            f"Execution time of Local beam for input {i + 1} with {tf}: {et - st} seconds"
        )
