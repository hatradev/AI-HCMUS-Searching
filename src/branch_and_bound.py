from io_data import *
import signal
import time
timeout_seconds = 10
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
def signal_handler(signum, frame):
    raise Exception("Timed out!")
input_number_of_files = int(input("Enter number of input files: "))
for i in range(input_number_of_files):
    Total_weight, Class_number, Items_weight, Items_value, Items_class, n = read_data_from_file(i + 1)
    max_value = 0
    selected_class = [1 for i in range(Class_number)]
    max_items = [0 for i in range(n)]
    selected_items = [0 for i in range(n)]
    st = time.time()
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(60 if i + 1 <= 6 else 120)
    tf = True    
    try:
        max_value, max_items = knapSack_recursive_BNB(0,0,0,selected_items,max_value,max_items)
        if any(selected_class) == 1:
            max_value = 0
            max_items = [0] * n        
        write_output_to_file(i + 1, max_value, max_items, True)
    except TimeoutError:
        et = time.time()
        tf = False        
        write_output_to_file(i + 1, max_value, max_items, False)
    print(f"Execution time of Brute-force for input {i + 1} with {tf}: {et - st} seconds")