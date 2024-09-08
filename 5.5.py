def cal_si(p,n,r):
    si=(p*n*r)/100
    return si

p=float(input("Enter the Principal amount :"))
n=float(input("Enter the no of yrs :"))
r=float(input("Enter the rate of interest :"))

si=cal_si(p,n,r)
print(f"The simple interest is : ₹{si:.2f}")

# OUTPUT
# Enter the Principal amount :1000
# Enter the no of yrs :2
# Enter the rate of interest :10
# The simple interest is : ₹200.00