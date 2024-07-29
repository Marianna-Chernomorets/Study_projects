from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fd
import numpy as np
from random import choice, randint
from string import punctuation
import os
import csv
import random
from tkinter.messagebox import askyesno


def exite(window):
    result = askyesno(message="Вы хотите выйти?")
    if result:
        window.destroy()


def ex_1_pz_1(entry1, entry2, entry3, window):
    a = float(entry1.get())
    b = float(entry2.get())
    c = float(entry3.get())
    label1 = Label(window, text="", width=29, justify=RIGHT)
    label1.grid(row=13, column=2, sticky=W)
    label1['text'] = ''
    if c - a == 0:
        label1['text'] = 'Ошибка. Делить на ноль нельзя'
        label1['fg'] = ['red']
    else:
        v = abs(1 - a * b ** c - a * (b ** 2 - c ** 2) + (b - c + a) * (12 + b) / (c - a))
        if label1['text'] == 'Ошибка. Делить на ноль нельзя':
            label1.destroy()
            label1 = Label(window, text=v, width=29, justify=RIGHT)
            label1.grid(row=13, column=2, sticky=W)
        else:
            label = Label(window, text=v, width=10, justify=RIGHT)
            label.grid(row=13, column=2, sticky=W)


def ex_2_pz_1(entry1, window):
    a = entry1.get().split()
    b = " ".join(a[1::2])
    label = Label(window, text=b, justify=RIGHT)
    label.grid(row=13, column=2, sticky=W)


def ex_3_pz_1(entry1, window):
    a = np.array((entry1.get().split()))
    k = 1
    c = 0
    for i in a:
        if int(i) < 10:
            k *= int(i)
            c += 1
    if c == 0:
        k = 0
    label = Label(window, text=k, justify=RIGHT)
    label.grid(row=13, column=2, sticky=W)


def ex_4_pz_1(entry1, window):
    a = np.array((entry1.get().split()))
    k = 0
    c = 0
    for i in a:
        k += int(i)
        c += 1
    sr = k/c
    label = Label(window, text=sr, justify=RIGHT)
    label.grid(row=13, column=2, sticky=W)


def ex_1_pz_2(entry1, window, label1):
    my_number = 10
    a = 10
    while a == my_number:
        label1['text'] = 'Введите число еще раз'
        user_number = entry1.get()
        a = user_number
        if int(a) != my_number:
            label = Label(window, text=f'Загаданное число было {my_number}', justify=RIGHT)
            label.grid(row=13, column=2, sticky=W)
        else:
            entry1.delete(0, END)


def ex_2_pz_2(entry1, window):
    a = entry1.get()
    c = a.split(', ')
    b = len(c)
    tv = ttk.Treeview(window, columns=(), show="headings", height=0)
    tv["columns"] = tuple(range(b))
    for i in range(b):
        tv.heading(i, text=c[i])
        tv.column(i, width=50, anchor=CENTER)
    tv.grid()
    v = []
    for i in c:
        if i[-1] == 'r':
            v.append(i)
    s = len(v)
    tv1 = ttk.Treeview(window, columns=(), show="headings", height=0)
    tv1["columns"] = tuple(range(s))
    for i in range(s):
        tv1.heading(i, text=v[i])
        tv1.column(i, width=50, anchor=CENTER)
    tv1.grid()


def ex_3_pz_2(window):
    result = [choice('012456789') for _ in range(5)]
    result.insert(randint(0, 5), '3')
    a = ''.join(result)
    label = Label(window, text=a, justify=RIGHT)
    label.grid(row=13, column=2, sticky=W)


def ex_4_pz_2(entry1, window):
    a = entry1.get().upper()
    b = ''
    for i in a:
        if i == 'Л':
            b += i
    label = Label(window, text=b, justify=RIGHT)
    label.grid(row=13, column=2, sticky=W)


def ex_1_pz_3(entry1, window):
    a = entry1.get().translate(str.maketrans('', '', punctuation)).split(' ')
    b = ''
    for i in a:
        if (len(i) > 4) and (len(i) < 10):
            b += i
            b += ' '
    c = b.rstrip()
    label = Label(window, text=c, justify=RIGHT)
    label.grid(row=13, column=2, sticky=W)


def ex_2_pz_3(window):
    tv = ttk.Treeview(window, height=3)

    a = '''Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;
    _Петров;Семен;Игоревич;22 года;Студент 2 курса'''''
    a = a.split('_')
    b = a[1].split(';')
    c = a[2].split(';')
    b[3], b[4] = b[4], ' ' + b[3]
    c[3], c[4] = c[4], ' ' + c[3]
    b[3] += ''.join(b[4:5])
    del b[4:5]
    del b[-1]
    c[3] += ''.join(c[4:5])
    del c[4:5]

    tv['columns'] = ('f', 'i', 'o', 'student')
    tv.column('#0', width=0, stretch=NO)
    tv.column('f', anchor=CENTER, width=80)
    tv.column('i', anchor=CENTER, width=80)
    tv.column('o', anchor=CENTER, width=80)
    tv.column('student', anchor=CENTER, width=150)

    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('f', text='Фамилия', anchor=CENTER)
    tv.heading('i', text='Имя', anchor=CENTER)
    tv.heading('o', text='Отчество', anchor=CENTER)
    tv.heading('student', text='О студенте', anchor=CENTER)

    tv.insert(parent='', index=0, text='', values=(b[0], b[1], b[2], b[3]))
    tv.insert(parent='', index=1, text='', values=(c[0], c[1], c[2], c[3]))

    tv.grid(row=13)


def ex_3_pz_3_func1(window):
    tv = ttk.Treeview(window)
    v = '''ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;
    Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;
    Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;
    Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;21 год;
    Студент 2 курса'''
    a = v.split(';_')
    b = a[1:]

    tv['columns'] = ('fio', 'age', 'student')
    tv.column('#0', width=0, stretch=NO)
    tv.column('fio', anchor=CENTER, width=200)
    tv.column('age', anchor=CENTER, width=80)
    tv.column('student', anchor=CENTER, width=150)

    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('fio', text='Фамилия', anchor=CENTER)
    tv.heading('age', text='Имя', anchor=CENTER)
    tv.heading('student', text='Категория', anchor=CENTER)

    for i in range(0, 8):
        c = b[i].split(';')
        tv.insert(parent='', index=i, text='', values=(c[0], c[1], c[2]))

    tv.grid()


def ex_3_pz_3_func2(window):
    v = '''ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;
    _Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;
    _Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;
    _Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;
    _Петров Всеволод Борисович;21 год;Студент 2 курса'''
    a = v.split(';_')
    b = a[1:]

    tv1 = ttk.Treeview(window)
    tv1['columns'] = ('fio', 'age', 'student')
    tv1.column('#0', width=0, stretch=NO)
    tv1.column('fio', anchor=CENTER, width=200)
    tv1.column('age', anchor=CENTER, width=80)
    tv1.column('student', anchor=CENTER, width=150)

    tv1.heading('#0', text='', anchor=CENTER)
    tv1.heading('fio', text='Фамилия', anchor=CENTER)
    tv1.heading('age', text='Имя', anchor=CENTER)
    tv1.heading('student', text='Категория', anchor=CENTER)

    for i in range(0, 8):
        c = b[i].split(';')
        if c[1] == '23 года' or c[1] == '22 года':
            tv1.insert(parent='', index=i, text='', values=(c[0], c[1], c[2]))
    tv1.grid()


def ex_4_pz_3(entry1, window):
    a = entry1.get()
    b = len(a)
    label = Label(window, text=b, justify=RIGHT)
    label.grid(row=13, column=2, sticky=W)
    c = a.split(' ')
    n = len(c)
    label = Label(window, text=n, justify=RIGHT)
    label.grid(row=14, column=2, sticky=W)


def ex_1_pz_4(entry1, window):
    n = int(entry1.get())
    a = [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]

    tv = ttk.Treeview(window, columns=(), show="headings", height=n)
    tv["columns"] = tuple(range(n))
    for i in range(n):
        tv.heading(i, text="Столбец " + str(i + 1))
        tv.column(i, width=70, anchor=CENTER)
    for j in a:
        tv.insert("", "end", values=j, )
    tv.grid()


def ex_2_pz_4_func1(entry1, window):
    a = entry1.get().split(',')
    b = len(a)
    tv = ttk.Treeview(window, columns=(), show="headings")
    tv["columns"] = tuple(range(b))
    for i in range(b):
        tv.heading(i, text=a[i])
        tv.column(i, width=50, anchor=CENTER)
    tv.grid()


def ex_2_pz_4_func2(entry1, entry2, window):
    a = entry1.get().split(',')
    del a[3:7]
    a += entry2.get().split(',')
    b = len(a)
    tv = ttk.Treeview(window, columns=(), show="headings")
    tv["columns"] = tuple(range(b))
    for i in range(b):
        tv.heading(i, text=a[i])
        tv.column(i, width=50, anchor=CENTER)
    tv.grid()


def ex_3_pz_4(window):
    my_len = [['БО-331101', ['Акулова Алена', 'Бабушкина Ксения', 'Иванов Иван']],
              ['БОВ-421102', ['Сергеев Максим', 'Молчанова Ульяна', 'Быкова Елизавета']],
              [' БО-331103', ['Матвеев Эрик', 'Золотарева Амелия', 'Зайцева Вероника']]]
    a, b, c = my_len[0], my_len[1], my_len[2]
    tv = ttk.Treeview(window, height=4)
    tv['columns'] = ('grup1', 'grup2', 'grup3')
    tv.column('#0', width=0, stretch=NO)
    tv.column('grup1', anchor=CENTER, width=150)
    tv.column('grup2', anchor=CENTER, width=150)
    tv.column('grup3', anchor=CENTER, width=150)

    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('grup1', text=a[0], anchor=CENTER)
    tv.heading('grup2', text=b[0], anchor=CENTER)
    tv.heading('grup3', text=c[0], anchor=CENTER)

    for i in range(0, 3):
        tv.insert(parent='', index=i, text='', values=(a[1][i], b[1][i], c[1][i]))

    tv.grid()


def ex_4_pz_4_func1(window, my_len):
    a, b, n = my_len[0], my_len[1], my_len[2]
    tv = ttk.Treeview(window, height=4)

    tv['columns'] = ('grup1', 'grup2', 'grup3')
    tv.column('#0', width=0, stretch=NO)
    tv.column('grup1', anchor=CENTER, width=150)
    tv.column('grup2', anchor=CENTER, width=150)
    tv.column('grup3', anchor=CENTER, width=150)

    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('grup1', text=a[0], anchor=CENTER)
    tv.heading('grup2', text=b[0], anchor=CENTER)
    tv.heading('grup3', text=n[0], anchor=CENTER)

    for i in range(0, 3):
        tv.insert(parent='', index=i, text='', values=(a[1][i], b[1][i], n[1][i]))
    tv.grid()


def ex_4_pz_4_func2(window, my_len):
    a, b, n = my_len[0], my_len[1], my_len[2]
    tv1 = ttk.Treeview(window, height=4)
    tv1['columns'] = ('grup', 'fio')

    tv1.column('#0', width=0, stretch=NO)
    tv1.column('grup', anchor=CENTER, width=150)
    tv1.column('fio', anchor=CENTER, width=150)

    tv1.heading('#0', text='', anchor=CENTER)
    tv1.heading('grup', text='Группа', anchor=CENTER)
    tv1.heading('fio', text='Студенты', anchor=CENTER)

    for i in range(0, 3):
        c = a[1][i].split()
        if (c[0][0] == 'П') and (c[1][0] == 'А'):
            c = ' '.join(c)
            tv1.insert(parent='', index=i, text='', values=(a[0], c))

    for i in range(0, 3):
        c = b[1][i].split()
        if (c[0][0] == 'П') and (c[1][0] == 'А'):
            c = ' '.join(c)
            tv1.insert(parent='', index=i, text='', values=(a[0], c))

    for i in range(0, 3):
        c = n[1][i].split()
        if (c[0][0] == 'П') and (c[1][0] == 'А'):
            c = ' '.join(c)
            tv1.insert(parent='', index=i, text='', values=(a[0], c))
    tv1.grid()


def ex_1_pz_5(window):
    label = Label(text="")
    label.grid()
    directory = fd.askdirectory(title="Открыть папку", initialdir="/")
    label = Label(text="")
    label.grid()
    files = os.listdir(directory)
    label = Label(window, text=f'Выбранный путь: {directory}')
    label.grid()
    label = Label(text="")
    label.grid()
    label = Label(window, text=f'Количество файлов: {len(files)}')
    return label.grid()


def ex_3_pz_5_info(listbox):
    f = os.path.join(os.getcwd(), 'students.csv')
    with open(f, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        a = str(data)
        a = a.split(',')
        for row in a:
            b = str(row)
            b = b.replace('[', '').replace(']', '').replace(';', ' ').replace("'", '')
            listbox.insert(END, b)


def ex_3_pz_5_save_file(entry):
    f2 = fd.asksaveasfilename()
    if f2 != "":
        with open(f2, "a", newline='') as file:
            s = entry.get().split(';')
            writer = csv.writer(file, delimiter=';')
            writer.writerow(s)


def ex_3_pz_5_sorts(listbox2):
    st = []
    with open('students.csv', 'r') as file:
        next(file)
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            st.append(row)
    st.sort(key=lambda x: x[3])
    a = str(st)
    a = a.split('], [')
    for row in a:
        b = str(row)
        b = b.replace('[', '').replace(']', '').replace(',', ' ').replace("'", '')
        listbox2.insert(END, b)


def ex_3_pz_5_choic(listbox1, gr):
    listbox1.delete(0, END)
    selection = gr.get()
    st = []
    with open('students.csv', 'r') as file:
        next(file)
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            st.append(row)
    st2 = []
    for i in range(len(st)):
        if st[i][3] == selection:
            st2.append(st[i])
    for i in range(len(st2)):
        st2[i][2] = str(int(st2[i][2]) + 1)
    st3 = []
    for i in range(1, (len(st2))):
        if st2[i - 1][2] > st2[i][2]:
            st3.append(st2[i])
            st3.append(st2[i - 1])
        else:
            st3.append(st2[i - 1])
            st3.append(st2[i])
    a = str(st3)
    a = a.split('], [')
    for row in a:
        b = str(row)
        b = b.replace('[', '').replace(']', '').replace(',', ' ').replace("'", '')
        listbox1.insert(END, b)


def PZ_1_ex1():
    window = Tk()
    window.title("Работа 1. Задание 1.")
    window.geometry("520x400")
    bt2 = Button(window, text='Выход', command=lambda: exite(window))
    bt2.grid() #row=14, column=2, sticky=W
    label = Label(window, text="Напишите программу для решения примера. Предусмотрите проверку деления на ноль.", justify = CENTER)
    label.grid(columnspan=5)

    label = Label(window, text="Все необходимые переменные пользователь вводит через консоль.", justify = CENTER)
    label.grid(columnspan=5)

    label = Label(window, text="Вариант 3. |1 - a*b**c- a*(b**2-c**2) + (b-c+a)*(12+b)/(c-a)|", justify = CENTER)
    label.grid(columnspan=5)

    label = Label(window, justify=CENTER)
    label.grid(columnspan=5)

    label = Label(window, text='Введите а: ')
    label.grid(column=1, row=5, sticky=E)
    entry1 = Entry(window)
    entry1.grid(column=2, row=5, sticky=W)
    label = Label(window)
    label.grid(row=6)

    label = Label(window, text='Введите b: ')
    label.grid(column=1, row=7, sticky=E)
    entry2 = Entry(window)
    entry2.grid(column=2, row=7, sticky=W)
    label = Label(window)
    label.grid(row=8)

    label = Label(window, text='Введите c: ')
    label.grid(column=1, row=9, sticky=E)
    entry3 = Entry(window)
    entry3.grid(column=2, row=9, sticky=W)
    label = Label(window)
    label.grid(row=10)

    bt1 = Button(window, text='Ввести', command= lambda : ex_1_pz_1(entry1, entry2, entry3, window))
    bt1.grid(row=11, column=2, sticky=W)
    label = Label(window)
    label.grid(row=12)

    label = Label(window, text="Результат:")
    label.grid(row=13, column=1, sticky=E)


def PZ_1_ex2():
    window = Tk()
    window.title("Работа 1. Задание 2.")
    window.geometry("520x400")

    label = Label(window, text="Дан произвольный список, содержащий и строки и числа.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Выведите все четные элементы в одной строке.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text='Введите список: ')
    label.grid(column=1, row=5, sticky=E)
    entry1 = Entry(window, width= 40)
    entry1.grid(column=2, row=5, sticky=W)
    label = Label(window)
    label.grid(row=6)
    bt1 = Button(window, text='Ввести', command=lambda: ex_2_pz_1(entry1, window))
    bt1.grid(row=11, column=2, sticky=W)
    label = Label(window, text="Результат:")
    label.grid(row=13, column=1, sticky=E)
    bt2 = Button(window, text='Выход', command=lambda: exite(window))
    bt2.grid(row=14, column=2, sticky=W)


def PZ_1_ex3():
    window = Tk()
    window.title("Работа 1. Задание 3.")
    window.geometry("520x400")

    label = Label(window, text="Дан произвольный список, содержащий только числа.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Выведите результат умножения всех чисел меньше 10.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text='Введите список: ')
    label.grid(column=1, row=5, sticky=E)
    entry1 = Entry(window, width=40)
    entry1.grid(column=2, row=5, sticky=W)
    label = Label(window)
    label.grid(row=6)
    bt1 = Button(window, text='Ввести', command=lambda: ex_3_pz_1(entry1, window))
    bt1.grid(row=11, column=2, sticky=W)
    label = Label(window, text="Результат:")
    label.grid(row=13, column=1, sticky=E)
    bt2 = Button(window, text='Выход', command=lambda: exite(window))
    bt2.grid(row=14, column=2, sticky=W)


def PZ_1_ex4():
    window = Tk()
    window.title("Работа 1. Задание 4.")
    window.geometry("520x400")

    label = Label(window, text="Дан произвольный список, содержащий только числа.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Выведите среднее арифметическое.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text='Введите список: ')
    label.grid(column=1, row=5, sticky=E)
    entry1 = Entry(window, width=40)
    entry1.grid(column=2, row=5, sticky=W)
    label = Label(window)
    label.grid(row=6)
    bt1 = Button(window, text='Ввести', command=lambda: ex_4_pz_1(entry1, window))
    bt1.grid(row=11, column=2, sticky=W)
    label = Label(window, text="Результат:")
    label.grid(row=13, column=1, sticky=E)
    bt2 = Button(window, text='Выход', command=lambda: exite(window))
    bt2.grid(row=14, column=2, sticky=W)


def PZ_2_ex1():
    window = Tk()
    window.title("Работа 2. Задание 1.")
    window.geometry("520x400")

    label = Label(window, text="Пусть задано некоторое число my_number.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Пользователь вводит с клавиатуры свое число user_number.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Запрашивайте у пользователя вводить число user_number если оно равно my_number.",justify=CENTER)
    label.grid(columnspan=5)
    label1 = Label(window, text='Введите число: ')
    label1.grid(column=1, row=5, sticky=E)
    entry1 = Entry(window, width=40)
    entry1.grid(column=2, row=5, sticky=W)
    label = Label(window)
    label.grid(row=6)
    bt1 = Button(window, text='Ввести', command=lambda: ex_1_pz_2(entry1, window, label1))
    bt1.grid(row=11, column=2, sticky=W)
    label = Label(window, text="Результат:")
    label.grid(row=13, column=1, sticky=E)
    bt2 = Button(window, text='Выход', command=lambda: exite(window))
    bt2.grid(row=14, column=2, sticky=W)


def PZ_2_ex2():
    window = Tk()
    window.title("Работа 2. Задание 1.")
    window.geometry("520x400")

    label = Label(window, text="Пусть задан список, содержащий строки.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Выведите все строки, заканчивающиеся буковой r.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text='Введите список: ')
    label.grid(column=1, row=5, sticky=E)
    entry1 = Entry(window, width=40)
    entry1.grid(column=2, row=5, sticky=W)
    label = Label(window)
    label.grid(row=6)
    bt1 = Button(window, text='Ввести', command=lambda: ex_2_pz_2(entry1, window))
    bt1.grid(row=11, column=2, sticky=W)
    label = Label(window, text="Результат:")
    label.grid(row=13, column=1, sticky=E)
    bt2 = Button(window, text='Выход', command=lambda: exite(window))
    bt2.grid(row=14, column=2, sticky=W)


def PZ_2_ex3():
    window = Tk()
    window.title("Работа 2. Задание 3.")
    window.geometry("520x400")

    label = Label(window, text="Сгенерируйте и выведите cлучайную строку размером 6 символов,", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="содержащую только цифры. Строка должна содержать хотя бы одну цифру 3", justify=CENTER)
    label.grid(columnspan=5)
    bt1 = Button(window, text='Ввести', command=lambda: ex_3_pz_2(window))
    bt1.grid(row=11, column=2, sticky=W)
    label = Label(window, text="Результат:")
    label.grid(row=13, column=1, sticky=E)
    bt2 = Button(window, text='Выход', command=lambda: exite(window))
    bt2.grid(row=14, column=2, sticky=W)


def PZ_2_ex4():
    window = Tk()
    window.title("Работа 2. Задание 4.")
    window.geometry("520x400")

    label = Label(window, text="Пусть дана строка. На основе данной строки сформируйте новую, содержащую", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="только буквы Л.  Выведите новую строку.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text='Введите строку: ')
    label.grid(column=1, row=5, sticky=E)
    entry1 = Entry(window, width=40)
    entry1.grid(column=2, row=5, sticky=W)
    label = Label(window)
    label.grid(row=6)
    bt1 = Button(window, text='Ввести', command=lambda: ex_4_pz_2(entry1, window))
    bt1.grid(row=11, column=2, sticky=W)
    label = Label(window, text="Результат:")
    label.grid(row=13, column=1, sticky=E)
    bt2 = Button(window, text='Выход', command=lambda: exite(window))
    bt2.grid(row=14, column=2, sticky=W)


def PZ_3_ex1():
    window = Tk()
    window.title("Работа 3. Задание 1.")
    window.geometry("520x400")

    label = Label(window, text="Пусть дана строка, состоящая из слов, пробелов и знаков препинания.",justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="На основании этой строки создайте новую,", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="содержащую только слова размером от 5 до 10 символов, и выведите ее на консоль", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text='Введите строку: ')
    label.grid(column=1, row=5, sticky=E)
    entry1 = Entry(window, width=40)
    entry1.grid(column=2, row=5, sticky=W)
    label = Label(window)
    label.grid(row=6)
    bt1 = Button(window, text='Ввести', command=lambda: ex_1_pz_3(entry1, window))
    bt1.grid(row=11, column=2, sticky=W)
    label = Label(window, text="Результат:")
    label.grid(row=13, column=1, sticky=E)
    bt2 = Button(window, text='Выход', command=lambda: exite(window))
    bt2.grid(row=14, column=2, sticky=W)


def PZ_3_ex2():
    window = Tk()
    window.title("Работа 3. Задание 2.")
    window.geometry('650x525')

    label = Label(window, text="Пусть дана строковая переменная, содержащая информацию о студентах:", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="my_string = «Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="_Петров;Семен;Игоревич;22 года;Студент 2 курса». Вывести информацию в нужном виде.",justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window)
    label.grid(row=6)
    bt1 = Button(window, text='Ввести', command=lambda: ex_2_pz_3(window))
    bt1.grid(row=11, column=2, sticky=W)
    label = Label(window)
    label.grid(row=12)
    bt2 = Button(window, text='Выход', command=lambda: exite(window))
    bt2.grid(row=14, column=2, sticky=W)


def PZ_3_ex3():
    window = Tk()
    window.title("Работа 3. Задание 3.")
    window.geometry('650x525')
    label = Label(window, text="Пусть дана строковая переменная, содержащая информацию о студентах вида:", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="my_string = «ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;",justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="_Петров Всеволод Борисович;21 год;Студент 2 курса». Выведите построчно информацию о студентах, чей возраст больше «21 года».", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window)
    label.grid(row=6)
    bt1 = Button(window, text='Ввести', command=lambda: ex_3_pz_3_func1(window))
    bt1.grid(row=11, column=2, sticky=W)
    label = Label(window)
    label.grid(row=12)
    bt2 = Button(window, text='Выбрать', command=lambda: ex_3_pz_3_func2(window))
    bt2.grid(row=13, column=2, sticky=W)
    label = Label(window)
    label.grid(row=14)
    bt2 = Button(window, text='Выход', command=lambda: exite(window))
    bt2.grid(row=14, column=2, sticky=W)


def PZ_3_ex4():
    window = Tk()
    window.title("Работа 3. Задание 4.")
    window.geometry("520x400")

    label = Label(window, text="Пусть дана строка произвольной длины.",justify=CENTER)
    label.grid(columnspan=5)

    label = Label(window, text="Выведите информацию о том, сколько в ней символов и сколько слов", justify=CENTER)
    label.grid(columnspan=5)

    label = Label(window, justify=CENTER)
    label.grid(columnspan=5)

    label = Label(window, text='Введите строку: ')
    label.grid(column=1, row=5, sticky=E)
    entry1 = Entry(window)
    entry1.grid(column=2, row=5, sticky=W)
    label = Label(window)
    label.grid(row=6)

    bt1 = Button(window, text='Ввести', command=lambda: ex_4_pz_3(entry1, window))
    bt1.grid(row=11, column=2, sticky=W)
    label = Label(window)
    label.grid(row=12)

    label = Label(window, text="Результат:")
    label.grid(row=13, column=1, sticky=E)
    bt2 = Button(window, text='Выход', command=lambda: exite(window))
    bt2.grid(row=14, column=2, sticky=W)


def PZ_4_ex1():
    window = Tk()
    window.title("Работа 4. Задание 1.")
    window.geometry("520x400")

    label = Label(window, text="Пусть дана матрица чисел размером NхN. Представьте данную матрицу в виде списка.", justify=CENTER)
    label.grid(columnspan=5)

    label = Label(window, text="Выведите результат сложения всех элементов матрицы.", justify=CENTER)
    label.grid(columnspan=5)

    label = Label(window, justify=CENTER)
    label.grid(columnspan=5)

    label = Label(window, text='Введите N: ')
    label.grid(column=1, row=5, sticky=E)
    entry1 = Entry(window)
    entry1.grid(column=2, row=5, sticky=W)
    label = Label(window)
    label.grid(row=6)

    bt1 = Button(window, text='Вывести матрицу', command=lambda: ex_1_pz_4(entry1, window))
    bt1.grid(row=11, column=2, sticky=W)
    label = Label(window)
    label.grid(row=12)

    label = Label(window, text="Результат:")
    label.grid(row=13, column=1, sticky=E)
    bt2 = Button(window, text='Выход', command=lambda: exite(window))
    bt2.grid(row=14, column=2, sticky=W)


def PZ_4_ex2():
    window = Tk()
    window.title("Работа 4. Задание 2.")
    window.geometry("520x400")

    label = Label(window, text="Пусть дан список из 10 элементов. Удалите элементы с 4 по 8 и добавьте 2 новых.", justify=CENTER)
    label.grid(columnspan=5)

    label = Label(window, text='Введите элементы списка через запятую: ')
    label.grid(column=1, row=5, sticky=E)
    entry1 = Entry(window)
    entry1.grid(column=2, row=5, sticky=W)
    label = Label(window)
    label.grid(row=6)
    label = Label(window, text='Введите через запятую 2 элемента, которые нужно добавить в список: ')
    label.grid(column=1, row=5, sticky=E)
    entry2 = Entry(window)
    entry2.grid(column=2, row=6, sticky=W)
    label = Label(window)
    label.grid(row=7)
    bt1 = Button(window, text='Вывести изначальный список: ', command=lambda: ex_2_pz_4_func1(entry1, window))
    bt1.grid(row=12, column=2, sticky=W)
    label = Label(window)
    label.grid(row=13)
    bt2 = Button(window, text='Вывести полученный список: ', command=lambda: ex_2_pz_4_func2(entry1, entry2, window))
    bt2.grid(row=14, column=2, sticky=W)
    label = Label(window)
    label.grid(row=15)
    label = Label(window, text="Результат:")
    label.grid(row=16, column=1, sticky=E)
    bt3 = Button(window, text='Выход', command=lambda: exite(window))
    bt3.grid(row=17, column=2, sticky=W)


def PZ_4_ex3():
    window = Tk()
    window.title("Работа 4. Задание 3.")
    window.geometry("520x400")

    label = Label(window, text="Пусть журнал по предмету «Информационные технологии» представлен в виде списка:", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="my_len = [[‘БО-331101’,[‘Акулова Алена’, ‘Бабушкина Ксения’, …….]],", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="[‘ БОВ-421102’,[…..]],[‘ БО-331103’,[….]]]. Выведите списки всех групп построчно в виде:", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="<Название группы>\n<ФИО>\n<ФИО>", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, justify=CENTER)
    label.grid(columnspan=5)

    bt1 = Button(window, text='Ввести', command=lambda: ex_3_pz_4(window))
    bt1.grid(row=11, column=2, sticky=W)
    label = Label(window)
    label.grid(row=12)
    bt3 = Button(window, text='Выход', command=lambda: exite(window))
    bt3.grid(row=17, column=2, sticky=W)


def PZ_4_ex4():
    my_len = [['БО-331101', ['Прохорова Алена', 'Бабушкина Ксения', 'Иванов Иван']],
              ['БОВ-421102', ['Сергеев Максим', 'Пономарев Александр', 'Быкова Елизавета']],
              [' БО-331103', ['Матвеев Эрик', 'Зайцева Вероника', 'Попова Амелия']]]

    window = Tk()
    window.title("Работа 4. Задание 4.")
    window.geometry("520x400")

    label = Label(window, text="Пусть журнал по предмету «Информационные технологии» представлен в виде списка:", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="my_len = [[‘БО-331101’,[‘Акулова Алена’, ‘Бабушкина Ксения’, …….]],[‘ БОВ-421102’,[…..]],[‘ БО-331103’,[….]]].", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Выведите всех студентов (и их группы), чья фамилия начинается на букву «П», а имя на букву «А»", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, justify=CENTER)
    label.grid(columnspan=5)

    bt1 = Button(window, text='Ввести изначальный список', command=lambda: ex_4_pz_4_func1(window, my_len))
    bt1.grid(row=11, column=2, sticky=W)
    label = Label(window)
    label.grid(row=12)
    bt1 = Button(window, text='Выбрать', command=lambda: ex_4_pz_4_func2(window, my_len))
    bt1.grid(row=13, column=2, sticky=W)
    bt3 = Button(window, text='Выход', command=lambda: exite(window))
    bt3.grid(row=17, column=2, sticky=W)


def PZ_5_ex1():
    window = Tk()
    window.title("Работа 5. Задание 1")
    window.geometry("350x350")

    label = Label(window, text="Пусть дана некоторая директория (папка). ")
    label.grid()
    label = Label(window, text="Посчитайте количество файлов в данной ")
    label.grid()
    label = Label(window, text="директории (папке) и выведите на экран. ")
    label.grid()
    label = Label(window, text="")
    label.grid()

    btn = Button(window, text="Выбрать путь", command=lambda: ex_1_pz_5(window))
    btn.grid()
    bt3 = Button(window, text='Выход', command=lambda: exite(window))
    bt3.grid(row=17, column=2, sticky=W)


def PZ_5_ex2():
    window = Tk()
    window.geometry('420x460')

    label = Label(window, text="Пусть дан список. Считайте информацию из файла.")
    label.grid()
    label = Label(window, text="Выведите информацию о студентах, отсортировав их по номеру группы.")
    label.grid()
    label = Label(window, text="")
    label.grid()
    button = Button(window, text="Вывести информацию из файла", command=lambda: ex_3_pz_5_info(listbox))
    button.grid()
    label = Label(window, text="")
    label.grid()
    button1 = Button(window, text="Сортировать", command=lambda: ex_3_pz_5_sorts(listbox1))
    button1.grid()
    result_label = Label(window, text="")
    result_label.grid()
    result_label = Label(window, text="Несортированный список:")
    result_label.grid()
    listbox = Listbox(window, width=55, height=7)
    listbox.grid()
    label = Label(window, text="")
    label.grid()
    result_label = Label(window, text="Сортированный список:")
    result_label.grid()
    listbox1 = Listbox(window, width=55, height=6)
    listbox1.grid()
    bt3 = Button(window, text='Выход', command=lambda: exite(window))
    bt3.grid(row=17, column=2, sticky=W)


def PZ_5_ex3():
    window = Tk()
    window.geometry('650x525')
    label = Label(window, text="Пусть дан список. Считайте информацию из файла.")
    label.grid(columnspan=3)
    label = Label(window, text="Задание 2. Выведите информацию о студентах, отсортировав их по номеру группы.")
    label.grid(columnspan=3)
    label = Label(window, text="Задание 3. Упорядочить по увеличению возраста студентов в заданной пользователем группе на 1")
    label.grid(columnspan=3)
    label = Label(window, text="")
    label.grid()
    label = Label(window, text="Задание 2")
    label.grid(column=0, pady=3)
    label = Label(window)
    label.grid(column=0)
    button = Button(window, text="Вывести информацию из файла", command=lambda: ex_3_pz_5_info(listbox))
    button.grid(column=0)
    label = Label(window, text='Несортированный список:')
    label.grid(column=0, padx=(20, 20), pady=(10, 0))
    listbox = Listbox(window, width=47, height=7)
    listbox.grid(padx=(7, 0))
    label = Label(window, text='Отсортированный список:')
    label.grid(column=0, padx=(20, 20), pady=(10, 0))
    listbox2 = Listbox(window, width=47, height=6)
    listbox2.grid()
    button2 = Button(window, text="Отсортировать", command=lambda: ex_3_pz_5_sorts(listbox2))
    button2.grid()
    label = Label(window, text="Задание 3")
    label.grid(column=2, pady=(0, 10), row=4)
    Label(window, text='Выберите группу: ').grid(column=2, row=5, sticky=W)
    gr = ttk.Combobox(window, width=27, state="readonly")
    gr['values'] = ('БО-333333', 'БО-222222', 'БО-111111')
    gr.grid(column=2, row=5, sticky=E)
    button1 = Button(window, text="Выбрать", command=lambda: ex_3_pz_5_choic(listbox1, gr))
    button1.grid(column=2, row=6, pady=(20, 0))
    listbox1 = Listbox(window, width=47, height=7)
    listbox1.grid(column=2, row=8, padx=10)
    bt3 = Button(window, text='Выход', command=lambda: exite(window))
    bt3.grid(row=17, column=2, sticky=W)


def PZ_5_ex4():
    window = Tk()
    window.geometry('950x535')

    label = Label(window, text="Пусть дан список. Считайте информацию из файла.")
    label.grid(columnspan=4)
    label = Label(window, text="Задание 2. Выведите информацию о студентах, отсортировав их по номеру группы.")
    label.grid(columnspan=4)
    label = Label(window, text="Задание 3. Упорядочить по увеличению возраста студентов в заданной пользователем группе на 1")
    label.grid(columnspan=4)
    label = Label(window, text="Задание 4. Добавьте возможность сохранения новых данных обратно в файл")
    label.grid(columnspan=4)
    label = Label(window, text="")
    label.grid()
    label = Label(window, text="Задание 2")
    label.grid(column=0, pady=(0, 10), row=5)
    label = Label(window)
    label.grid(column=0)
    listbox = Listbox(window, width=47, height=7)
    button = Button(window, text="Вывести информацию из файла", command=lambda: ex_3_pz_5_info(listbox))
    button.grid(column=0)
    label = Label(window, text='Несортированный список:')
    label.grid(column=0, padx=(20, 20), pady=(10, 0))
    listbox.grid(padx=(7, 0))
    label = Label(window, text='Отсортированный список:')
    label.grid(column=0, padx=(20, 20), pady=(10, 0))
    listbox2 = Listbox(window, width=47, height=6)
    listbox2.grid()
    button2 = Button(window, text="Отсортировать", command=lambda: ex_3_pz_5_sorts(listbox2))
    button2.grid(padx=(20, 20), pady=(10, 0))
    label = Label(window, text="Задание 3")
    label.grid(column=2, pady=(0, 10), row=5)
    Label(window, text='Выберите группу: ').grid(column=2, row=6, sticky=W)
    gr = ttk.Combobox(window, width=27, state="readonly")
    gr['values'] = ('БО-333333', 'БО-222222', 'БО-111111')
    gr.grid(column=2, row=6, sticky=E)
    listbox1 = Listbox(window, width=47, height=7)
    button1 = Button(window, text="Выбрать", command=lambda: ex_3_pz_5_choic(listbox1, gr))
    button1.grid(column=2, row=7, pady=(20, 0))
    listbox1.grid(column=2, row=9, padx=10)
    label = Label(window, text="Задание 4")
    label.grid(column=3, pady=(0, 10), row=5, padx=(20, 0))
    entry = Entry(window, width=50)
    entry.grid(column=3, row=6, padx=(20, 0))
    button3 = Button(window, text="Сохранить", command=lambda: ex_3_pz_5_save_file(entry))
    button3.grid(column=3, row=7, pady=(20, 0), padx=(20, 0))
    bt3 = Button(window, text='Выход', command=lambda: exite(window))
    bt3.grid(row=17, column=2, sticky=W)

root = Tk()

menu = Menu(root)
menu.add_cascade(label='Выход', command=lambda: exite(root))
PZ1menu = Menu(menu, tearoff=0)
PZ1menu.add_command(label="Задание 1", command=PZ_1_ex1)
PZ1menu.add_command(label="Задание 2", command=PZ_1_ex2)
PZ1menu.add_command(label="Задание 3", command=PZ_1_ex3)
PZ1menu.add_command(label="Задание 4", command=PZ_1_ex4)

PZ2menu = Menu(menu, tearoff=0)
PZ2menu.add_command(label="Задание 1", command=PZ_2_ex1)
PZ2menu.add_command(label="Задание 2", command=PZ_2_ex2)
PZ2menu.add_command(label="Задание 3", command=PZ_2_ex3)
PZ2menu.add_command(label="Задание 4", command=PZ_2_ex4)

PZ3menu = Menu(menu, tearoff=0)
PZ3menu.add_command(label="Задание 1", command=PZ_3_ex1)
PZ3menu.add_command(label="Задание 2", command=PZ_3_ex2)
PZ3menu.add_command(label="Задание 3", command=PZ_3_ex3)
PZ3menu.add_command(label="Задание 4", command=PZ_3_ex4)

PZ4menu = Menu(menu, tearoff=0)
PZ4menu.add_command(label="Задание 1", command=PZ_4_ex1)
PZ4menu.add_command(label="Задание 2", command=PZ_4_ex2)
PZ4menu.add_command(label="Задание 3", command=PZ_4_ex3)
PZ4menu.add_command(label="Задание 4", command=PZ_4_ex4)

PZ5menu = Menu(menu, tearoff=0)
PZ5menu.add_command(label="Задание 1", command=PZ_5_ex1)
PZ5menu.add_command(label="Задание 2", command=PZ_5_ex2)
PZ5menu.add_command(label="Задание 3", command=PZ_5_ex3)
PZ5menu.add_command(label="Задание 4", command=PZ_5_ex4)

menu.add_cascade(label="Работа 1", menu=PZ1menu)
menu.add_cascade(label="Работа 2", menu=PZ2menu)
menu.add_cascade(label="Работа 3", menu=PZ3menu)
menu.add_cascade(label="Работа 4", menu=PZ4menu)
menu.add_cascade(label="Работа 5", menu=PZ5menu)

root.config(menu=menu, width=375, height=200)
label5 = Label(root, text='Выберите номер работы и задание', justify=CENTER, width=55, height=10, font=('arial bold', 12))
label5.grid()

root.mainloop()
