def cal_sum_pro(a,b,c):
    total_s=a+b+c
    total_p = a * b * c
    return total_s,total_p
n1=int(input("Enter the 1st integer :"))
n2=int(input("Enter the 1st integer :"))
n3=int(input("Enter the 1st integer :"))

sum_r,pro_r=cal_sum_pro(n1,n2,n3)
print(f"The sum of three integers is :{sum_r}")
print(f"The product of three integers is :{pro_r}")

#OUTPUT
#Enter the 1st integer :5
# Enter the 1st integer :5
# Enter the 1st integer :2
# The sum of three integers is :12
# The product of three integers is :50