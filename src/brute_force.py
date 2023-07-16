from read_data import *


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
print(maxTotalV, maxKnapsack)
