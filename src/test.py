import random

a = [1, 2, 3, 4, 5]
b = random.choices(a, weights=[0.1, 0.1, 0.8, 0, 0], k=1)
print(b)


def mutation(child, mutation_rate):
    if random.random() < mutation_rate:
        mutation_idx = random.randint(0, len(child) - 1)
        child[mutation_idx] = 1 - child[mutation_idx]
    return child


print(a)
mutation(a, 0.5)
print(a)
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)

w = [
    6,
    12,
    1,
    7,
    10,
    11,
    3,
    8,
    9,
    4,
    1,
    9,
    6,
    6,
    1,
    4,
    8,
    8,
    9,
    12,
    5,
    1,
    10,
    10,
    4,
    8,
    8,
    6,
    11,
    12,
    5,
    4,
    1,
    5,
    4,
    8,
    10,
    7,
]
v = [
    93,
    54,
    28,
    51,
    50,
    91,
    88,
    59,
    87,
    96,
    17,
    83,
    75,
    83,
    68,
    31,
    45,
    95,
    18,
    68,
    75,
    49,
    60,
    70,
    53,
    23,
    90,
    58,
    31,
    87,
    54,
    78,
    53,
    70,
    71,
    71,
    94,
    56,
]
ind = [
    1,
    0,
    1,
    0,
    0,
    1,
    1,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
]
totalW = sum(ind[i] * w[i] for i in range(len(w)))
totalV = sum(ind[i] * v[i] for i in range(len(w)))
print(totalW, totalV)
