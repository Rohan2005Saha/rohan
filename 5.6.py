def cal_si(p,n,r,q):
    a=p*(1+r/q)**(n)
    ci=a-p
    return ci

p=float(input("Enter the Principal amount :"))
n=float(input("Enter the no of yrs :"))
r=float(input("Enter the rate of interest :"))
q=float(input("Enter the no of times the interest is compounded per yr :"))
i=cal_si(p, n, r,q)
print(f"The compound interest is : ₹ {i:.2f}")

# OUTPUT
# Enter the Principal amount :10000
# Enter the no of yrs :2
# Enter the rate of interest :10
# Enter the no of times the interest is compounded per yr :2
# The compound interest is : ₹ 350000.00