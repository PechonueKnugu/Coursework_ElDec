from Room import Room
import Student


class Dormitory:
    def __init__(self, max_rooms=20, max_places=0):
        self.rooms = []
        self.max_rooms = max_rooms
        self.max_places = max_places

    def addRoom(self, room):
        self.rooms.append(room)


def base():
    global list_rm, dormitory
    list_rm = []
    with open("rooms", 'r') as file:
        lines = file.readlines()
        dormitory = Dormitory()
        for j in range(dormitory.max_rooms):
            room = Room()
            room.number = j + 1
            dormitory.addRoom(room)
            if j in range(len(lines)):
                lines[j] = lines[j].split(";")
        for i in range(len(lines)):
            for j in range(dormitory.max_rooms):
                if j + 1 == int(lines[i][0]):
                    room1 = Room()
                    students_id = lines[i][2].split(",")
                    room1.createRoom(lines[i][0], lines[i][1])
                    for k in students_id:
                        student = Student.findStudent(k)
                        room1.addStudent(student)
                    dormitory.rooms[j] = room1
    file.close()
    with open("dormitory", 'r') as file:
        lines = file.readlines()
        dormitory.max_places = int(lines[0])


base()


def findRoom(number):
    for i in dormitory.rooms:
        if i.number == number:
            return i


def list_st():
    list_st = []
    for i in dormitory.rooms:
        for j in dormitory.rooms[i].students:
            list_st.append(j)
    return list_st


def get_dormitory():
    return dormitory


def rep_check(student):
    for i in dormitory.rooms:
        for stud in i.students:
            if stud == student:
                return True
    return False
