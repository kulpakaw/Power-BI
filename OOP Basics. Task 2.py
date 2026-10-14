from abc import abstractmethod

class SchoolMember:
    
    @abstractmethod
    def show()-> str:
         pass
    
class Teacher(SchoolMember):
    def __init__(self,name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary
    
    def show(self)-> str:
        print(f"Teacher name: {self.name}, age: {self.age}, salary: {self.salary}")
        
class Student(SchoolMember):
    def __init__(self, name: str, age: int, grades):
        self.name = name
        self.age = age
        self.grades = grades
        
    def show(self)-> str:
        print(f"Student name: {self.name}, age: {self.age}, grades: {self.grades}")
        
        
member1 = Teacher("John", 35, 50000)
member2 = Student("Alice", 20, [90, 85, 92])
member1.show()
member2.show()