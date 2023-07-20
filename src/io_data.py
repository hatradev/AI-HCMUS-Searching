# Read data from the file INPUT_x.txt
W, m, w, v, c, n = 0, 0, 0, 0, 0, 0


def read_data_from_file(x):
    file = open(f"../datasets/INPUT_{x}.txt")
    W = int(file.readline())  # the Knapsack's storage capacity
    m = int(file.readline())  # number of class
    w = file.readline().split(", ")
    w = [float(wi) for wi in w]  # list of weight of items
    v = file.readline().split(", ")
    v = [int(vi) for vi in v]  # list of values of items
    c = file.readline().split(", ")
    c = [int(ci) for ci in c]  # list of class
    n = len(w)  # number of items
    return W, m, w, v, c, n


def write_output_to_file(x, max_value, knapsack):
    file = open(f"../outputs/OUTPUT_{x}.txt", "w")
    file.write(str(max_value))
    file.write("\n")
    file.write(", ".join(map(str, knapsack)))
    file.close()
