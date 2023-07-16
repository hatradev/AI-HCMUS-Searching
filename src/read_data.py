# Read data from the file INPUT_x.txt
file = open("INPUT_1.txt")
W = int(file.readline())
m = int(file.readline())
w = file.readline().split(', ')
w = [float(wi) for wi in w]
v = file.readline().split(', ')
v = [int(vi) for vi in v]
c = file.readline().split(', ')
c = [int(ci) for ci in c]

n = len(w)
totalW, totalV, maxTotalV = 0, 0, 0
knapsack = [0] * n
maxKnapsack = [0] * n
c_set = [0]