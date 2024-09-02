class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll}")

student1 = Student("Rohan Saha", 105)

student1.display()