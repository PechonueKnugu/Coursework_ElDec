from tkinter import *
from tkinter import messagebox
import Dormitory
import Student


def win_dm_st():
    choice = IntVar()

    def changeS_D():
        room = Dormitory.findRoom(rm_num.get())
        ch = st_id.get().split(" ")
        if choice.get() == 1:
            for i in ch:
                if i and room is not None and len(room.students) < int(room.places) and Dormitory.rep_check(
                        Student.findStudent(i)) == False:
                    room.addStudent(Student.findStudent(i))
                elif i and room is not None and len(room.students) >= int(room.places):
                    messagebox.showerror("Помилка", "Переповнення студентів у кімнаті")
                    break
                elif i and room is not None and len(room.students) < int(room.places) and Dormitory.rep_check(
                        Student.findStudent(i)) == True:
                    messagebox.showerror("Помилка", "Студент вже поселений у іншій кімнаті")
                elif i is None:
                    messagebox.showerror("Помилка", "Студента не існує")
                elif room is None:
                    messagebox.showerror("Помилка", "Кімнати не існує")
        elif choice.get() == 2:
            for i in ch:
                if i and room is not None:
                    room.removeStudent(Student.findStudent(i))
                elif i is None:
                    messagebox.showerror("Помилка", "Студента не існує")
                elif room is None:
                    messagebox.showerror("Помилка", "Кімнати не існує")

    def radio1():
        choice.set(1)

    def radio2():
        choice.set(2)

    win1 = Tk()
    win1.title("Додавання та видалення студента з гуртожитку")
    win1.resizable(True, True)
    win1.config(bg='#4169E1')
    Label(win1, text="Номер кімнати", bg='#4169E1').grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    rm_num = Entry(win1, bg="#DEB887")
    rm_num.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    rad1 = Radiobutton(win1, text="Додати студента", variable=choice, value=1, command=radio1, bg='#4169E1')
    rad1.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    rad2 = Radiobutton(win1, text="Видалити студента", variable=choice, value=2, command=radio2, bg='#4169E1')
    rad2.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
    Label(win1, text="Введіть ID студента/студентів(введення через пробіл)", bg='#4169E1').grid(row=3, column=0,
                                                                                                columnspan=2, padx=5,
                                                                                                pady=5, sticky="nsew")
    st_id = Entry(win1, bg="#DEB887")
    st_id.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    Button(win1, text="Змінити", command=changeS_D, bg="#5F9EA0").grid(row=5, column=0, columnspan=2, padx=5, pady=5,
                                                                       sticky="nsew")
    choice.set(1)
    rad1.select()


def win_ch_rm():
    def changeS_D():
        room = Dormitory.findRoom(rm_num.get())
        pl = st_max.get()
        pl = int(pl)
        if room is not None and pl >= 0 and len(room.students) <= pl:
            pl = str(pl)
            room.places = pl
        elif room is not None and pl >= 0 and len(room.students) > pl:
            messagebox.showerror("Помилка", "Для початку випишіть зайвих студентів")
        elif room is not None and pl < 0:
            messagebox.showerror("Помилка", "Кількість місць не може бути від'ємним числом")
        elif room is None:
            messagebox.showerror("Помилка", "Кімнати не існує")
        elif pl is None:
            messagebox.showerror("Помилка", "Число введено неправильно")

    win1 = Tk()
    win1.title("Зміна даних про кімнату")
    win1.resizable(True, True)
    win1.config(bg='#4169E1')
    Label(win1, text="Номер кімнати", bg='#4169E1').grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    rm_num = Entry(win1, bg="#DEB887")
    rm_num.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    Label(win1, text="Введіть нову максимальну кількість студентів", bg='#4169E1').grid(row=3, column=0, columnspan=2,
                                                                                        padx=5, pady=5, sticky="nsew")
    st_max = Entry(win1, bg="#DEB887")
    st_max.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    Button(win1, text="Змінити", command=changeS_D, bg="#5F9EA0").grid(row=5, column=0, columnspan=2, padx=5, pady=5,
                                                                       sticky="nsew")


def win_ch_dm():
    def changeS_D():
        ch = val.get()
        dormitory = Dormitory.get_dormitory()
        if ch.isdigit() and int(ch) >= 0:
            dormitory.max_places = int(ch)
        elif ch.isdigit() and int(ch) < 0:
            messagebox.showerror("Помилка", "Кількість місць не може бути від'ємним числом")
        else:
            messagebox.showerror("Помилка", "Число введено неправильно")

    win1 = Tk()
    win1.title("Змінити дані про гуртожиток")
    win1.geometry("200x200")
    win1.config(bg='#4169E1')
    Label(win1, text="Максимальне число студентів", bg='#4169E1').grid(row=3, column=0, columnspan=2, padx=5, pady=5,
                                                                       sticky="nsew")
    val = Entry(win1, bg="#DEB887")
    val.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    Button(win1, text="Змінити", command=changeS_D, bg="#5F9EA0").grid(row=5, column=0, columnspan=2, padx=5, pady=5,
                                                                       sticky="nsew")


def win_sh_st():
    choice = IntVar()

    def changeS_D():
        if choice.get() == 1:
            dormitory = Dormitory.get_dormitory()
            list_room = []
            numofstud = 0
            for i in dormitory.rooms:
                local_list = f"Номер кімнати: {i.number}, Кількість вільних місць: {int(i.places) - len(i.students)}\n"
                for i in i.students:
                    local_list = local_list + f"ID: {i.id}, Студент: {i.name} {i.surname}, Вік: {i.age} років\n"
                    numofstud += 1
                list_room.append(local_list)
                list_st = "".join(list_room)
                text_data.delete(1.0, END)
                text_data.insert(1.0, ''.join(list_st))
            text_data.insert(0.0, f'Кількість студентів у гуртожитку: {numofstud}\n')
        elif choice.get() == 2:
            list_room = []
            room = Dormitory.findRoom(rm_num.get())
            if room is not None:
                local_list = f"Номер кімнати: {room.number}, Кількість вільних місць: {int(room.places) - len(room.students)}\n"
                for i in room.students:
                    local_list = local_list + f"ID: {i.id}, Студент: {i.name} {i.surname}, Вік: {i.age} років\n"
                list_room.append(local_list)
                list_st = "".join(list_room)
                text_data.delete(1.0, END)
                text_data.insert(1.0, ''.join(list_st))
            elif room is None:
                messagebox.showerror("Помилка", "Кімнати не існує")

    def radio1():
        choice.set(1)

    def radio2():
        choice.set(2)

    win1 = Tk()
    win1.title("Інформація про гуртожиток")
    win1.resizable(True, True)
    win1.config(bg='#4169E1')
    Label(win1, text="Номер кімнати", bg='#4169E1').grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    rm_num = Entry(win1, bg="#DEB887")
    rm_num.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    rad1 = Radiobutton(win1, text="Повна інформація", variable=choice, value=1, command=radio1, bg='#4169E1')
    rad1.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
    rad2 = Radiobutton(win1, text="Інформація про кімнату", variable=choice, value=2, command=radio2, bg='#4169E1')
    rad2.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
    text_data = Text(win1, width=100, height=20, bg="#DEB887")
    text_data.configure(font=("Ariel", 11))
    text_data.grid(row=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    Button(win1, text="Показати", command=changeS_D, bg="#5F9EA0").grid(row=4, column=0, columnspan=2, padx=5, pady=5,
                                                                        sticky="nsew")
    choice.set(1)
    rad1.select()
