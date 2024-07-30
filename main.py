class Person:
    def __init__(self,name,age,workspaces):
        self.name = name
        self.age = age
        self.workspaces = workspaces

    def workspace(self):
        print("Hello, my name is ",self.name)
        print("I have done ",self.workspaces," out of 181")

p1 = Person("Viaan", 7,0)
p2 = Person("John", 12, 123)


#del p1
#print(p1.age)
#print(p2.name)
p2.workspace()
