students={
    1:"Rup",
    2:"Rai",
    3:"Riju",
    4:"Riya"
}
roll=int(input("Enter roll no :"))
if roll in students:
    print(f"Congratulations {students[roll]}")
else:
    print(f"Congratulations students!")

#OUTPUT
#Enter roll no :1
#Congratulations Rup
#Enter roll no :5
#Congratulations students!
