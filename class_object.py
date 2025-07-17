#write the python code using class and object to print your name and age

class Name:
    def __init__(self, name,age):
        self.name = name
        self.age=age
    def printname(self):
        print(f"my name is {self.name}. I am {self.age} old")

a=Name("Suresh",22)
a.printname()



