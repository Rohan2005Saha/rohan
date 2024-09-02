def sum_of_digits(n):

    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)

number = int(input("Enter a 4-digit positive number: "))

if 1000 <= number <= 9999:
    result = sum_of_digits(number)
    print(f"The sum of the digits of {number} is {result}")
else:
    print("Please enter a valid 4-digit positive number.")

