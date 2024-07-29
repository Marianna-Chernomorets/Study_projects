from tkinter import *
from tkinter.messagebox import showerror, askyesno, showinfo
import os
import csv
from tkinter import ttk
import copy
from random import randint
from datetime import *
import re
import matplotlib.pyplot as plt
import pandas as pd
import tkinter.filedialog as fd
from PIL import Image, ImageTk


def exite(window):
    result = askyesno(message="Вы уверены, что хотите закрыть окно?")
    if result:
        window.destroy()


def keep(entry, entry_1, entry_2, entry_3, entry_4, entry_5, entry_6):
    if entry.get() == '' or entry_1.get() == '' or entry_2.get() == '' or entry_3.get() == '' or entry_4.get() == '' or entry_5.get() == '' or entry_6.get() == '':
        showerror(title="Ошибка!", message="Заполните все поля ввода")
    elif not entry.get().isalpha() or not entry_1.get().isdigit() or not entry_3.get().isdigit() or not entry_4.get().isdigit() or (entry_5.get().lower() != 'да' and entry_5.get().lower() != 'нет') or (entry_6.get().lower() != 'да' and entry_6.get().lower() != 'нет'):
        showerror(title="Ошибка!", message="Некорректно заполненные поля ввода")
    else:
        new_stud = fd.asksaveasfilename()
        if new_stud == '':
            showerror(title="Ошибка!", message="Выберите файл для сохранения")
        elif new_stud != "":
            with open(new_stud, "a", newline='') as file:
                s = []
                s.extend([entry.get(), entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get(), entry_5.get(), entry_6.get()])
                writer = csv.writer(file, delimiter=';')
                writer.writerow(s)
                showinfo(title="Готово", message="Данные о студенте сохранены")


def saving():
    root_save = Tk()
    root_save['background'] = 'lightblue'
    Label(root_save, text='Введите данные студента для сохранения', font=('gabriola', 25), justify=CENTER, background='lightblue', foreground='grey9').grid(columnspan=7)
    Label(root_save, text='ФИО студента: ', font=('gabriola', 25), justify=CENTER, background='lightblue', foreground='grey9').grid(column=0, row=7, sticky=E)
    entry = Entry(root_save, width=35)
    entry.grid(column=1, row=7, sticky=W)

    Label(root_save, text='Курс:  ', font=('gabriola', 25), justify=CENTER, background='lightblue', foreground='grey9').grid(column=0, row=8, sticky=E)
    entry_1 = Entry(root_save, width=35)
    entry_1.grid(column=1, row=8, sticky=W, padx=5)

    Label(root_save, text='Группа: ', font=('gabriola', 25), justify=CENTER, background='lightblue', foreground='grey9').grid(column=0, row=9, sticky=E)
    entry_2 = Entry(root_save, width=35)
    entry_2.grid(column=1, row=9, sticky=W)

    Label(root_save, text='Оценка "Базы данных": ', font=('gabriola', 25), justify=CENTER, background='lightblue', foreground='grey9').grid(column=0, row=10, sticky=E)
    entry_3 = Entry(root_save, width=35)
    entry_3.grid(column=1, row=10, sticky=W)

    Label(root_save, text='Оценка "Комп.сети": ', font=('gabriola', 25), justify=CENTER, background='lightblue', foreground='grey9').grid(column=0, row=11, sticky=E)
    entry_4 = Entry(root_save, width=35)
    entry_4.grid(column=1, row=11, sticky=W)

    Label(root_save, text='Наличие льготы: ', font=('gabriola', 25), justify=CENTER, background='lightblue', foreground='grey9').grid(column=0, row=12, sticky=E)
    entry_5 = Entry(root_save, width=35)
    entry_5.grid(column=1, row=12, sticky=W)

    Label(root_save, text='Разрешена ли пересдача": ', font=('gabriola', 25), justify=CENTER, background='lightblue', foreground='grey9').grid(column=0, row=13, sticky=E)
    entry_6 = Entry(root_save, width=35)
    entry_6.grid(column=1, row=13, sticky=W)

    saved = Button(root_save, text='Сохранить', command=lambda: keep(entry, entry_1, entry_2, entry_3, entry_4, entry_5, entry_6), background="skyblue4", foreground="white", font=('Arial', 11))
    saved.grid(columnspan=2, pady=10)

    quite_save = Button(root_save, text='Закрыть окно', command=lambda: exite(root_save), background="skyblue4", foreground="white", font=('Arial', 11))
    quite_save.grid(columnspan=2, pady=10)

    root_save.mainloop()


def statistica(student):
    stud = student
    ot = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    oth = ['Курс', 'отличники', 'хорошисты', 'двоечники']
    n = 0
    while n < 4:
        for i in range(len(stud)):
            if int(stud[i][1]) == n+1:
                if int(stud[i][3]) == 5 and int(stud[i][4]) == 5:
                    ot[n][0] += 1
                elif (int(stud[i][3]) == 4 or int(stud[i][3]) == 5) and (int(stud[i][4]) == 5 or int(stud[i][4]) == 4):
                    ot[n][1] += 1
                elif (int(stud[i][3]) == 2 or int(stud[i][4]) == 2) and (stud[i][6] == 'да'):
                    ot[n][2] += 1
        n += 1
    df = pd.DataFrame([['1 курс', ot[0][0], ot[0][1], ot[0][2]], ['2 курс',  ot[1][0], ot[1][1], ot[1][2]], ['3 курс', ot[2][0], ot[2][1], ot[2][2]], ['4 курс', ot[3][0], ot[3][1], ot[3][2]]], columns=oth)
    df.plot(x='Курс', kind='bar', stacked=True, title='Отличники, хорошисты и двоечники по всем четырем курсам')
    plt.show()


def otl_step(student, st, sots):
    if st.get() == '' or sots.get() == '':
        showerror(title="Ошибка!", message="В строки со стипендиями должны быть введены целые цифры, не оставляйте поля ввода пустыми")
    elif not st.get().isdigit() or not sots.get().isdigit():
        showerror(title="Ошибка!", message="В строки со стипендиями должны быть введены цифры")
    else:
        stud = copy.deepcopy(student)
        root_otl = Tk()
        root_otl['background'] = 'mediumpurple1'
        Label(root_otl, text='Студенты-отличники и сумма начисленной им стипендии', font=('gabriola', 25), justify=CENTER, background='mediumpurple1', foreground='grey9').grid()
        baza = float(st.get())
        sotsial = float(sots.get())
        ln = len(stud)
        s = list()
        olich = list()
        for i in range(0, ln):
            if (int(stud[i][1]) == 1 or int(stud[i][1]) == 2) and (int(stud[i][3]) == 5 and int(stud[i][4]) == 5):
                s.append(baza+150)
                olich.append(stud[i])
            elif (int(stud[i][1]) == 3 or int(stud[i][1]) == 4) and (int(stud[i][3]) == 5 and int(stud[i][4]) == 5):
                s.append(baza + 300)
                olich.append(stud[i])
        ls = len(s)
        for i in range(0, len(olich)):
            if olich[i][5] == 'да':
                s[i] += sotsial
        tv = ttk.Treeview(root_otl, height=ls, show="headings")
        style = ttk.Style(tv)
        tv['columns'] = ('ФИО', 'Курс', 'Группа', 'Наличие льготы', 'Стипендия')
        tv.column('ФИО', anchor=CENTER, width=270)
        tv.column('Курс', anchor=CENTER, width=50)
        tv.column('Группа', anchor=CENTER, width=70)
        tv.column('Наличие льготы', anchor=CENTER, width=120)
        tv.column('Стипендия', anchor=CENTER, width=150)

        tv.heading('ФИО', text='ФИО', anchor=CENTER)
        tv.heading('Курс', text='Курс', anchor=CENTER)
        tv.heading('Группа', text='Группа', anchor=CENTER)
        tv.heading('Наличие льготы', text='Наличие льготы', anchor=CENTER)
        tv.heading('Стипендия', text='Стипендия', anchor=CENTER)
        for i in range(0, ls):
            tv.insert(parent='', index=i, text='', values=(olich[i][0], olich[i][1], olich[i][2], olich[i][5], s[i]))
        style.configure("Treeview", background="purple4", foreground="white", font=('Arial', 11))
        style.configure('Treeview.Heading', font=('Arial', 10))
        tv.grid(row=1, columnspan=3, sticky=W, padx=10, rowspan=ls)

        quite_otl = Button(root_otl, text='Закрыть окно', command=lambda: exite(root_otl), background="purple4", foreground="white", font=('Arial', 11))
        quite_otl.grid(row=ls+3, columnspan=3, pady=10)
        root_otl.mainloop()


def hor_step(student, st, sots):
    if st.get() == '' or sots.get() == '':
        showerror(title="Ошибка!", message="В строки со стипендиями должны быть введены целые цифры, не оставляйте поля ввода пустыми")
    elif not st.get().isdigit() or not sots.get().isdigit():
        showerror(title="Ошибка!", message="В строки со стипендиями должны быть введены цифры")
    else:
        stud = copy.deepcopy(student)
        root_hor = Tk()
        root_hor['background'] = 'lightblue'
        Label(root_hor, text='Студенты-хорошисты и сумма начисленной им стипендии', font=('gabriola', 25), justify=CENTER, background='lightblue', foreground='grey9').grid()
        baza = float(st.get())
        sotsial = float(sots.get())
        ln = len(stud)
        s = list()
        good = list()

        for i in range(0, ln):
            if (int(stud[i][3]) == 5) and (int(stud[i][4]) == 5):
                continue
            elif (int(stud[i][3]) == 4 or int(stud[i][3]) == 5) and (int(stud[i][4]) == 5 or int(stud[i][4]) == 4):
                s.append(baza)
                good.append(stud[i])
        ls = len(s)
        for i in range(0, len(good)):
            if good[i][5] == 'да':
                s[i] += sotsial

        tv = ttk.Treeview(root_hor, height=ls, show="headings")
        tv['columns'] = ('ФИО', 'Курс', 'Группа', 'Наличие льготы', 'Стипендия')
        tv.column('ФИО', anchor=CENTER, width=270)
        tv.column('Курс', anchor=CENTER, width=50)
        tv.column('Группа', anchor=CENTER, width=70)
        tv.column('Наличие льготы', anchor=CENTER, width=120)
        tv.column('Стипендия', anchor=CENTER, width=150)

        tv.heading('ФИО', text='ФИО', anchor=CENTER)
        tv.heading('Курс', text='Курс', anchor=CENTER)
        tv.heading('Группа', text='Группа', anchor=CENTER)
        tv.heading('Наличие льготы', text='Наличие льготы', anchor=CENTER)
        tv.heading('Стипендия', text='Стипендия', anchor=CENTER)
        for i in range(0, ls):
            tv.insert(parent='', index=i, text='', values=(good[i][0], good[i][1], good[i][2], good[i][5], s[i]))
        style = ttk.Style(tv)
        style.configure("Treeview", background="skyblue4", foreground="white", font=('Arial', 11))
        style.configure('Treeview.Heading', font=('Arial', 10))
        tv.grid(row=1, columnspan=3, sticky=W, padx=10, rowspan=ls)

        quite_hor = Button(root_hor, text='Закрыть окно', command=lambda: exite(root_hor), background="skyblue4", foreground="white", font=('Arial', 11))
        quite_hor.grid(pady=10)

        root_hor.mainloop()


def dvoech_ekz(student):
    root_dvoech = Tk()
    root_dvoech['background'] = 'light salmon'
    Label(root_dvoech, text='Студенты-двоечники и несданные экзамены', font=('gabriola', 25), justify=CENTER, background='light salmon', foreground='grey9').grid()
    bad = list()
    stud = copy.deepcopy(student)
    for i in range(0, len(stud)):
        if (int(stud[i][3]) == 2 or int(stud[i][4]) == 2) and (stud[i][6] == 'да'):
            bad.append(stud[i])
    for i in range(len(bad)):
        if int(bad[i][3]) == 2:
            bad[i][3] = 'Базы данных'
            if int(bad[i][4]) == 2:
                bad[i][3] += ', Комп. сети'
        else:
            bad[i][3] = 'Комп. сети'''
    tv = ttk.Treeview(root_dvoech, height=len(bad), show="headings")
    tv['columns'] = ('ФИО', 'Курс', 'Группа', 'Заваленный экзамен(ы)')
    tv.column('ФИО', anchor=CENTER, width=270)
    tv.column('Курс', anchor=CENTER, width=50)
    tv.column('Группа', anchor=CENTER, width=70)
    tv.column('Заваленный экзамен(ы)', anchor=CENTER, width=180)

    tv.heading('ФИО', text='ФИО', anchor=CENTER)
    tv.heading('Курс', text='Курс', anchor=CENTER)
    tv.heading('Группа', text='Группа', anchor=CENTER)
    tv.heading('Заваленный экзамен(ы)', text='Заваленный экзамен(ы)', anchor=CENTER)
    for i in range(0, len(bad)):
        tv.insert(parent='', index=i, text='', values=(bad[i][0], bad[i][1], bad[i][2], bad[i][3]))
    style = ttk.Style(tv)
    style.configure("Treeview", background="coral3", foreground="white", font=('Arial', 11))
    style.configure('Treeview.Heading', font=('Arial', 10))
    tv.grid(row=1, columnspan=3, sticky=W, padx=10, rowspan=len(bad))

    quite_dvoech = Button(root_dvoech, text='Закрыть окно', command=lambda: exite(root_dvoech), background="coral3", foreground="white", font=('Arial', 11))
    quite_dvoech.grid(pady=10)

    root_dvoech.mainloop()


def otchislinie(student):
    root_otchis = Tk()
    root_otchis['background'] = 'palegreen1'
    Label(root_otchis, text='Студенты на отчисление и несданные экзамены', font=('gabriola', 25), justify=CENTER, background='palegreen1', foreground='grey9').grid()
    fio = list()
    info = list()
    info_fin = list()
    stud = copy.deepcopy(student)
    for i in range(len(stud)):
        if (int(stud[i][3]) == 2 or int(stud[i][4]) == 2) and (stud[i][6] == 'нет'):
            info.append(stud[i])
            fio.append(stud[i][0])
    fio.sort()
    for i in range(len(info)):
        for j in range(len(fio)):
            if fio[i] == info[j][0]:
                info_fin.append(info[j])
    tv = ttk.Treeview(root_otchis, height=len(info_fin), show="headings")
    tv['columns'] = ('ФИО', 'Курс', 'Группа')
    tv.column('ФИО', anchor=CENTER, width=270)
    tv.column('Курс', anchor=CENTER, width=50)
    tv.column('Группа', anchor=CENTER, width=70)

    tv.heading('ФИО', text='ФИО', anchor=CENTER)
    tv.heading('Курс', text='Курс', anchor=CENTER)
    tv.heading('Группа', text='Группа', anchor=CENTER)
    for i in range(0, len(info_fin)):
        tv.insert(parent='', index=i, text='', values=(info_fin[i][0], info_fin[i][1], info_fin[i][2]))
    style = ttk.Style(tv)
    style.configure("Treeview", background="darkgreen", foreground="white", font=('Arial', 11))
    style.configure('Treeview.Heading', font=('Arial', 10))
    tv.grid(row=1, columnspan=3, padx=20, rowspan=len(info_fin))

    quite_otchis = Button(root_otchis, text='Закрыть окно', command=lambda: exite(root_otchis), background="darkgreen", foreground="white", font=('Arial', 11))
    quite_otchis.grid(pady=10)

    root_otchis.mainloop()


def oplatit(entry_kurs, summa, texts):
    ek = entry_kurs.get()
    if (texts != 'Рубли') and (ek == ''):
        showerror(title="Ошибка!", message="Введите курс валюты. Поле не должно быть пустым и курс не должен быть равен 0")
    elif (texts != 'Рубли') and (int(ek) == 0):
        showerror(title="Ошибка!", message="Введите курс валюты. Поле не должно быть пустым и курс не должен быть равен 0")
    elif texts != 'Рубли':
        root_summa = Tk()
        root_summa['background'] = 'plum1'
        Label(root_summa, text=f'оплатите {summa / int(ek)} {texts.lower()} в кассе', font=('gabriola', 20), justify=CENTER, background='plum1', foreground='grey9').grid()
        quite_summa = Button(root_summa, text='Закрыть окно', command=lambda: exite(root_summa), background="purple4", foreground="white", font=('Arial', 11))
        quite_summa.grid(pady=10)
        root_summa.mainloop()
    else:
        root_summa = Tk()
        root_summa['background'] = 'plum1'
        Label(root_summa, font=('gabriola', 20), text=f'оплатите {summa} рублей в кассе', justify=CENTER, background='plum1', foreground='grey9').grid()
        quite_summa = Button(root_summa, text='Закрыть окно', command=lambda: exite(root_summa), background="purple4", foreground="white", font=('Arial', 11))
        quite_summa.grid(pady=10)
        root_summa.mainloop()


def sel(lang, kurs, entry_kurs, summa, texts, oplata):
    if lang.get() == 2 or lang.get() == 3:
        kurs['state'] = 'normal'
        entry_kurs['state'] = 'normal'
    else:
        kurs['state'] = 'disabled'
        entry_kurs['state'] = 'disabled'
    oplata.grid()
    oplata['command'] = lambda: oplatit(entry_kurs, summa, texts)


def cash(rub, dollar, evro):
    rub['state'] = 'normal'
    dollar['state'] = 'normal'
    evro['state'] = 'normal'


def pay_out(number, datas):
    num = number.get()
    dt = datas.get()
    p_1 = re.compile("^[0-9]{2}/[0-9]{2}$")
    p_2 = re.compile("^[0-9]{13,19}")
    if not re.fullmatch(p_2, num):
        showerror(title="Ошибка!", message="Номер карты введен неверно, попробуйте еще раз")
    elif not re.fullmatch(p_1, dt):
        showerror(title="Ошибка!", message="Срок действия карты введен неверно, попробуйте еще раз")
    else:
        dat = dt.split('/')
        if int(dat[1])+2000 < date.today().year:
            showerror(title="Ошибка!", message="Ваша карта просрочена, введите данные другой карты")
        elif int(dat[1])+2000 == date.today().year and int(dat[0]) < date.today().month:
            showerror(title="Ошибка!", message="Ваша карта просрочена, введите данные другой карты")
        else:
            root_cards = Tk()
            root_cards['background'] = 'plum1'
            label10 = Label(root_cards, text='Оплата успешно прошла', font=('gabriola', 20), justify=CENTER, background='plum1', foreground='grey9')
            label10.grid()

            quite_cards = Button(root_cards, text='Закрыть окно', command=lambda: exite(root_cards), background="purple4", foreground="white", font=('Arial', 11))
            quite_cards.grid(pady=10)

            root_cards.mainloop()


def card():
    root_card = Tk()
    root_card['background'] = 'plum1'
    label11 = Label(root_card, text='Введите номер карты:', font=('gabriola', 20), justify=CENTER, background='plum1', foreground='grey9')
    label11.grid()
    number = Entry(root_card, width=30)
    number.grid()
    label12 = Label(root_card, text='Введите срок действия карты(через слэш):', font=('gabriola', 20), justify=CENTER, background='plum1', foreground='grey9')
    label12.grid()
    datas = Entry(root_card)
    datas.grid()
    to_pay = Button(root_card, text='Оплатить', command=lambda: pay_out(number, datas), background="purple4", foreground="white", font=('Arial', 11))
    to_pay.grid(pady=10)

    quite_card = Button(root_card, text='Закрыть окно', command=lambda: exite(root_card), background="purple4", foreground="white", font=('Arial', 11))
    quite_card.grid(pady=10)

    root_card.grid()


def paying(tv):
    stud = list()
    for select in tv.selection():
        item = tv.item(select)
        stud = item["values"]
    if not stud:
        showerror(title="Ошибка!", message="Выберите студента из таблицы")
    else:
        root_paying = Tk()
        root_paying['background'] = 'plum1'
        label5 = Label(root_paying, text=f'Имя: {stud[0]} \n Курс: {stud[1]} \n Группа: {stud[2]} \n Несданный экзамен: {stud[3]} \n Сумма для оплаты: {stud[4]}', font=('gabriola', 20), justify=CENTER, background='plum1', foreground='grey9')
        label5.grid()

        n = randint(10, 30)
        label6 = Label(root_paying, text=f'Оплатить в течении {n} дней \n Выберите способ оплаты:', font=('Cranberry Cyr', 17), justify=CENTER, background='plum1', foreground='grey9')
        label6.grid()

        kurs = Label(root_paying, text='Курс валюты:', state=DISABLED, font=('Arial', 11), justify=CENTER, background='plum1', foreground='grey9')
        entry_kurs = Entry(root_paying, state=DISABLED)
        oplata = Button(root_paying, text='Оплатить', background="purple4", foreground="white", font=('Arial', 11))
        texts = ['Рубли', 'Доллары', 'Евро']

        styles = ttk.Style(root_paying)
        styles.configure("TRadiobutton", background="plum1", foreground="grey9", font=('Arial', 11))

        lang = IntVar(root_paying, value=0)
        rub = ttk.Radiobutton(root_paying, text=texts[0], value=1, variable=lang, state=DISABLED, command=lambda: sel(lang, kurs, entry_kurs, stud[4], texts[0], oplata), style='TRadiobutton')
        rub.grid()
        dollar = ttk.Radiobutton(root_paying, text=texts[1], value=2, variable=lang, state=DISABLED, command=lambda: sel(lang, kurs, entry_kurs, stud[4], texts[1], oplata), style='TRadiobutton')
        dollar.grid()
        evro = ttk.Radiobutton(root_paying, text=texts[2], value=3, variable=lang, state=DISABLED, command=lambda: sel(lang, kurs, entry_kurs, stud[4], texts[2], oplata), style='TRadiobutton')
        evro.grid()
        kurs.grid()
        entry_kurs.grid()
        oplata.forget()

        nul = Button(root_paying, text='Наличные', command=lambda: cash(rub, dollar, evro), background="purple4", foreground="white", font=('Arial', 11))
        nul.grid()
        deb = Button(root_paying, text='Дебетовая карта', command=card, background="purple4", foreground="white", font=('Arial', 11))
        deb.grid()
        kred = Button(root_paying, text='Кредитная карта', command=card, background="purple4", foreground="white", font=('Arial', 11))
        kred.grid()

        quite_paing = Button(root_paying, text='Закрыть окно', command=lambda: exite(root_paying), background="purple4", foreground="white", font=('Arial', 11))
        quite_paing.grid(pady=10)

        root_paying.mainloop()


def rest(student):
    root_rest = Tk()
    root_rest['background'] = 'rosybrown1'
    stud_rest = list()
    stud = copy.deepcopy(student)
    price = list()
    for i in range(0, len(stud)):
        if (int(stud[i][3]) == 2 or int(stud[i][4]) == 2) and (stud[i][6] == 'да'):
            stud_rest.append(stud[i])
    for i in range(len(stud_rest)):
        if int(stud_rest[i][3]) == 2:
            stud_rest[i][3] = 'Базы данных'
            price.append(1500)
            if int(stud_rest[i][4]) == 2:
                stud_rest[i][3] += ', Комп. сети'
                price[i] += 1500
        else:
            stud_rest[i][3] = 'Комп. сети'
            price.append(1500)
    label4 = Label(root_rest, text='Выберите в таблице студента и нажмите на кнопку "Оплата задолженности"', font=('gabriola', 25), justify=CENTER, background='rosybrown1', foreground='grey9')
    label4.grid()
    tv = ttk.Treeview(root_rest, height=len(stud_rest), show="headings")
    tv['columns'] = ('ФИО', 'Курс', 'Группа', 'Экзамен(ы) для пересдачи', 'Стоимость')
    tv.column('ФИО', anchor=CENTER, width=270)
    tv.column('Курс', anchor=CENTER, width=50)
    tv.column('Группа', anchor=CENTER, width=70)
    tv.column('Экзамен(ы) для пересдачи', anchor=CENTER, width=180)
    tv.column('Стоимость', anchor=CENTER, width=140)

    tv.heading('ФИО', text='ФИО', anchor=CENTER)
    tv.heading('Курс', text='Курс', anchor=CENTER)
    tv.heading('Группа', text='Группа', anchor=CENTER)
    tv.heading('Экзамен(ы) для пересдачи', text='Экзамен(ы) для пересдачи', anchor=CENTER)
    tv.heading('Стоимость', text='Стоимость', anchor=CENTER)
    for i in range(0, len(stud_rest)):
        tv.insert(parent='', index=i, text='', values=(stud_rest[i][0], stud_rest[i][1], stud_rest[i][2], stud_rest[i][3], price[i]))
    style = ttk.Style(tv)
    style.configure("Treeview", background="indianred4", foreground="white", font=('Arial', 11))
    style.configure('Treeview.Heading', font=('Arial', 10))
    tv.grid(row=1, columnspan=3, padx=10, rowspan=len(stud_rest))
    pay = Button(root_rest, text='Оплата задолжненности', command=lambda: paying(tv), background="indianred4", foreground="white", font=('Arial', 11))
    pay.grid(pady=10)

    quite_rest = Button(root_rest, text='Закрыть окно', command=lambda: exite(root_rest), background="indianred4", foreground="white", font=('Arial', 11))
    quite_rest.grid(pady=10)

    root_rest.mainloop()


def accession(p, r, rt):
    pas = p.get()
    roots = rt
    roots.destroy()
    if pas != r:
        showerror(title="Ошибка!", message="Пароль неверный, попробуйте еще раз")
    else:
        root_info = Tk()
        root_info.geometry('950x500')

        root_info.resizable(width=False, height=False)
        image_1 = Image.open("главное_меню.png")
        image_1 = image_1.resize((950, 500), Image.LANCZOS)
        pic_1 = ImageTk.PhotoImage(image_1)
        Label(root_info, image=pic_1).grid(row=0, column=0)
        r = os.path.join(os.getcwd(), 'Студенты.csv')
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
        tv = ttk.Treeview(root_info, height=n, show="headings")
        tv['columns'] = ('ФИО', 'Курс', 'Группа', 'Оценка "Базы данных"', 'Оценка "Комп. сети"', 'Наличие льготы', 'Разрешена ли пересдача')
        style = ttk.Style(tv)
        tv.column('ФИО', anchor=CENTER, width=250)
        tv.column('Курс', anchor=CENTER, width=50)
        tv.column('Группа', anchor=CENTER, width=70)
        tv.column('Оценка "Базы данных"', anchor=CENTER, width=145)
        tv.column('Оценка "Комп. сети"', anchor=CENTER, width=130)
        tv.column('Наличие льготы', anchor=CENTER, width=105)
        tv.column('Разрешена ли пересдача', anchor=CENTER, width=170)

        tv.heading('ФИО', text='ФИО', anchor=CENTER)
        tv.heading('Курс', text='Курс', anchor=CENTER)
        tv.heading('Группа', text='Группа', anchor=CENTER)
        tv.heading('Оценка "Базы данных"', text='Оценка "Базы данных"', anchor=CENTER)
        tv.heading('Оценка "Комп. сети"', text='Оценка "Комп. сети"', anchor=CENTER)
        tv.heading('Наличие льготы', text='Наличие льготы', anchor=CENTER)
        tv.heading('Разрешена ли пересдача', text='Разрешена ли пересдача', anchor=CENTER)

        style.configure("Treeview", background="lightskyblue2", foreground="grey7", font=('Arial', 11))
        style.configure('Treeview.Heading', font=('Arial', 10))

        for i in range(0, n):
            tv.insert(parent='', index=i, text='', values=(f[i][0], f[i][1], f[i][2], f[i][3], f[i][4], f[i][5], f[i][6]))
        tv.place(relx=0.5, rely=0.25, anchor=CENTER)

        label4 = Label(root_info, text="Базовая стипендия:", font=('gabriola', 18), borderwidth=0, background='#333333', foreground='white')
        label4.place(relx=0.4, rely=0.5, anchor=CENTER)
        stip = Entry(root_info)
        stip.place(relx=0.6, rely=0.53, anchor=CENTER)

        label5 = Label(root_info, text="Социальная стипендия:", font=('gabriola', 18), borderwidth=0, background='#333333', foreground='white')
        label5.place(relx=0.4, rely=0.59, anchor=CENTER)
        sots_stip = Entry(root_info)
        sots_stip.place(relx=0.6, rely=0.59, anchor=CENTER)

        otl = Button(root_info, text='Отличники', command=lambda: otl_step(f, stip, sots_stip), font=('Arial', 12), background="dark salmon")
        otl.place(relx=0.1, rely=0.7, anchor=CENTER)

        hor = Button(root_info, text='Хорошисты', command=lambda: hor_step(f, stip, sots_stip), font=('Arial', 12), background="dark salmon")
        hor.place(relx=0.25, rely=0.7, anchor=CENTER)

        dvoech = Button(root_info, text='Двоечники', command=lambda: dvoech_ekz(f), font=('Arial', 12), background="dark salmon")
        dvoech.place(relx=0.4, rely=0.7, anchor=CENTER)

        otchis = Button(root_info, text='Отчисление', command=lambda: otchislinie(f), font=('Arial', 12), background="dark salmon")
        otchis.place(relx=0.55, rely=0.7, anchor=CENTER)

        restart = Button(root_info, text='Пересдача', command=lambda: rest(f), font=('Arial', 12), background="dark salmon")
        restart.place(relx=0.7, rely=0.7, anchor=CENTER)

        statistic = Button(root_info, text='Статистика', command=lambda: statistica(f), font=('Arial', 12), background="dark salmon")
        statistic.place(relx=0.87, rely=0.7, anchor=CENTER)

        save = Button(root_info, text='Сохранение данных', command=saving, font=('Arial', 12), background="dark salmon")
        save.place(relx=0.12, rely=0.9, anchor=CENTER)

        quite = Button(root_info, text='Закрыть окно', command=lambda: exite(root_info), font=('Arial', 12), background="dark salmon")
        quite.place(relx=0.87, rely=0.9, anchor=CENTER)

        root_info.mainloop()


root = Tk()
root.title("Начальная страница. Вход")
root.geometry('800x500')

root.resizable(width=False, height=False)
image = Image.open("заставка_8.jpg")
image = image.resize((800, 500), Image.LANCZOS)
pic = ImageTk.PhotoImage(image)
Label(root, image=pic).grid(row=0, column=0)

label1 = Label(root, text='Программа с данными для начисления студентам стипендии', justify=CENTER, borderwidth=0, font=('gabriola', 25), background='#15171C', foreground='white')
label1.place(relx=0.5, rely=0.12, anchor=CENTER)
label1 = Label(root, text='и отчисления задолжников по результатам сессии', justify=CENTER, borderwidth=0, font=('gabriola', 25), background='#15171C', foreground='white')
label1.place(relx=0.5, rely=0.22, anchor=CENTER)
label2 = Label(root, text='Введите пароль для входа в систему', justify=CENTER, font=('Cranberry Cyr', 17), background='#15171C', foreground='orange')
label2.place(relx=0.5, rely=0.35, anchor=CENTER)
right_password = '070123'
password = Entry(root, width=20, font=('Franklin Gothic Book', 17))
password.place(relx=0.5, rely=0.65, anchor=CENTER)
access = Button(root, text="Войти", font=('Arial', 12), command=lambda: accession(password, right_password, root), bg='darkorange3', foreground='white', width=10)
access.place(relx=0.5, rely=0.75, anchor=CENTER)
label3 = Label(root, text='Разработчик: Черноморец М.С. 2 курс ДП-21 2024г', justify=CENTER, font=('gabriola', 15), background='#15171C', foreground='white')
label3.place(relx=0.5, rely=0.91, anchor=CENTER)

root.mainloop()
