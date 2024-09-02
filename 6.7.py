# from functools import reduce

# sum_list = lambda lst: reduce(lambda x, y: x + y, lst)

numbers = [1, 2, 3, 4, 5]

result = sum(map(lambda x:x,numbers))

print(f"The sum of all values in the list is: {result}")