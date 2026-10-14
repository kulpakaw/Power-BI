from abc import ABC, abstractmethod

class SchoolMember(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


    @abstractmethod
    def show(self) -> str:
        pass


class Teacher(SchoolMember):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age)
        self.salary = salary


    def show(self) -> str:
        return f"Teacher name: {self.name}, age: {self.age}, salary: {self.salary}"


class Student(SchoolMember):
    def __init__(self, name: str, age: int, grades):
        super().__init__(name, age)
        self.grades = grades


    def show(self) -> str:
        return f"Student name: {self.name}, age: {self.age}, grades: {self.grades}"


member1 = Teacher("John", 35, 50000)
member2 = Student("Alice", 20, [90, 85, 92])

print(member1.show())
print(member2.show())

persons = [
Teacher("Mr.Snape", 40, 3000),
Student("Harry", 16, 75)
]

for person in persons:
    print(person.show())


