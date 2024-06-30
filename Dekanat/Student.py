from Subject import Subject


class Student(Subject):
    def __init__(self, name="", surname="", age=0, id=0):
        super().__init__()
        self.name = name
        self.surname = surname
        self.age = age
        self.id = id
        self.observers = []

    def createStudent(self, name, surname, age, id):
        self.name = name
        self.surname = surname
        self.age = age
        self.id = id

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, operation):
        for observer in self.observers:
            observer.update(self, operation)


def base():
    global list_st
    list_st = []
    with open("students", 'r') as file:
        lines = file.readlines()
        for j in range(len(lines)):
            lines[j] = lines[j].split(";")
            student = Student()
            student.createStudent(lines[j][0], lines[j][1], lines[j][2], lines[j][3])
            list_st.append(student)
    file.close()


base()


def get_list_st():
    return list_st


def findStudent(id):
    for i in list_st:
        if i.id == id:
            return i


def minId():
    id_list = []
    for i in list_st:
        id_list.append(int(i.id))
    max_id = max(id_list)
    for i in range(1, int(max_id) + 2):
        if i not in id_list:
            return i
