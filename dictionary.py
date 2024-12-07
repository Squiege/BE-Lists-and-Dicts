# Task 1 - Implement a function to merge two dictionaries, 
# preserving the values of common keys from the second dictionary

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy() # This has a space complexity of O(n)
    merged.update(dict2)
    return merged

dictionaryOne = {"Soccer", "Football", "Baseball"}
dictionaryTwo = {"Swimming", "Track", "Cheer"}
resultTaskOne = merge_dictionaries(dictionaryOne, dictionaryTwo)
print("Task 1 - ", resultTaskOne)

# Task 2 - Implement a function to find the intersection of two dictionaries, 
# i.e., keys common to both dictionaries along with their values.

def commonKeys(dict1, dict2):
    common_keys = dict1.keys() & dict2.keys()
    intersection = {key: dict1[key] for key in common_keys if dict1[key] == dict2[key]} # This is O(k) space complexity because its looking for matching key pairs
    return intersection

dictionary1 = {'a': 1, 'b': 2, 'c': 3 }
dictionary2 = {'d': 4, 'b': 2, 'f': 6}
resultTaskTwo = commonKeys(dictionary1, dictionary2)
print("Task 2 - ", resultTaskTwo)

# Task 3 - Cound amount of words from a list

def countWords(lst):
    common_word_count = {}

    for word in lst: # This has a space complexity of O(n)
        common_word_count[word] = common_word_count.get(word, 0) + 1 # This has a space complexity of O(k)
    return common_word_count
    
word_list = ["John", "Harold", "Jane", "John", "Penny", "Jane"]
resultTaskThree = countWords(word_list)
print("Task 3 - ", resultTaskThree)
