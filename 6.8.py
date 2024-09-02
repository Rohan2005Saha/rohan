list1 = [1, 2, 3, 4, 5, 6]
list2 = [5, 6, 7, 8, 9, 2]

result = list(map(lambda x,y:x+y, list1, list2))

print(f"The sum of elements from both lists is: {result}")