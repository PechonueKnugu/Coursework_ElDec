import Student
from Observer import Observer


class Group(Observer):
    def __init__(self, name="", course=0):
        self.name = name
        self.course = course
        self.students = []

    def createGroup(self, name_g, course):
        self.name = name_g
        self.course = course

    def addStudent(self, student):
        self.students.append(student)
        student.attach(self)

    def removeStudent(self, student):
        self.students.remove(student)
        student.detach(self)

    def update(self, student, operation):
        if operation == "delete":
            for stud in self.students:
                if student.id == stud.id:
                    self.removeStudent(stud)

    def del_group(self):
        for i in self.students:
            i.detach(self)


def base():
    global list_gr
    list_gr = []
    with open("groups", 'r') as file:
        lines = file.readlines()
        for j in range(len(lines)):
            lines[j] = lines[j].split(";")
            group = Group()
            group.createGroup(lines[j][0], lines[j][1])
            students_id = lines[j][2].split(",")
            for k in students_id:
                student = Student.findStudent(k)
                if students_id != ['']:
                    group.addStudent(student)
            list_gr.append(group)
    file.close()


base()


def get_list_gr():
    return list_gr


def findGroup(name):
    for i in list_gr:
        if i.name == name:
            return i


def rep_check(student):
    for i in list_gr:
        for stud in i.students:
            if stud == student:
                return True
    return False
