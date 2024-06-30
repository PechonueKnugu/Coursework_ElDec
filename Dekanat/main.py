from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import Win_Student
import Win_Group
import Win_Dormitory
import Win_Search
import Student
import Group
import Dormitory

def save_data():
    students = Student.get_list_st()
    with open("students", 'w') as file:
        for i in students:
            n = i.name
            s = i.surname
            a = i.age
            id = i.id
            file.write(f'{n};{s};{a};{id};\n')
    file.close()
    groups = Group.get_list_gr()
    with open("groups", 'r+') as file:
        for i in groups:
            n = i.name
            c = i.course
            s = i.students
            id_list = []
            for i in s:
                id_list.append(str(i.id))
            id_list = ",".join(id_list)
            file.write(f'{n};{c};{id_list};\n')
    file.close()
    dormitory = Dormitory.get_dormitory()
    with open("rooms", 'w') as file:
        ids = 0
        list_ids = []
        list_write = []
        for i in dormitory.rooms:
            if i.students is not [] and i != dormitory.rooms[len(dormitory.rooms)-1]:
                n = i.number
                p = i.places
                s = i.students
                id_list = []
                for j in s:
                    id_list.append(str(j.id))
                    ids += 1
                list_write.append(f'{n};{p};{",".join(id_list)};\n')
                list_ids.append(','.join(id_list))
            elif i.students is not [] and i == dormitory.rooms[len(dormitory.rooms)-1]:
                n = i.number
                p = i.places
                s = i.students
                id_list = []
                for j in s:
                    id_list.append(str(j.id))
                    ids += 1
                list_write.append(f'{n};{p};{",".join(id_list)};\n')
                list_ids.append(','.join(id_list))
                if ids > dormitory.max_places:
                    messagebox.showerror("Помилка", "Переповення студентів у гуртожитку")
                    break
                else:
                    for i in list_write:
                        file.write(i)
    file.close()
    with open("dormitory", 'w') as file:
        file.write(f'{dormitory.max_places}')

root = Tk()
root.title("Електронний деканат")
root.geometry("515x536")
root.config(bg='#2F4F4F', highlightcolor='black', highlightthickness=3)

notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky="nsew")

image = Image.open('background.png')
image = image.resize((500, 500), Image.Resampling.NEAREST)
image = ImageTk.PhotoImage(image)

frame1 = Frame(notebook)
frame1.config(bg='#4169E1')
notebook.add(frame1, text='Інформація')
Label(frame1, image=image).grid(row=0, rowspan=21)
Label(frame1, text = 'Електронний деканат').grid(row=0, padx=10, pady=10)
Label(frame1, text = 'Перед закриттям програми натисніть кнопку "Зберегти дані"').grid(row=1, padx=10, pady=10)
Button(frame1, text = 'Зберегти дані', command=save_data, bg="#5F9EA0").grid(row=2, padx=10, pady=10)

frame2 = Frame(notebook)
frame2.config(bg='#4169E1')
notebook.add(frame2, text='Студенти')
Label(frame2, image=image).grid(row=0, rowspan=21)
Button(frame2, text="Новий студент", command=Win_Student.win_st_cr, bg="#5F9EA0").grid(row=0, padx=10, pady=10)
Button(frame2, text="Видалити студента", command=Win_Student.win_st_dl, bg="#5F9EA0").grid(row=1, padx=10, pady=10)
Button(frame2, text="Змінити дані студента", command=Win_Student.win_st_ch, bg="#5F9EA0").grid(row=2, padx=10, pady=10)
Button(frame2, text="Всі студенти", command=Win_Student.win_show_st, bg="#5F9EA0").grid(row=3, padx=10, pady=10)

frame3 = Frame(notebook)
frame3.config(bg='#4169E1')
notebook.add(frame3, text='Групи')
Label(frame3, image=image).grid(row=0, rowspan=21)
Button(frame3, text="Нова група", command=Win_Group.win_gr_cr, bg="#5F9EA0").grid(row=0, padx=10, pady=10)
Button(frame3, text="Видалити групу", command=Win_Group.win_gr_dl, bg="#5F9EA0").grid(row=1, padx=10, pady=10)
Button(frame3, text="Змінити дані групи", command=Win_Group.win_gr_ch, bg="#5F9EA0").grid(row=2, padx=10, pady=10)
Button(frame3, text="Дані окремої групи", command=Win_Group.win_show_gr, bg="#5F9EA0").grid(row=3, padx=10, pady=10)
Button(frame3, text="Дані всіх груп", command=Win_Group.win_show_grs, bg="#5F9EA0").grid(row=4, padx=10, pady=10)
Button(frame3, text="Додавання/Видалення студентів", command=Win_Group.win_gr_st, bg="#5F9EA0").grid(row=5, padx=10, pady=10)

frame4 = Frame(notebook)
frame4.config(bg='#4169E1')
notebook.add(frame4, text='Гуртожиток')
Label(frame4, image=image).grid(row=0, rowspan=21)
Button(frame4, text="Додавання/Видалення студентів", command=Win_Dormitory.win_dm_st, bg="#5F9EA0").grid(row=0, padx=10, pady=10)
Button(frame4, text="Змінити дані кімнати", command=Win_Dormitory.win_ch_rm, bg="#5F9EA0").grid(row=1, padx=10, pady=10)
Button(frame4, text="Змінити дані гурожитку", command=Win_Dormitory.win_ch_dm, bg="#5F9EA0").grid(row=2, padx=10, pady=10)
Button(frame4, text="Подивитися дані про гуртожиток", command=Win_Dormitory.win_sh_st, bg="#5F9EA0").grid(row=3, padx=10, pady=10)

frame5 = Frame(notebook)
frame5.config(bg='#4169E1')
notebook.add(frame5, text='Пошук')
Label(frame5, image=image).grid(row=0, rowspan=21)
Button(frame5, text="Пошук за ім'ям та прізвищем", command=Win_Search.win_sr_st, bg="#5F9EA0").grid(row=0, padx=10, pady=10)
Button(frame5, text="Пошук у певній групі", command=Win_Search.win_sr_gr, bg="#5F9EA0").grid(row=1, padx=10, pady=10)
Button(frame5, text="Пошук у гуртожитку", command=Win_Search.win_sr_dm, bg="#5F9EA0").grid(row=2, padx=10, pady=10)

root.mainloop()
