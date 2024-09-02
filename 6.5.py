'''Add 3 nos using lambda '''
add_three_numbers = lambda a, b, c: a + b + c

num1 = int(input("Enter 1st no :"))
num2 = int(input("Enter 2nd no :"))
num3 = int(input("Enter 3rd no :"))

result = add_three_numbers(num1, num2, num3)
print(f"The sum of {num1}, {num2}, and {num3} is {result}")
