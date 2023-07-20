# Read data from the file INPUT_x.txt
file = open("../datasets/INPUT_1.txt")
W = int(file.readline())  # the Knapsack's storage capacity
m = int(file.readline())  # number of class
w = file.readline().split(", ")
w = [float(wi) for wi in w]  # list of weight of items
v = file.readline().split(", ")
v = [int(vi) for vi in v]  # list of values of items
c = file.readline().split(", ")
c = [int(ci) for ci in c]  # list of class

n = len(w)  # number of items
totalW, totalV, maxTotalV = 0, 0, 0
knapsack = [0] * n
maxKnapsack = [0] * n
c_set = [0]

# print(n, len(v))
