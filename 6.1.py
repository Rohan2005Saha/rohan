def remove_duplicate(input_list):
    return list(set(input_list))

sample_list = [1, 2, 3, 2, 4, 3, 5, 1]
result = remove_duplicate(sample_list)
print("List after removing duplicates:", result)