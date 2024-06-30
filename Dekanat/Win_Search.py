from tkinter import *
import Group
import Student
import Dormitory
import Room

def win_sr_st():

    def search():
        info = st_in.get()
        list_st = Student.get_list_st()
        list_fn = []
        list_stud = []
        for i in list_st:
            if info in i.name:
                list_fn.append(i)
            elif info in i.surname:
                list_fn.append(i)
        for student in list_fn:
            local_list = f"ID: {student.id}, {student.name} {student.surname}"
            for i in student.observers:
                if type(i) == Group.Group:
                    local_list += f', Група: {i.name}'
            local_list = local_list + '\n'
            list_stud.append(local_list)
        list_st = "".join(list_stud)
        text_data.delete(1.0, END)
        text_data.insert(1.0, ''.join(list_st))


    win1 = Tk()
    win1.title("Пошук")
    win1.resizable(True, True)
    win1.config(bg='#4169E1')
    Label(win1, text="Введіть ім'я або прізвище", bg='#4169E1').grid(row=0, column=0,padx=5, pady=5, sticky="nsew")
    st_in = Entry(win1, bg="#DEB887")
    st_in.grid(row=1, column=0, columnspan=2,padx=5, pady=5, sticky="nsew")
    Button(win1, text="Знайти", command=search, bg="#5F9EA0").grid(row=2, column=0, columnspan=2,padx=5, pady=5, sticky="nsew")
    text_data = Text(win1, width=60, height=10, bg="#DEB887")
    text_data.configure(font=("Ariel", 11))
    text_data.grid(row=3,padx=5, pady=5, sticky="nsew")

def win_sr_gr():

    def search():
        info = st_in.get()
        list_st = Group.findGroup(gr_in.get()).students
        list_fn = []
        list_stud = []
        for i in list_st:
            if info in i.name:
                list_fn.append(i)
            if info in i.surname:
                list_fn.append(i)
        for student in list_fn:
            local_list = f"ID: {student.id}, {student.name} {student.surname}\n"
            list_stud.append(local_list)
        list_st = "".join(list_stud)
        text_data.delete(1.0, END)
        text_data.insert(1.0, ''.join(list_st))


    win1 = Tk()
    win1.title("Пошук у групі")
    win1.resizable(True, True)
    win1.config(bg='#4169E1')
    Label(win1, text="Введіть назву групи", bg='#4169E1').grid(row=0, column=0,padx=5, pady=5, sticky="nsew")
    gr_in = Entry(win1, bg="#DEB887")
    gr_in.grid(row=1, column=0, columnspan=2,padx=5, pady=5, sticky="nsew")
    Label(win1, text="Введіть ім'я або прізвище", bg='#4169E1').grid(row=2, column=0,padx=5, pady=5, sticky="nsew")
    st_in = Entry(win1, bg="#DEB887")
    st_in.grid(row=3, column=0, columnspan=2,padx=5, pady=5, sticky="nsew")
    Button(win1, text="Знайти", command=search, bg="#5F9EA0").grid(row=4, column=0, columnspan=2,padx=5, pady=5, sticky="nsew")
    text_data = Text(win1, width=60, height=10, bg="#DEB887")
    text_data.configure(font=("Ariel", 11))
    text_data.grid(row=5,padx=5, pady=5, sticky="nsew")

def win_sr_dm():

    def search():
        info = st_in.get()
        dormitory = Dormitory.get_dormitory()
        list_fn = []
        list_stud = []
        for i in dormitory.rooms:
            for j in i.students:
                if info in j.name:
                    list_fn.append(j)
                if info in j.surname:
                    list_fn.append(j)
        for student in list_fn:
            local_list = f"ID: {student.id}, {student.name} {student.surname}"
            for i in student.observers:
                if type(i) == Room.Room:
                    local_list += f', Кімната: {i.number}'
            local_list = local_list + '\n'
            list_stud.append(local_list)
        list_st = "".join(list_stud)
        text_data.delete(1.0, END)
        text_data.insert(1.0, ''.join(list_st))


    win1 = Tk()
    win1.title("Пошук у гуртожитку")
    win1.resizable(True, True)
    win1.config(bg='#4169E1')
    Label(win1, text="Введіть ім'я або прізвище", bg='#4169E1').grid(row=0, column=0,padx=5, pady=5, sticky="nsew")
    st_in = Entry(win1, bg="#DEB887")
    st_in.grid(row=1, column=0, columnspan=2,padx=5, pady=5, sticky="nsew")
    Button(win1, text="Знайти", command=search, bg="#5F9EA0").grid(row=2, column=0, columnspan=2,padx=5, pady=5, sticky="nsew")
    text_data = Text(win1, width=60, height=10, bg="#DEB887")
    text_data.configure(font=("Ariel", 11))
    text_data.grid(row=3,padx=5, pady=5, sticky="nsew")
