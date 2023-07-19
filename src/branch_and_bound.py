def knapSack_BNB():
    bound = [(float(Items_value[i])/float(Items_weight[i])) for i in range(n)]
    current_weight = 0
    current_value = 0
    numbered_items = [i for i in range(n)]
    sort_based_on_class = [[]]
    for i in range(Class_number):
        sort_based_on_class
        for j in range(n):
            if Items_class[j] == i + 1:
                tmp = []
                tmp.append(float(Items_value[j])/float(Items_weight[j]))
        tmp.sort(reverse = True)
        sort_based_on_class.append(tmp)
    dict = list(zip(bound,numbered_items))
    dict.sort(reverse = True)        
    for i in range(Class_number):
        for j in range(len(sort_based_on_class[i])):
            index = 0 
            for (ub,idx) in dict:
                if sort_based_on_class[i][j] == ub:
                    index = idx
                    break
            take = current_value + Items_value[index] + (Total_weight - current_weight - Items_weight[index])/sort_based_on_class[i][j]
            not_take = current_value + (Total_weight - current_weight)/sort_based_on_class[i][j]
            if take >= not_take and current_weight + Items_weight[index] <= Total_weight:
                current_weight += Items_weight[index]
                current_value += Items_value[index]
                selected_items[index] += 1             
                break               
    for (i,j) in dict:
        if selected_items[j] == 0:
            take = current_value + Items_value[j] + (Total_weight - current_weight - Items_weight[j])/bound[j]
            not_take = current_value + (Total_weight - current_weight)/bound[j]
            if take >= not_take and current_weight + Items_weight[j] <= Total_weight:
                current_weight += Items_weight[j]
                current_value += Items_value[j]
                selected_items[j] += 1
    return current_value             

file = open("datasets/INPUT_5.txt")
Total_weight = int(file.readline())
Class_number = int(file.readline())
Items_weight = file.readline().split(', ')
Items_weight = [float(wi) for wi in Items_weight]
Items_value = file.readline().split(', ')
Items_value = [int(vi) for vi in Items_value]
Items_class = file.readline().split(', ')
Items_class = [int(ci) for ci in Items_class]
n = len(Items_weight)
selected_class = [0 for i in range(Class_number)]
#max_items = [0 for i in range(n)]
selected_items = [0 for i in range(n)]   
print(knapSack_BNB())
print(selected_items)