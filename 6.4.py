'''Sum of 1st 25 natural nos '''
def running_sum(n):

    if n == 1:
        return 1
    else:

        return n + running_sum(n - 1)


result = running_sum(25)
print(f"The running sum of the first 25 natural numbers is {result}")
