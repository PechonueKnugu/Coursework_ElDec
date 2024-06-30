from Observer import Observer

class Room(Observer):
    def __init__(self, number=0, places=0):
        self.number = number
        self.places = places
        self.students = []

    def addStudent(self, student):
        self.students.append(student)
        student.attach(self)

    def createRoom(self, number, places):
        self.places = places
        self.number = number

    def removeStudent(self, student):
        self.students.remove(student)
        student.detach(self)

    def update(self, student, operation):
        if operation == "delete":
            for stud in self.students:
                if student.id == stud.id:
                    self.removeStudent(stud)
