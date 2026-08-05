#single inheritance
"""class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno=rollno
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll Number: {self.rollno}")

person1=Person("abc",25)
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")
student1=Student("xyz",20,101)
student1.display()"""

#multiple 
"""class Father:
    def skills(self):
        print("Father: gardening, Driving")
        
class Mother:
    def talents(self):
        print("Mother: Cooking, Painting")
        
class childs(Father,Mother):
    def Multi(self):
        self.skills()
        self.talents()
        
childs1=childs()
childs1.Multi()"""

#multilevel
'''class Employee:
    def __init__(self,name ,salary):
        self.name=name
        self.salary=salary
class Devloper(Employee):
    def __init__(self, name, salary,language):
        super().__init__(name, salary)
        self.language=language
        
class HR(Devloper):
    def __init__(self, name, salary, language):
        super().__init__(name, salary, language)
        
    def display(self):
        print(f"name :{self.name}\nsalary :{self.salary}\nlanguage :{self.language}")
        
emp1=HR("abc",20000,"Python")
emp2=HR("xyz",30000,"JAVA")
emp1.display()
emp2.display()'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
class Student(Person):
    def __init__(self,name,age,rollNo):
        super().__init__(self,name,age)
        self.rollNo=rollNo
        
class Sports(Person):
    def __init__(self, name, age,game):
        super().__init__(name, age)
        self.game=game

class SportsStudent(Student,Sports):
    def __init__(self, name, age, rollNo, game):
        Student.__init__(self,name, age, rollNo)
        Sports.__init__(self,name,age,game)
        
    def display(self):
        print(f"name :{self.name}\nage :{self.age}\nrollNo :{self.rollNo}\ngame :{self.game}")
        
s1=SportsStudent("abc",20,31,"kabaddi")
s1.display()        
        