from tkinter import *
from tkinter import messagebox
import Group
import Student


def win_gr_cr():
    def createG():
        n = gr_name.get()
        c = gr_course.get()
        groups = Group.get_list_gr()
        isExists = 0
        for i in groups:
            if i.name == n:
                isExists = 1
        if isExists == 1:
            messagebox.showerror("Помилка", "Така група вже існує")
        elif n and c is not None and c.isdigit() is True:
            group = Group.Group()
            group.createGroup(n, c)
            groups.append(group)
        else:
            messagebox.showerror("Помилка", "Дані введено неправильно")

    win1 = Tk()
    win1.title("Створення групи")
    win1.geometry("200x200")
    win1.config(bg='#4169E1')
    Label(win1, text="Назва", bg='#4169E1').grid(row=0, padx=5, pady=5, sticky="nsew")
    gr_name = Entry(win1, bg="#DEB887")
    gr_name.grid(row=1, padx=5, pady=5, sticky="nsew")
    Label(win1, text="Курс", bg='#4169E1').grid(row=2, padx=5, pady=5, sticky="nsew")
    gr_course = Entry(win1, bg="#DEB887")
    gr_course.grid(row=3, padx=5, pady=5, sticky="nsew")
    Button(win1, text="Створити", command=createG, bg="#5F9EA0").grid(row=4, padx=5, pady=5, sticky="nsew")


def win_gr_dl():
    def deleteG():
        i = gr_name.get()
        groups = Group.get_list_gr()
        for j in groups:
            if j.name == i:
                j.del_group()
                groups.remove(j)
                return
        messagebox.showerror("Помилка", "Групи не знайдено")

    win1 = Tk()
    win1.title("Видалення групи")
    win1.geometry("200x200")
    win1.config(bg='#4169E1')
    Label(win1, text="Введіть назву групи", bg='#4169E1').grid(row=0, padx=5, pady=5, sticky="nsew")
    gr_name = Entry(win1, bg="#DEB887")
    gr_name.grid(row=1, padx=5, pady=5, sticky="nsew")
    Button(win1, text="Видалити", command=deleteG, bg="#5F9EA0").grid(row=2, padx=5, pady=5, sticky="nsew")


def win_gr_ch():
    choice = IntVar()

    def changeG():
        line = Group.findGroup(gr_name.get())
        ch = st_change.get()
        if line is not None:
            if choice.get() == 1:
                groups = Group.get_list_gr()
                isExists = 0
                for i in groups:
                    if i.name == ch:
                        isExists = 1
                if isExists == 1:
                    messagebox.showerror("Помилка", "Така група вже існує")
                else:
                    if ch != '':
                        line.name = ch
                    else:
                        messagebox.showerror("Помилка", "Дані введено неправильно")
            elif choice.get() == 2:
                if ch.isdigit() is True:
                    line.course = ch
                else:
                    messagebox.showerror("Помилка", "Дані введено неправильно")
        else:
            messagebox.showerror("Помилка", "Групи не існує")

    def radio1():
        choice.set(1)

    def radio2():
        choice.set(2)

    win1 = Tk()
    win1.title("Зміна інформації про групу")
    win1.resizable(True, True)
    win1.config(bg='#4169E1')
    Label(win1, text="Назва групи", bg='#4169E1').grid(row=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    gr_name = Entry(win1, bg="#DEB887")
    gr_name.grid(row=1, columnspan=2, padx=5, pady=5, sticky="nsew")
    rad1 = Radiobutton(win1, text="Змінити назву", variable=choice, value=1, command=radio1, bg='#4169E1')
    rad1.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    rad2 = Radiobutton(win1, text="Змінити курс", variable=choice, value=2, command=radio2, bg='#4169E1')
    rad2.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
    Label(win1, text="Введіть зміни:", bg='#4169E1').grid(row=3, columnspan=2, padx=5, pady=5, sticky="nsew")
    st_change = Entry(win1, bg="#DEB887")
    st_change.grid(row=4, columnspan=2, padx=5, pady=5, sticky="nsew")
    Button(win1, text="Змінити", command=changeG, bg="#5F9EA0").grid(row=5, columnspan=2, padx=5, pady=5, sticky="nsew")
    rad1.select()
    choice.set(1)


def win_show_gr():
    def show_gr():
        gr_name = ent_group.get()
        list_group = []
        group = Group.findGroup(gr_name)
        if group is not None:
            local_list = f"Назва: {group.name}, Курс: {group.course}, Кількість студентів: {len(group.students)}\n"
            for j in group.students:
                local_list = local_list + f"ID: {j.id}, {j.name} {j.surname}\n"
            list_group.append(local_list)
            list_st = "".join(list_group)
            text_data.delete(1.0, END)
            text_data.insert(1.0, ''.join(list_st))
        elif group is None:
            messagebox.showerror("Помилка", "Групи не існує")

    win1 = Tk()
    win1.title("Дані групи")
    win1.resizable(True, True)
    win1.config(bg='#4169E1')
    Label(win1, text='Введіть назву групи', bg='#4169E1').grid(row=0, padx=5, pady=5, sticky="nsew")
    ent_group = Entry(win1, bg="#DEB887")
    ent_group.grid(row=1, padx=5, pady=5, sticky="nsew")
    text_data = Text(win1, width=100, height=20, bg="#DEB887")
    text_data.configure(font=("Ariel", 11))
    text_data.grid(row=2, padx=5, pady=5, sticky="nsew")
    Button(win1, text="Показати", command=show_gr, bg="#5F9EA0").grid(row=3, padx=5, pady=5, sticky="nsew")


def win_show_grs():
    def show_grs():
        list_group = []
        groups = Group.get_list_gr()
        for i in groups:
            local_list = f"Назва: {i.name}, Курс: {i.course}, Кількість студентів: {len(i.students)}\n"
            for j in i.students:
                local_list = local_list + f"ID: {j.id}, {j.name} {j.surname}\n"
            list_group.append(local_list)
            list_st = "".join(list_group)
            text_data.delete(1.0, END)
            text_data.insert(1.0, ''.join(list_st))

    win1 = Tk()
    win1.title("Список всіх груп")
    win1.resizable(True, True)
    win1.config(bg='#4169E1')
    text_data = Text(win1, width=100, height=20, bg="#DEB887")
    text_data.configure(font=("Ariel", 11))
    text_data.grid(row=0, padx=5, pady=5, sticky="nsew")
    Button(win1, text="Показати", command=show_grs, bg="#5F9EA0").grid(row=1, padx=5, pady=5, sticky="nsew")


def win_gr_st():
    choice = IntVar()

    def changeS_G():
        group = Group.findGroup(gr_name.get())
        ch = st_id.get().split(" ")
        if choice.get() == 1:
            for i in ch:
                if i and group is not None and Group.rep_check(Student.findStudent(i)) is False:
                    group.addStudent(Student.findStudent(i))
                elif i and group is not None and Group.rep_check(Student.findStudent(i)) is True:
                    messagebox.showerror("Помилка", "Цей стедент вже знаходиться у групі")
                elif group is None:
                    messagebox.showerror("Помилка", "Групи не існує")
                elif i is None:
                    messagebox.showerror("Помилка", "Студента не існує")
        elif choice.get() == 2:
            for i in ch:
                if i is not None:
                    group.removeStudent(Student.findStudent(i))

    def radio1():
        choice.set(1)

    def radio2():
        choice.set(2)

    win1 = Tk()
    win1.title("Додавання та видалення студента з групи")
    win1.resizable(True, True)
    win1.config(bg='#4169E1')
    Label(win1, text="Назва групи", bg='#4169E1').grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    gr_name = Entry(win1, bg="#DEB887")
    gr_name.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    rad1 = Radiobutton(win1, text="Додати студента", variable=choice, value=1, command=radio1, bg='#4169E1')
    rad1.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    rad2 = Radiobutton(win1, text="Видалити студента", variable=choice, value=2, command=radio2, bg='#4169E1')
    rad2.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
    Label(win1, text="Введіть ID студента/студентів(введення через пробіл)", bg='#4169E1').grid(row=3, column=0,
                                                                                                columnspan=2, padx=5,
                                                                                                pady=5, sticky="nsew")
    st_id = Entry(win1, bg="#DEB887")
    st_id.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    Button(win1, text="Змінити", command=changeS_G, bg="#5F9EA0").grid(row=5, column=0, columnspan=2, padx=5, pady=5,
                                                                       sticky="nsew")
    choice.set(1)
    rad1.select()
