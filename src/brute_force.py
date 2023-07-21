from io_data import *
import signal
import time


knapsack, maxKnapsack, totalW, totalV, maxTotalV, c_set = 0, 0, 0, 0, 0, 0


def brute_force(i, getItem=False):
    global totalV, totalW, maxTotalV, maxKnapsack, c_set
    if i == n:
        return
    if getItem:
        totalW += w[i]
        totalV += v[i]
        knapsack[i] = 1
        existed = True
        if c[i] not in c_set:
            c_set.append(c[i])
            existed = False
        if totalW <= W and totalV > maxTotalV and len(c_set) - 1 == m:
            maxTotalV = totalV
            maxKnapsack = knapsack.copy()
        brute_force(i + 1, True)
        brute_force(i + 1)
        totalW -= w[i]
        totalV -= v[i]
        knapsack[i] = 0
        if not existed:
            c_set.pop()
    else:
        brute_force(i + 1, True)
        brute_force(i + 1)


def signal_handler(signum, frame):
    raise Exception("Timed out!")


if __name__ == "__main__":
    num_files = int(input("Enter number of input files: "))
    for i in range(num_files):
        W, m, w, v, c, n = read_data_from_file(i + 1)
        knapsack = [0] * n
        maxKnapsack = [0] * n
        totalW, totalV, maxTotalV = 0, 0, 0
        c_set = [0]
        st = time.time()
        signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(60 if i + 1 <= 6 else 120)
        tf = True
        try:
            brute_force(-1)
            et = time.time()
            write_output_to_file(i + 1, maxTotalV, maxKnapsack, True)
        except Exception:
            et = time.time()
            tf = False
            write_output_to_file(i + 1, maxTotalV, maxKnapsack, False)
        print(
            f"Execution time of Brute-force for input {i + 1} with {tf}: {et - st} seconds"
        )
