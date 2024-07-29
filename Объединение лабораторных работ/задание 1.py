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
from idlelib.tooltip import Hovertip


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
    label.grid(row=14, column=2, sticky=W)


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
    label.grid(row=15, column=2, sticky=W)


def ex_4_pz_1(entry1, window):
    a = np.array((entry1.get().split()))
    k = 0
    c = 0
    for i in a:
        k += int(i)
        c += 1
    sr = k/c
    label = Label(window, text=sr, justify=RIGHT)
    label.grid(row=15, column=2, sticky=W)


def ex_1_pz_2(entry1, window, label1):
    my_number = 10
    a = 10
    while a == my_number:
        label1['text'] = 'Введите число еще раз'
        user_number = entry1.get()
        a = user_number
        if int(a) != my_number:
            label = Label(window, text=f'Загаданное число было {my_number}', justify=RIGHT)
            label.grid(row=15, column=2, sticky=W)
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
    label = Label(window, text='Изначальный список')
    label.grid(row=13, columnspan=5)
    tv.grid(row=14, columnspan=5)
    label = Label(window)
    label.grid(row=15)
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
    label = Label(window, text='Полученный список')
    label.grid(row=16, columnspan=5)
    tv1.grid(row=17, columnspan=5)


def ex_3_pz_2(window):
    result = [choice('012456789') for _ in range(5)]
    result.insert(randint(0, 5), '3')
    a = ''.join(result)
    label = Label(window, text=a, justify=RIGHT)
    label.grid(row=8, column=2, sticky=W)


def ex_4_pz_2(entry1, window):
    a = entry1.get().upper()
    b = ''
    for i in a:
        if i == 'Л':
            b += i
    label = Label(window, text=b, justify=RIGHT)
    label.grid(row=11, column=2, sticky=W)


def ex_1_pz_3(entry1, window):
    a = entry1.get().translate(str.maketrans('', '', punctuation)).split(' ')
    b = ''
    for i in a:
        if (len(i) > 4) and (len(i) < 10):
            b += i
            b += ' '
    c = b.rstrip()
    label = Label(window, text=c, justify=RIGHT)
    label.grid(row=11, column=2)


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

    tv.grid(row=9, columnspan=5)


def ex_3_pz_3_func1(window):
    tv = ttk.Treeview(window, height=8)
    v = '''ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;21 год;Студент 2 курса'''
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
    tv.grid(row=16, columnspan=5)


def ex_3_pz_3_func2(window):
    v = '''ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;21 год;Студент 2 курса'''
    a = v.split(';_')
    b = a[1:]
    tv1 = ttk.Treeview(window, height=5)
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
    tv1.grid(row=28, columnspan=5)


def ex_4_pz_3(entry1, window):
    a = entry1.get()
    b = len(a)
    label = Label(window, text=b, justify=RIGHT)
    label.grid(row=10, column=2, sticky=W)
    c = a.split(' ')
    n = len(c)
    label = Label(window, text=n, justify=RIGHT)
    label.grid(row=11, column=2, sticky=W)


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
    tv.grid(row=15, columnspan=5)


def ex_2_pz_4_func1(entry1, window):
    a = entry1.get().split(',')
    b = len(a)
    tv = ttk.Treeview(window, columns=(), show="headings", height=0)
    tv["columns"] = tuple(range(b))
    for i in range(b):
        tv.heading(i, text=a[i])
        tv.column(i, width=50, anchor=CENTER)
    tv.grid(row=11, columnspan=5)
    label = Label(window)
    label.grid(row=12)


def ex_2_pz_4_func2(entry1, entry2, window):
    a = entry1.get().split(',')
    del a[3:7]
    a += entry2.get().split(',')
    b = len(a)
    tv = ttk.Treeview(window, columns=(), show="headings", height=0)
    tv["columns"] = tuple(range(b))
    for i in range(b):
        tv.heading(i, text=a[i])
        tv.column(i, width=50, anchor=CENTER)
    tv.grid(row=15, columnspan=5)


def ex_3_pz_4(window):
    my_len = [['БО-331101', ['Акулова Алена', 'Бабушкина Ксения', 'Иванов Иван']],
              ['БОВ-421102', ['Сергеев Максим', 'Молчанова Ульяна', 'Быкова Елизавета']],
              [' БО-331103', ['Матвеев Эрик', 'Золотарева Амелия', 'Зайцева Вероника']]]
    a, b, c = my_len[0], my_len[1], my_len[2]
    tv = ttk.Treeview(window, height=4)
    tv['columns'] = ('группа1', 'группа2', 'группа3')
    tv.column('#0', width=0, stretch=NO)
    tv.column('группа1', anchor=CENTER, width=150)
    tv.column('группа2', anchor=CENTER, width=150)
    tv.column('группа3', anchor=CENTER, width=150)
    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('группа1', text=a[0], anchor=CENTER)
    tv.heading('группа2', text=b[0], anchor=CENTER)
    tv.heading('группа3', text=c[0], anchor=CENTER)
    for i in range(0, 3):
        tv.insert(parent='', index=i, text='', values=(a[1][i], b[1][i], c[1][i]))
    tv.grid(row=12, columnspan=5)


def ex_4_pz_4_func1(window, my_len):
    a, b, n = my_len[0], my_len[1], my_len[2]
    tv = ttk.Treeview(window, height=4)
    tv['columns'] = ('группа1', 'группа2', 'группа3')
    tv.column('#0', width=0, stretch=NO)
    tv.column('группа1', anchor=CENTER, width=150)
    tv.column('группа2', anchor=CENTER, width=150)
    tv.column('группа3', anchor=CENTER, width=150)
    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('группа1', text=a[0], anchor=CENTER)
    tv.heading('группа2', text=b[0], anchor=CENTER)
    tv.heading('группа3', text=n[0], anchor=CENTER)
    for i in range(0, 3):
        tv.insert(parent='', index=i, text='', values=(a[1][i], b[1][i], n[1][i]))
    tv.grid(row=9, columnspan=5)
    label = Label(window)
    label.grid(row=14)


def ex_4_pz_4_func2(window, my_len):
    a, b, n = my_len[0], my_len[1], my_len[2]
    tv1 = ttk.Treeview(window, height=4)
    tv1['columns'] = ('группа', 'фио')
    tv1.column('#0', width=0, stretch=NO)
    tv1.column('группа', anchor=CENTER, width=150)
    tv1.column('фио', anchor=CENTER, width=150)
    tv1.heading('#0', text='', anchor=CENTER)
    tv1.heading('группа', text='Группа', anchor=CENTER)
    tv1.heading('фио', text='Студенты', anchor=CENTER)
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
    tv1.grid(row=17, columnspan=5)


def ex_1_pz_5(window):
    label = Label(window, text='')
    label.grid()
    directory = fd.askdirectory(title="Открыть папку", initialdir="/")
    label = Label(window)
    label.grid(row=8)
    files = os.listdir(directory)
    label = Label(window, text=f'Выбранный путь: {directory}')
    label.grid(row=9, columnspan=2, ipadx=50)
    label = Label(window)
    label.grid(row=10)
    label = Label(window, text=f'Количество файлов: {len(files)}')
    return label.grid(row=11, columnspan=2, ipadx=50)


def ex_3_pz_5_info(window):
    r = os.path.join(os.getcwd(), 'students.csv')
    with open(r, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        a = str(data)
        a = a.split(',')
        c = []
        n = len(a)
        for i in range(0, n):
            b = a[i]
            b = b.replace('[', '').replace(']', '').replace("'", '')
            c.append(b)
    f = []
    n = len(c)
    for i in range(0, n):
        f.append(c[i].split(';'))
    f = f[1:]
    n = len(f)
    tv = ttk.Treeview(window, height=7)
    tv['columns'] = ('номер', 'фио', 'возраст', 'группа')
    tv.column('#0', width=0, stretch=NO)
    tv.column('номер', anchor=CENTER, width=50)
    tv.column('фио', anchor=CENTER, width=200)
    tv.column('возраст', anchor=CENTER, width=50)
    tv.column('группа', anchor=CENTER, width=100)
    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('номер', text='номер', anchor=CENTER)
    tv.heading('фио', text='фио', anchor=CENTER)
    tv.heading('возраст', text='возраст', anchor=CENTER)
    tv.heading('группа', text='группа', anchor=CENTER)
    for i in range(0, n):
        tv.insert(parent='', index=i, text='', values=(f[i][0], f[i][1], f[i][2], f[i][3]))
    tv.grid(row=9, columnspan=2, sticky=W, padx=10, rowspan=7)
    label = Label(window, text="")
    label.grid(row=10, sticky=W, columnspan=2)


def ex_3_pz_5_save_file(entry, entry_1, entry_2, entry_3):
    f2 = fd.asksaveasfilename()
    if f2 != "":
        with open(f2, "a", newline='') as file:
            s = []
            s.extend([entry.get(), entry_1.get(), entry_2.get(), entry_3.get()])
            writer = csv.writer(file, delimiter=';')
            writer.writerow(s)


def ex_3_pz_5_sorts(window):
    st = []
    with open('students.csv', 'r') as file:
        next(file)
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            st.append(row)
    st.sort(key=lambda x: x[3])
    a = st
    n = len(a)
    tv1 = ttk.Treeview(window, height=7)
    tv1['columns'] = ('номер', 'фио', 'возраст', 'группа')
    tv1.column('#0', width=0, stretch=NO)
    tv1.column('номер', anchor=CENTER, width=50)
    tv1.column('фио', anchor=CENTER, width=200)
    tv1.column('возраст', anchor=CENTER, width=50)
    tv1.column('группа', anchor=CENTER, width=100)

    tv1.heading('#0', text='', anchor=CENTER)
    tv1.heading('номер', text='номер', anchor=CENTER)
    tv1.heading('фио', text='фио', anchor=CENTER)
    tv1.heading('возраст', text='возраст', anchor=CENTER)
    tv1.heading('группа', text='группа', anchor=CENTER)

    for i in range(0, n):
        tv1.insert(parent='', index=i, text='', values=(a[i][0], a[i][1], a[i][2], a[i][3]))
    tv1.grid(row=25, columnspan=2, padx=10)


def ex_3_pz_5_choc(window, gr):
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
    a = st3
    n = len(a)
    tv1 = ttk.Treeview(window, height=n)
    tv1['columns'] = ('номер', 'фио', 'возраст', 'группа')
    tv1.column('#0', width=0, stretch=NO)
    tv1.column('номер', anchor=CENTER, width=50)
    tv1.column('фио', anchor=CENTER, width=200)
    tv1.column('возраст', anchor=CENTER, width=50)
    tv1.column('группа', anchor=CENTER, width=100)

    tv1.heading('#0', text='', anchor=CENTER)
    tv1.heading('номер', text='номер', anchor=CENTER)
    tv1.heading('фио', text='фио', anchor=CENTER)
    tv1.heading('возраст', text='возраст', anchor=CENTER)
    tv1.heading('группа', text='группа', anchor=CENTER)

    for i in range(0, n):
        tv1.insert(parent='', index=i, text='', values=(a[i][0], a[i][1], a[i][2], a[i][3]))
    tv1.grid(row=10, columnspan=2, column=4, rowspan=4)


def pz_1_ex1():
    window = Tk()
    window.title("Работа 1. Задание 1.")
    window.geometry("520x400")
    bt2 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt2.grid(columnspan=2, sticky=W)
    label = Label(window, text="Напишите программу для решения примера. Предусмотрите проверку деления на ноль.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Все необходимые переменные пользователь вводит через консоль.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Вариант 3. |1 - a*b**c- a*(b**2-c**2) + (b-c+a)*(12+b)/(c-a)|", justify=CENTER)
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
    bt1 = Button(window, text='Ввести', command=lambda: ex_1_pz_1(entry1, entry2, entry3, window))
    bt1.grid(row=11, column=1, sticky=E)
    label = Label(window)
    label.grid(row=12)
    label = Label(window, text="Результат:")
    label.grid(row=13, column=1, sticky=E)


def pz_1_ex2():
    window = Tk()
    window.title("Работа 1. Задание 2.")
    window.geometry("400x300")
    bt2 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt2.grid(columnspan=2)
    label = Label(window)
    label.grid(row=2)
    label = Label(window, text="Дан произвольный список, содержащий и строки и числа.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Выведите все четные элементы в одной строке.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window)
    label.grid(row=5)
    label = Label(window, text='Введите список: ')
    label.grid(column=1, row=6, sticky=E)
    entry1 = Entry(window, width=40)
    entry1.grid(column=2, row=6, sticky=W)
    label = Label(window)
    label.grid(row=7)
    bt1 = Button(window, text='Ввести', command=lambda: ex_2_pz_1(entry1, window))
    bt1.grid(row=12, column=2, sticky=W)
    label = Label(window)
    label.grid(row=13)
    label = Label(window, text="Все четные элементы:")
    label.grid(row=14, column=1, sticky=E)


def pz_1_ex3():
    window = Tk()
    window.title("Работа 1. Задание 3.")
    window.geometry("400x300")
    bt2 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt2.grid(columnspan=2)
    label = Label(window, text='')
    label.grid(row=2)
    label = Label(window, text="Дан произвольный список, содержащий только числа.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Выведите результат умножения всех чисел меньше 10.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text='')
    label.grid(row=6)
    label = Label(window, text='Введите список: ')
    label.grid(column=1, row=7, sticky=E)
    entry1 = Entry(window, width=40)
    entry1.grid(column=2, row=7, sticky=W)
    label = Label(window)
    label.grid(row=8)
    bt1 = Button(window, text='Ввести', command=lambda: ex_3_pz_1(entry1, window))
    bt1.grid(row=13, column=2, sticky=W)
    label = Label(window, text='')
    label.grid(row=14)
    label = Label(window, text="Результат умножения:")
    label.grid(row=15, column=1, sticky=E)


def pz_1_ex4():
    window = Tk()
    window.title("Работа 1. Задание 4.")
    window.geometry("450x300")
    bt2 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt2.grid(columnspan=2, sticky=W)
    label = Label(window, text='')
    label.grid(row=2)
    label = Label(window, text="Дан произвольный список, содержащий только числа.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Выведите среднее арифметическое.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window)
    label.grid(row=5)
    label = Label(window, text='Введите список: ')
    label.grid(column=1, row=7, sticky=E)
    entry1 = Entry(window, width=40)
    entry1.grid(column=2, row=7, sticky=W)
    label = Label(window)
    label.grid(row=8)
    bt1 = Button(window, text='Ввести', command=lambda: ex_4_pz_1(entry1, window))
    bt1.grid(row=13, column=2, sticky=W)
    label = Label(window)
    label.grid(row=14)
    label = Label(window, text="Среднее арифметическое:")
    label.grid(row=15, column=1, sticky=E)


def pz_2_ex1():
    window = Tk()
    window.title("Работа 2. Задание 1.")
    window.geometry("520x400")
    bt2 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt2.grid(columnspan=2, sticky=W)
    label = Label(window)
    label.grid(row=2)
    label = Label(window, text="Пусть задано некоторое число my_number.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Пользователь вводит с клавиатуры свое число user_number.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Запрашивайте у пользователя вводить число user_number если оно равно my_number.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window)
    label.grid(row=6)
    label1 = Label(window, text='Введите число: ')
    label1.grid(column=1, row=7, sticky=E)
    entry1 = Entry(window, width=40)
    entry1.grid(column=2, row=7, sticky=W)
    label = Label(window)
    label.grid(row=8)
    bt1 = Button(window, text='Ввести', command=lambda: ex_1_pz_2(entry1, window, label1))
    bt1.grid(row=13, column=2, sticky=W)
    label = Label(window)
    label.grid(row=14)
    label = Label(window, text="Какое загаданное число?")
    label.grid(row=15, column=1, sticky=E)


def pz_2_ex2():
    window = Tk()
    window.title("Работа 2. Задание 2.")
    window.geometry("425x350")
    bt2 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt2.grid(columnspan=2, sticky=W)
    label = Label(window)
    label.grid(row=2)
    label = Label(window, text="Пусть задан список, содержащий строки.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Выведите все строки, заканчивающиеся буковой r.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window)
    label.grid(row=5)
    label = Label(window, text='Введите список: ')
    label.grid(column=1, row=6, sticky=E)
    entry1 = Entry(window, width=40)
    entry1.grid(column=2, row=6, sticky=W)
    label = Label(window)
    label.grid(row=7)
    bt1 = Button(window, text='Ввести', command=lambda: ex_2_pz_2(entry1, window))
    bt1.grid(row=11, column=2, sticky=W)
    label = Label(window)
    label.grid(row=12)


def pz_2_ex3():
    window = Tk()
    window.title("Работа 2. Задание 3.")
    window.geometry("450x250")
    bt2 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt2.grid(columnspan=2, sticky=W)
    label = Label(window)
    label.grid(row=2)
    label = Label(window, text="Сгенерируйте и выведите cлучайную строку размером 6 символов,", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="содержащую только цифры. Строка должна содержать хотя бы одну цифру 3", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window)
    label.grid(row=5)
    bt1 = Button(window, text='Ввести', command=lambda: ex_3_pz_2(window))
    bt1.grid(row=6, columnspan=5)
    label = Label(window)
    label.grid(row=7)
    label = Label(window, text="Сгенерированная строка:")
    label.grid(row=8, column=1, sticky=E)


def pz_2_ex4():
    window = Tk()
    window.title("Работа 2. Задание 4.")
    window.geometry("470x250")
    bt2 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt2.grid(columnspan=2, sticky=W)
    label = Label(window)
    label.grid(row=2)
    label = Label(window, text="Пусть дана строка. На основе данной строки сформируйте новую, содержащую", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="только буквы Л.  Выведите новую строку.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window)
    label.grid(row=6)
    label = Label(window, text='Введите строку: ')
    label.grid(column=1, row=7, sticky=E)
    entry1 = Entry(window, width=40)
    entry1.grid(column=2, row=7, sticky=W)
    label = Label(window)
    label.grid(row=8)
    bt1 = Button(window, text='Ввести', command=lambda: ex_4_pz_2(entry1, window))
    bt1.grid(row=9, column=2, sticky=W)
    label = Label(window)
    label.grid(row=10)
    label = Label(window, text="Полученная строка:")
    label.grid(row=11, column=1, sticky=E)


def pz_3_ex1():
    window = Tk()
    window.title("Работа 3. Задание 1.")
    window.geometry("520x300")
    bt2 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt2.grid(columnspan=2, sticky=W)
    label = Label(window)
    label.grid(row=2)
    label = Label(window, text="Пусть дана строка, состоящая из слов, пробелов и знаков препинания.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="На основании этой строки создайте новую,", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="содержащую только слова размером от 5 до 10 символов, и выведите ее на консоль", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window)
    label.grid(row=6)
    label = Label(window, text='Введите строку: ')
    label.grid(column=1, row=7, sticky=E)
    entry1 = Entry(window, width=40)
    entry1.grid(column=2, row=7, sticky=W)
    label = Label(window)
    label.grid(row=8)
    bt1 = Button(window, text='Вывести', command=lambda: ex_1_pz_3(entry1, window))
    bt1.grid(row=9, column=2, sticky=W)
    label = Label(window)
    label.grid(row=10)
    label = Label(window, text="Новая строка:")
    label.grid(row=11, column=1, sticky=E)


def pz_3_ex2():
    window = Tk()
    window.title("Работа 3. Задание 2.")
    window.geometry('520x300')
    bt2 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt2.grid(columnspan=2, sticky=W)
    label = Label(window)
    label.grid(row=2)
    label = Label(window, text="Пусть дана строковая переменная, содержащая информацию о студентах:", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="my_string = «Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="_Петров;Семен;Игоревич;22 года;Студент 2 курса». Вывести информацию в нужном виде.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window)
    label.grid(row=6)
    bt1 = Button(window, text='Ввести', command=lambda: ex_2_pz_3(window))
    bt1.grid(row=7, columnspan=5)
    label = Label(window)
    label.grid(row=8)


def pz_3_ex3():
    window = Tk()
    window.title("Работа 3. Задание 3.")
    window.geometry('750x650')
    bt3 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt3.grid(columnspan=2, sticky=W)
    label = Label(window)
    label.grid(row=2)
    label = Label(window, text="Пусть дана строковая переменная, содержащая информацию о студентах вида:", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="my_string = «ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, justify=CENTER, text="_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;")
    label.grid(columnspan=5)
    label = Label(window, text="_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="_Петров Всеволод Борисович;21 год;Студент 2 курса». Выведите построчно информацию о студентах, чей возраст больше «21 года».", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window)
    label.grid(row=9)
    bt1 = Button(window, text='Ввести изначальный список', command=lambda: ex_3_pz_3_func1(window))
    bt1.grid(row=10, column=2)
    label = Label(window)
    label.grid(row=11)
    label = Label(window)
    label.grid(row=25)
    bt2 = Button(window, text='Выбрать студентов', command=lambda: ex_3_pz_3_func2(window))
    bt2.grid(row=26, column=2)
    label = Label(window)
    label.grid(row=27)


def pz_3_ex4():
    window = Tk()
    window.title("Работа 3. Задание 4.")
    window.geometry("410x270")
    bt3 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt3.grid(columnspan=2, sticky=W)
    label = Label(window)
    label.grid(row=2)
    label = Label(window, text="Пусть дана строка произвольной длины.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Выведите информацию о том, сколько в ней символов и сколько слов", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window)
    label.grid(row=5)
    label = Label(window, text='Введите строку: ')
    label.grid(column=1, row=6, sticky=E)
    entry1 = Entry(window)
    entry1.grid(column=2, row=6, sticky=W)
    label = Label(window)
    label.grid(row=7)
    bt1 = Button(window, text='Вывести информацию', command=lambda: ex_4_pz_3(entry1, window))
    bt1.grid(row=8, columnspan=5)
    label = Label(window)
    label.grid(row=9)
    label = Label(window, text="Количество символов:")
    label.grid(row=10, column=1, sticky=E)
    label = Label(window, text="Количество слов:")
    label.grid(row=11, column=1, sticky=E)


def pz_4_ex1():
    window = Tk()
    window.title("Работа 4. Задание 1.")
    window.geometry("500x400")
    bt3 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt3.grid(columnspan=2, sticky=W)
    label = Label(window)
    label.grid(row=2)
    label = Label(window, text="Пусть дана матрица чисел размером NхN. Представьте данную матрицу в виде списка.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Выведите результат сложения всех элементов матрицы.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text='Введите N: ')
    label.grid(column=1, row=6, sticky=E)
    entry1 = Entry(window)
    entry1.grid(column=2, row=6, sticky=W)
    label = Label(window)
    label.grid(row=7)
    bt1 = Button(window, text='Вывести матрицу', command=lambda: ex_1_pz_4(entry1, window))
    bt1.grid(row=12, column=2, sticky=W)
    label = Label(window)
    label.grid(row=13)


def pz_4_ex2():
    window = Tk()
    window.title("Работа 4. Задание 2.")
    window.geometry("550x370")
    bt3 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt3.grid(columnspan=2, sticky=W)
    label = Label(window)
    label.grid(row=2)
    label = Label(window, text="Пусть дан список из 10 элементов. Удалите элементы с 4 по 8 и добавьте 2 новых.", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window)
    label.grid(row=4)
    label = Label(window, text='Введите элементы списка через запятую: ')
    label.grid(column=1, row=5, sticky=E)
    entry1 = Entry(window)
    entry1.grid(column=2, row=5, sticky=W)
    label = Label(window)
    label.grid(row=6)
    label = Label(window, text='Введите через запятую 2 элемента, которые нужно добавить в список: ')
    label.grid(column=1, row=7, sticky=E)
    entry2 = Entry(window)
    entry2.grid(column=2, row=7, sticky=W)
    label = Label(window)
    label.grid(row=8)
    bt1 = Button(window, text='Вывести изначальный список: ', command=lambda: ex_2_pz_4_func1(entry1, window))
    bt1.grid(row=9, columnspan=5)
    label = Label(window)
    label.grid(row=10)
    bt2 = Button(window, text='Вывести полученный список: ', command=lambda: ex_2_pz_4_func2(entry1, entry2, window))
    bt2.grid(row=13, columnspan=5)
    label = Label(window)
    label.grid(row=14)


def pz_4_ex3():
    window = Tk()
    window.title("Работа 4. Задание 3.")
    window.geometry("500x400")
    bt3 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt3.grid(columnspan=2, sticky=W)
    label = Label(window)
    label.grid(row=2)
    label = Label(window, text="Пусть журнал по предмету «Информационные технологии» представлен в виде списка:", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="my_len = [[‘БО-331101’,[‘Акулова Алена’, ‘Бабушкина Ксения’, …….]],", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="[‘ БОВ-421102’,[…..]],[‘ БО-331103’,[….]]]. Выведите списки всех групп построчно в виде:", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="<Название группы>\n<ФИО>\n<ФИО>", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window)
    label.grid(columnspan=5)
    bt1 = Button(window, text='Ввести списки', command=lambda: ex_3_pz_4(window))
    bt1.grid(row=10, columnspan=5)
    label = Label(window)
    label.grid(row=11)


def pz_4_ex4():
    my_len = [['БО-331101', ['Прохорова Алена', 'Бабушкина Ксения', 'Иванов Иван']],
              ['БОВ-421102', ['Сергеев Максим', 'Пономарев Александр', 'Быкова Елизавета']],
              [' БО-331103', ['Матвеев Эрик', 'Зайцева Вероника', 'Попова Амелия']]]
    window = Tk()
    window.title("Работа 4. Задание 4.")
    window.geometry("600x500")
    bt3 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt3.grid(columnspan=2, sticky=W)
    label = Label(window)
    label.grid(row=2)
    label = Label(window, text="Пусть журнал по предмету «Информационные технологии» представлен в виде списка:", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="my_len = [[‘БО-331101’,[‘Акулова Алена’, ‘Бабушкина Ксения’, …….]],[‘ БОВ-421102’,[…..]],[‘ БО-331103’,[….]]].", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window, text="Выведите всех студентов (и их группы), чья фамилия начинается на букву «П», а имя на букву «А»", justify=CENTER)
    label.grid(columnspan=5)
    label = Label(window)
    label.grid(columnspan=5)
    bt1 = Button(window, text='Вывести изначальный список', command=lambda: ex_4_pz_4_func1(window, my_len))
    bt1.grid(row=7, columnspan=5)
    label = Label(window)
    label.grid(row=8)
    bt1 = Button(window, text='Вывести выбранных студентов', command=lambda: ex_4_pz_4_func2(window, my_len))
    bt1.grid(row=15, columnspan=5)
    label = Label(window)
    label.grid(row=16)


def pz_5_ex1():
    window = Tk()
    window.title("Работа 5. Задание 1")
    window.geometry("350x350")
    bt3 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt3.grid(columnspan=2, sticky=W)
    label = Label(window)
    label.grid(row=2)
    label = Label(window, text="Пусть дана некоторая директория (папка).", justify=CENTER)
    label.grid(columnspan=2, ipadx=50)
    label = Label(window, text="Посчитайте количество файлов в данной", justify=CENTER)
    label.grid(columnspan=2)
    label = Label(window, text="директории (папке) и выведите на экран.", justify=CENTER)
    label.grid(columnspan=2)
    label = Label(window)
    label.grid(row=6)
    btn = Button(window, text="Выбрать путь", command=lambda: ex_1_pz_5(window))
    btn.grid(columnspan=2, row=7)


def pz_5_ex2():
    window = Tk()
    window.geometry('420x650')
    window.title("Работа 5. Задание 2")
    bt3 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt3.grid(columnspan=2, sticky=W)
    label = Label(window)
    label.grid(row=2)
    label = Label(window, text="Пусть дан список. Считайте информацию из файла.")
    label.grid()
    label = Label(window, text="Выведите информацию о студентах, отсортировав их по номеру группы.")
    label.grid()
    label = Label(window, text="")
    label.grid()
    button = Button(window, text="Вывести информацию из файла", command=lambda: ex_3_pz_5_info(window))
    button.grid()
    label = Label(window, text="")
    label.grid()
    button1 = Button(window, text="Сортировать", command=lambda: ex_3_pz_5_sorts(window))
    button1.grid()
    result_label = Label(window, text="")
    result_label.grid()
    result_label = Label(window, text="Несортированный список:")
    result_label.grid()
    label = Label(window, text="")
    label.grid()
    result_label = Label(window, text="Сортированный список:")
    result_label.grid(row=21)


def pz_5_ex3():
    window = Tk()
    window.geometry('850x720')
    window.title("Работа 5. Задание 3")
    bt3 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt3.grid(columnspan=2, sticky=W)
    label = Label(window)
    label.grid(row=2)
    label = Label(window, text="Пусть дан список. Считайте информацию из файла.")
    label.grid(columnspan=7)
    label = Label(window, text="Задание 2. Выведите информацию о студентах, отсортировав их по номеру группы.")
    label.grid(columnspan=7)
    label = Label(window, text="Задание 3. Упорядочить по увеличению возраста студентов в заданной пользователем группе на 1")
    label.grid(columnspan=7)
    label = Label(window, text="")
    label.grid()
    label = Label(window, text="Задание 2")
    label.grid(columnspan=2, pady=3)
    button = Button(window, text="Вывести информацию из файла", command=lambda: ex_3_pz_5_info(window))
    button.grid(columnspan=2)
    label = Label(window, text="")
    label.grid()
    result_label = Label(window, text="Несортированный список:")
    result_label.grid(columnspan=2)
    label = Label(window, text="")
    label.grid()
    button2 = Button(window, text="Отсортировать", command=lambda: ex_3_pz_5_sorts(window))
    button2.grid(columnspan=2, row=21)
    result_label = Label(window, text="")
    result_label.grid()
    result_label = Label(window, text="Сортированный список:")
    result_label.grid(row=23, columnspan=2)
    label = Label(window, text="Задание 3")
    label.grid(column=4, columnspan=2, pady=(0, 10), row=7)
    Label(window, text='Выберите группу: ').grid(column=4, row=8, sticky=E)
    gr = ttk.Combobox(window, width=27, state="readonly")
    gr['values'] = ('БО-333333', 'БО-222222', 'БО-111111')
    gr.grid(column=5, row=8, sticky=E)
    button1 = Button(window, text="Выбрать", command=lambda: ex_3_pz_5_choc(window, gr))
    button1.grid(column=4, columnspan=2, row=9, pady=(20, 0))


def pz_5_ex4():
    window = Tk()
    window.geometry('1150x625')
    window.title("Работа 5. Задание 4")
    bt3 = Button(window, text='Выйти из программы', command=lambda: exite(window))
    bt3.grid(columnspan=2, sticky=W)
    label = Label(window, text="Пусть дан список. Считайте информацию из файла.")
    label.grid(columnspan=8)
    label = Label(window, text="Задание 2. Выведите информацию о студентах, отсортировав их по номеру группы.")
    label.grid(columnspan=8)
    label = Label(window, text="Задание 3. Упорядочить по увеличению возраста студентов в заданной пользователем группе на 1")
    label.grid(columnspan=8)
    label = Label(window, text="Задание 4. Добавьте возможность сохранения новых данных обратно в файл")
    label.grid(columnspan=8)
    label = Label(window, text="")
    label.grid()
    label = Label(window, text="Задание 2")
    label.grid(columnspan=2, pady=3)
    button = Button(window, text="Вывести информацию из файла", command=lambda: ex_3_pz_5_info(window))
    button.grid(column=0, row=7, sticky=E)
    result_label = Label(window, text="Несортированный список:")
    result_label.grid(columnspan=2, row=8)
    button2 = Button(window, text="Отсортировать", command=lambda: ex_3_pz_5_sorts(window))
    button2.grid(column=1, row=7, sticky=W)
    result_label = Label(window, text="")
    result_label.grid()
    result_label = Label(window, text="Сортированный список:")
    result_label.grid(row=23, columnspan=2)
    label = Label(window, text="Задание 3")
    label.grid(column=4, columnspan=2, pady=(0, 10), row=6)
    Label(window, text='Выберите группу: ').grid(column=4, row=7, sticky=E)
    gr = ttk.Combobox(window, width=27, state="readonly")
    gr['values'] = ('БО-333333', 'БО-222222', 'БО-111111')
    gr.grid(column=5, row=7, sticky=E)
    button1 = Button(window, text="Выбрать", command=lambda: ex_3_pz_5_choc(window, gr))
    button1.grid(column=4, columnspan=2, row=8)
    label = Label(window, text="Задание 4", justify=CENTER)
    label.grid(column=6, pady=(0, 10), row=6, columnspan=2)
    label = Label(window, text='Номер в списке: ')
    label.grid(column=6, columnspan=2, row=7, sticky=W)
    entry = Entry(window, width=35)
    entry.grid(column=7, row=7, columnspan=2, sticky=E)
    label = Label(window, text='ФИО студента:  ')
    label.grid(column=6, row=8, sticky=E)
    entry_1 = Entry(window, width=35)
    entry_1.grid(column=7, row=8, sticky=W)
    label = Label(window, text='Возраст студента: ')
    label.grid(column=6, row=9, sticky=E)
    entry_2 = Entry(window, width=35)
    entry_2.grid(column=7, row=9, sticky=W)
    label = Label(window, text='Номер группы: ')
    label.grid(column=6, row=10, sticky=E)
    entry_3 = Entry(window, width=35)
    entry_3.grid(column=7, row=10, sticky=W)
    button3 = Button(window, text="Сохранить", command=lambda: ex_3_pz_5_save_file(entry, entry_1, entry_2, entry_3), justify=CENTER)
    button3.grid(column=6, row=11, pady=(20, 0), padx=(20, 0), columnspan=2)


def pz_1_choice(_):
    s = listbox_1.get(listbox_1.curselection())
    y = listbox_1.curselection()
    n = y[0]
    match s:
        case 'задание 1':
            pz_1_ex1()
        case 'задание 2':
            pz_1_ex2()
        case 'задание 3':
            pz_1_ex3()
        case 'задание 4':
            pz_1_ex4()
    listbox_1.selection_clear(n)


def pz_2_choice(_):
    s = listbox_1.get(listbox_1.curselection())
    y = listbox_1.curselection()
    n = y[0]
    match s:
        case 'задание 1':
            pz_2_ex1()
        case 'задание 2':
            pz_2_ex2()
        case 'задание 3':
            pz_2_ex3()
        case 'задание 4':
            pz_2_ex4()
    listbox_1.selection_clear(n)


def pz_3_choice(_):
    s = listbox_1.get(listbox_1.curselection())
    y = listbox_1.curselection()
    n = y[0]
    match s:
        case 'задание 1':
            pz_3_ex1()
        case 'задание 2':
            pz_3_ex2()
        case 'задание 3':
            pz_3_ex3()
        case 'задание 4':
            pz_3_ex4()
    listbox_1.selection_clear(n)


def pz_4_choice(_):
    s = listbox_1.get(listbox_1.curselection())
    y = listbox_1.curselection()
    n = y[0]
    match s:
        case 'задание 1':
            pz_4_ex1()
        case 'задание 2':
            pz_4_ex2()
        case 'задание 3':
            pz_4_ex3()
        case 'задание 4':
            pz_4_ex4()
    listbox_1.selection_clear(n)


def pz_5_choice(_):
    s = listbox_1.get(listbox_1.curselection())
    y = listbox_1.curselection()
    n = y[0]
    match s:
        case 'задание 1':
            pz_5_ex1()
        case 'задание 2':
            pz_5_ex2()
        case 'задание 3':
            pz_5_ex3()
        case 'задание 4':
            pz_5_ex4()
    listbox_1.selection_clear(n)


def button_ex(button_select):
    a = button_select['text']
    label_ex = Label(text='Выберите номер задания', font=('arial bold', 10), background='beige')
    label_ex.grid(row=3, columnspan=8)
    label_not = Label(text='')
    label_not.grid(row=4)
    match a:
        case 'Работа 1':
            v = ['задание 1', 'задание 2', 'задание 3', 'задание 4']
            var = Variable(value=v)
            listbox_1['listvariable'] = var
            listbox_1['background'] = 'cadetblue2'
            listbox_1.bind("<<ListboxSelect>>", pz_1_choice)
            listbox_1.grid(row=5, columnspan=8)
        case 'Работа 2':
            v = ['задание 1', 'задание 2', 'задание 3', 'задание 4']
            var = Variable(value=v)
            listbox_1['listvariable'] = var
            listbox_1['background'] = 'coral'
            listbox_1.bind("<<ListboxSelect>>", pz_2_choice)
            listbox_1.grid(row=5, columnspan=8)
        case 'Работа 3':
            v = ['задание 1', 'задание 2', 'задание 3', 'задание 4']
            var = Variable(value=v)
            listbox_1['listvariable'] = var
            listbox_1['background'] = 'darkolivegreen1'
            listbox_1.bind("<<ListboxSelect>>", pz_3_choice)
            listbox_1.grid(row=5, columnspan=8)
        case 'Работа 4':
            v = ['задание 1', 'задание 2', 'задание 3', 'задание 4']
            var = Variable(value=v)
            listbox_1['listvariable'] = var
            listbox_1['background'] = 'hotpink2'
            listbox_1.bind("<<ListboxSelect>>", pz_4_choice)
            listbox_1.grid(row=5, columnspan=8)
        case 'Работа 5':
            v = ['задание 1', 'задание 2', 'задание 3', 'задание 4']
            var = Variable(value=v)
            listbox_1['listvariable'] = var
            listbox_1['background'] = 'cornflowerblue'
            listbox_1.bind("<<ListboxSelect>>", pz_5_choice)
            listbox_1.grid(row=5, columnspan=8)


root = Tk()
root.title("Работа 6. Меню программы")
root['background'] = 'beige'
root.geometry('500x300')
label5 = Label(root, text='Вы находитесь в меню\nВыберите номер работы', justify=CENTER, width=55, height=4, font=('arial bold', 12), background='beige')
label5.grid(columnspan=8)

listbox_1 = Listbox(root, selectmode=SINGLE, height=4, width=10, font=('arial bold', 11), borderwidth=0)
listbox_1.grid_forget()

button_pz_1 = Button(root, text='Работа 1', background='cadetblue2', borderwidth=1, relief=RIDGE)
hover_1 = Hovertip(button_pz_1, "Введение в Python")
button_pz_1.grid(column=1, row=1)
button_pz_1.config(command=lambda button_select=button_pz_1: button_ex(button_select))

button_pz_2 = Button(root, text='Работа 2', background='coral', borderwidth=1, relief=RIDGE)
hover_2 = Hovertip(button_pz_2, "Строки и списки")
button_pz_2.grid(column=2, row=1)
button_pz_2.config(command=lambda button_select=button_pz_2: button_ex(button_select))

button_pz_3 = Button(root, text='Работа 3', background='darkolivegreen1', borderwidth=1, relief=RIDGE)
hover_3 = Hovertip(button_pz_3, "Строки")
button_pz_3.grid(column=3, row=1)
button_pz_3.config(command=lambda button_select=button_pz_3: button_ex(button_select))

button_pz_4 = Button(root, text='Работа 4', background='hotpink2', borderwidth=1, relief=RIDGE)
hover_4 = Hovertip(button_pz_4, "Списки")
button_pz_4.grid(column=4, row=1)
button_pz_4.config(command=lambda button_select=button_pz_4: button_ex(button_select))

button_pz_5 = Button(root, text='Работа 5', background='cornflowerblue', borderwidth=1, relief=RIDGE)
hover_5 = Hovertip(button_pz_5, "Файлы и файловая система")
button_pz_5.grid(column=5, row=1)
button_pz_5.config(command=lambda button_select=button_pz_5: button_ex(button_select))

button_exit = Button(root, text='Выход', command=lambda: exite(root), background='crimson', borderwidth=1, relief=RIDGE)
hover_exit = Hovertip(button_exit, "Выход из программы")
button_exit.grid(column=6, row=1)
label_no = Label(text='')
label_no.grid(row=2)
root.mainloop()
