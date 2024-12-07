# Task 1 - Implement a function to create a new list using list comprehension that contains squares of numbers 
# from 1 to n, where n is a parameter

def primeNumbersList(n):
    newList = []
    return [i ** 2 for i in range(1, n + 1)] # This has a space complexity of O(1) 

print("Task 1 - ", primeNumbersList(20))

# Task 2 - Reverse a sublist within a list from index i to j (inclusive)

def reverse_sublist(list, i, j):
    if i < 0 or j >= len(list) or i > j: # This has a space complexity of O(1)
        print("i is less than 0 or j is larger than the length of the list!")
    
    list[i:j+1] = list[i:j+1][::-1]

my_list = [10, 20, 30, 40, 50]
reverse_sublist(my_list, 1, 3)
print("Task 2 - ", my_list) 

# Task 3 - Merge two sorted lists into a single sorted list

def merge_sorted_lists(list1, list2):
    i, j = 0, 0
    merged_list = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    # This has a space complexity of O(len(list1) + len(list2)) because it needs to know the length of each list
    return merged_list


sorted_list1 = [1, 3, 5, 7]
sorted_list2 = [2, 4, 6, 8]
result = merge_sorted_lists(sorted_list1, sorted_list2)
print("Task 3 - ", result)  

