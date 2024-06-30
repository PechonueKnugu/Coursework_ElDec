from tkinter import *
from tkinter import messagebox
import Student
import Group


def win_st_dl():
    def deleteS():
        i = st_id1.get()
        student = Student.findStudent(i)
        student.notify("delete")
        Student.get_list_st().remove(student)

    win1 = Tk()
    win1.title("Видалення студента")
    win1.geometry("200x200")
    win1.resizable(True, True)
    win1.config(bg='#4169E1')
    Label(win1, text="Введіть id студента", bg='#4169E1').grid(row=0, padx=5, pady=5, sticky="nsew")
    st_id1 = Entry(win1, bg="#DEB887")
    st_id1.grid(row=1, padx=5, pady=5, sticky="nsew")
    Button(win1, text="Видалити", command=deleteS, bg="#5F9EA0").grid(row=8, padx=5, pady=5, sticky="nsew")


def win_st_cr():
    def createS():
        n = st_name.get()
        s = st_surname.get()
        a = st_age.get()
        i = Student.minId()
        if n and s is not None and a.isdigit() is True:
            student = Student.Student()
            student.createStudent(n, s, a, str(i))
            Student.get_list_st().append(student)
        else:
            messagebox.showerror("Помилка", "Дані введено неправильно")

    win1 = Tk()
    win1.title("Створення студента")
    win1.geometry("200x250")
    win1.config(bg='#4169E1')
    Label(win1, text="Ім'я", bg='#4169E1').grid(row=0, padx=5, pady=5, sticky="nsew")
    st_name = Entry(win1, bg="#DEB887")
    st_name.grid(row=1, padx=5, pady=5, sticky="nsew")
    Label(win1, text="Прізвище", bg='#4169E1').grid(row=2, padx=5, pady=5, sticky="nsew")
    st_surname = Entry(win1, bg="#DEB887")
    st_surname.grid(row=3, padx=5, pady=5, sticky="nsew")
    Label(win1, text="Вік", bg='#4169E1').grid(row=4, padx=5, pady=5, sticky="nsew")
    st_age = Entry(win1, bg="#DEB887")
    st_age.grid(row=5, padx=5, pady=5, sticky="nsew")
    Button(win1, text="Створити", command=createS, bg="#5F9EA0").grid(row=8, padx=5, pady=5, sticky="nsew")


def win_st_ch():
    choice = IntVar()

    def changeS():
        student = Student.findStudent(st_id.get())
        ch = st_change.get()
        if student is not None:
            if choice.get() == 1:
                if ch != '':
                    student.name = ch
                elif ch == '':
                    messagebox.showerror("Помилка", "Дані введено неправильно")
            elif choice.get() == 2:
                if ch != '':
                    student.surname = ch
                elif ch == '':
                    messagebox.showerror("Помилка", "Дані введено неправильно")
            elif choice.get() == 3:
                if ch is int and ch != '':
                    student.age = ch
                elif ch is not int:
                    messagebox.showerror("Помилка", "Дані введено неправильно")
            student.notify("change")
        elif student is None:
            messagebox.showerror("Помилка", "Студента не існує")

    def radio1():
        choice.set(1)

    def radio2():
        choice.set(2)

    def radio3():
        choice.set(3)

    win1 = Tk()
    win1.title("Зміна інформації про студента")
    win1.resizable(True, True)
    win1.config(bg='#4169E1')
    Label(win1, text="ID студента", bg='#4169E1').grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
    st_id = Entry(win1, bg="#DEB887")
    st_id.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    rad1 = Radiobutton(win1, text="Змінити ім'я", variable=choice, value=1, command=radio1, bg='#4169E1')
    rad1.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    rad2 = Radiobutton(win1, text="Змінити прізвище", variable=choice, value=2, command=radio2, bg='#4169E1')
    rad2.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
    rad3 = Radiobutton(win1, text="Змінити вік", variable=choice, value=3, command=radio3, bg='#4169E1')
    rad3.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
    Label(win1, text="Введіть зміни:", bg='#4169E1').grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
    st_change = Entry(win1, bg="#DEB887")
    st_change.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
    Button(win1, text="Змінити", command=changeS, bg="#5F9EA0").grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
    choice.set(1)
    rad1.select()


def win_show_st():
    def show_st():
        list_stud = []
        students = Student.get_list_st()
        for i in students:
            local_list = f"ID: {i.id}, {i.name} {i.surname}"
            for j in i.observers:
                if type(j) == Group.Group:
                    local_list += f', Група: {j.name}'
            local_list += '\n'
            list_stud.append(local_list)
        list_st = "".join(list_stud)
        text_data.delete(1.0, END)
        text_data.insert(1.0, ''.join(list_st))

    win1 = Tk()
    win1.title("Список всіх студентів")
    win1.resizable(True, True)
    win1.config(bg='#4169E1')
    text_data = Text(win1, width=50, height=20, bg="#DEB887")
    text_data.configure(font=("Ariel", 11))
    text_data.grid(row=0, padx=5, pady=5, sticky="nsew")
    Button(win1, text="Показати", command=show_st, bg="#5F9EA0").grid(row=1, padx=5, pady=5, sticky="nsew")
