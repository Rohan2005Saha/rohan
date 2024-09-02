'''To accept a string in lowercase and convert it into uppercase using lambda '''
to_uppercase = lambda s: s.upper()

input_string = input("Enter a string in lowercase: ")

result = to_uppercase(input_string)

print(f"The uppercase version of the string is: {result}")
