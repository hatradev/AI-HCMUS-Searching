from io_data import *

W, m, w, v, c, n, x = read_data_from_file()

knapsack = [0] * n
maxKnapsack = [0] * n
totalW, totalV, maxTotalV = 0, 0, 0
c_set = [0]


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


brute_force(-1)
write_output_to_file(totalV, maxKnapsack)
