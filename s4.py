class School:
    def print_school(self):
        print("This is in School class")
class Student1(School):
    def print_student(self):
        print("This is in Student one class")
class Student2(School): #hierarchical
    def print_student2(self):
        print("This is in School two class")
class Main(Student1, School): #multiple
    def main_fun(self):
        print("This is in Main class")
obj1 = Main()
obj1.print_school()
obj1.print_student()
