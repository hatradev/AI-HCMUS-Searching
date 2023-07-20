def upper_bound(index, current_weight, current_value):
    remaining_weight = Total_weight - current_weight
    total_value = current_value

    # Sort items in descending order of value-to-weight ratio
    sorted_indices = sorted(range(index, n), key=lambda i: Items_value[i] / Items_weight[i], reverse=True)
    for i in sorted_indices:
        if Items_weight[i] <= remaining_weight:
            total_value += Items_value[i]
            remaining_weight -= Items_weight[i]
        else:
            total_value += (remaining_weight / Items_weight[i]) * Items_value[i]
            break

    return total_value

def knapSack_recursive_BNB(current_value, current_weight, index, selected_items, max_value, max_items):
    if index == n:
        if current_value > max_value: return current_value, selected_items[:]
        return max_value, max_items

    # Calculate the bound using fractional knapsack algorithm
    bound = upper_bound(index,current_weight,current_value)
    if bound <= max_value:  # Prune the branch if bound is not better than current max_value
        return max_value, max_items

    # Try not selecting the current item
    max_value, max_items = knapSack_recursive_BNB(current_value, current_weight, index + 1, selected_items, max_value, max_items)
    # Try selecting the current item
    if current_weight + Items_weight[index] <= Total_weight and selected_items[index] == 0:
        value = Items_value[index]
        selected_items[index] = selected_items[index] + 1
        selected_class[Items_class[index] - 1] = 1
        max_value, max_items = knapSack_recursive_BNB(current_value + value, current_weight + Items_weight[index], index+1, selected_items, max_value, max_items)
        selected_items[index] = selected_items[index] - 1
        selected_class[Items_class[index] - 1] = 0
    if not all(selected_class):
        for i in range(index, n):
            class_id = Items_class[i] - 1
            if not selected_class[class_id]:
                value = Items_value[i]
                weight = Items_weight[i]
                if current_weight + weight <= Total_weight and selected_items[i] == 0:
                    selected_items[i] = 1
                    selected_class[class_id] = 1
                    max_value, max_items = knapSack_recursive_BNB(current_value + value, current_weight + weight, i + 1, selected_items, max_value, max_items)
                    selected_items[i] = 0
                    selected_class[class_id] = 0
                    break        
    return max_value, max_items

# def KnapSack_select_class_before(Items_value, Items_weight,Items_class, n):
#     bound = [(float(Items_value[i])/float(Items_weight[i])) for i in range(n)]
#     current_weight = 0
#     current_value = 0
#     numbered_items = [i for i in range(n)]
#     dict = list(zip(bound,numbered_items))
#     dict.sort(reverse = True)
#     for (i,j) in dict:
#         if Items_class[j] not in selected_class:
#             selected_class.append(Items_class[j])
#             current_weight += Items_weight[j]
#             current_value += Items_value[j]
#             selected_items[j] += 1
#     return current_weight,current_value      

# def knapSack():
#     current_weight, current_value = KnapSack_select_class_before(Items_value,Items_weight,Items_class,n)
#     return knapSack_recursive_BNB(current_value,current_weight,0,selected_items, max_value, max_items)

file = open("C:/Users/Admin/Desktop/AI/ArtificialIntelligence_21CLC10/datasets/INPUT_2.txt")
Total_weight = int(file.readline())
Class_number = int(file.readline())
Items_weight = file.readline().split(', ')
Items_weight = [float(wi) for wi in Items_weight]
Items_value = file.readline().split(', ')
Items_value = [int(vi) for vi in Items_value]
Items_class = file.readline().split(', ')
Items_class = [int(ci) for ci in Items_class]
n = len(Items_weight)
max_value = 0
selected_class = [0 for i in range(Class_number)]
max_items = [0 for i in range(n)]
selected_items = [0 for i in range(n)]
# k = 2
# file = open("datasets/INPUT_{k}.txt")

max_value, max_items = knapSack_recursive_BNB(0,0,0,selected_items,max_value,max_items)

print("Maximum value:", max_value)
print("Selected items:")
for idx, count in enumerate(max_items):
    if count > 0:
        print(f"Item {idx} chosen {count} time(s)")