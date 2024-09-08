boys={"Riju":12,"Rahul":23,"Rohit":34}
girls={"Riya":15,"Rai":13,"Sana":28}
c={}
for i in (boys,girls):
    c.update(i)
print("Merged dictionary :",c)

#OUTPUT
#Merged dictionary : {'Riju': 12, 'Rahul': 23, 'Rohit': 34, 'Riya': 15, 'Rai': 13, 'Sana': 28}