class Student:
    'Common base class for all students'
    student_count=0

    def __init__(self, name, id):
       self.name = name
       self.id = id
       Student.student_count+=1

    def printStudentData(self):
       print ("Name : ", self.name, ", Id : ", self.id)

s=Student(name=input('enter name:'),id=input(" enter id:"))
s.printStudentData()
print(Student.__name__)