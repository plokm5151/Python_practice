class Person:
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        self.school = school
    
    def print_info(self):
        print(self.name)
        print(self.age)
        print(self.school)       

class Student(Person):
    def __init__(self):
        self.name="frank"
        self.age=24
        self.school="NTUST"


me_at_20=Person("plokm",20,"NPTU")
me_at_20.print_info()
me=Student()
me.print_info()
