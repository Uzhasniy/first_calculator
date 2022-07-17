import math
from tkinter import *
from tkinter import messagebox

#функции
#цифарки
def click_one():
    clicks.set(clicks.get() + str(1))
def click_two():
    clicks.set(clicks.get() + str(2))
def click_tree():
    clicks.set(clicks.get() + str(3))
def click_four():
    clicks.set(clicks.get() + str(4))
def click_five():
    clicks.set(clicks.get() + str(5))
def click_six():
    clicks.set(clicks.get() + str(6))
def click_seven():
    clicks.set(clicks.get() + str(7))
def click_eight():
    clicks.set(clicks.get() + str(8))
def click_nine():
    clicks.set(clicks.get() + str(9))
def click_zero():
    clicks.set(clicks.get() + str(0))
#арифметика
def click_plus():
    global a, znach
    a = float(clicks.get())
    znach = 1
    clicks.set('')
def click_minus():
    global a, znach
    a = float(clicks.get())
    znach = 2
    clicks.set('')
def click_umnozh():
    global a, znach
    a = float(clicks.get())
    znach = 3
    clicks.set('')
def click_delit():
    global a, znach
    a = float(clicks.get())
    znach = 4
    clicks.set('')
#результат
def click_result():
    global b
    b = int(clicks.get())
    int(b)
    clicks.set('')
    check()
def check():
    global c
    match znach:
        case 1:
            c = a+b
            str(c)
            clicks.set(c)
            clicks.set(clicks.get())
        case 2:
            c = a-b
            str(c)
            clicks.set(c)
            clicks.set(clicks.get())
        case 3:
            c = a*b
            str(c)
            clicks.set(c)
            clicks.set(clicks.get())   
        case 4:
            c = a/b
            str(c)
            clicks.set(c)
            clicks.set(clicks.get())   
def show():
    messagebox.showinfo("Слова благодарности", words.get())
#бинды арифм
def ravno_k(event):
    click_result()
def plus_k(event):
    click_plus()
def minus_k(event):
    click_minus()
def umnozh_k(event):
    click_umnozh()
def delit_k(event):
    click_delit()
#бинды цифарки
def one_k(event):
    click_one()
def two_k(event):
    click_two()
def tree_k(event):
    click_tree()
def four_k(event):
    click_four()
def five_k(event):
    click_five()
def six_k(event):
    click_six()
def seven_k(event):
    click_seven()
def eight_k(event):
    click_eight()
def nine_k(event):
    click_nine()
def zero_k(event):
    click_zero()

#основа
kalk = Tk()
kalk.title("Калькулятор для дэбилов")
kalk.configure(bg='black')
kalk.iconbitmap('heart.ico')
kalk.geometry("245x300+500+200")

#варвары
words = StringVar()
words.set('я не знаю на каком святом духе\nоно работает но как же я харош\n\nкста я люблю когда волосатые\nмужики обмазываются маслом...')
clicks = StringVar()

#лэйбл
viv = Entry(textvariable=clicks, background='#000000', fg='#ffffff', font='30', bd=0)
viv.grid(columnspan=3, row=0, pady=20)

#плюс минус сука саси пинус
plus = Button(text='+',background='#f0f0f0',padx='20',pady='15',font='30', command=click_plus)
plus.grid(column=0, row=1)
minus = Button(text='-', background='#f0f0f0', padx='22', pady='15', font='30', command=click_minus)
minus.grid(column=1, row=1)
umnozh = Button(text='*', background='#f0f0f0', padx='21', pady='15', font='30', command=click_umnozh)
umnozh.grid(column=2, row=1)
delit = Button(text='/', background='#f0f0f0', padx='23', pady='15', font='30', command=click_delit)
delit.grid(column=3, row=1)

#цифарки
one = Button(text='1',background='#f0f0f0', padx='20', pady='15', font='30', command=click_one)
one.grid(column=0, row=2)
two = Button(text='2',background='#f0f0f0', padx='20', pady='15', font='30', command=click_two)
two.grid(column=1, row=2)
tree = Button(text='3',background='#f0f0f0', padx='20', pady='15', font='30', command=click_tree)
tree.grid(column=2, row=2)
four = Button(text='4',background='#f0f0f0', padx='20', pady='15', font='30', command=click_four)
four.grid(column=0, row=3)
five = Button(text='5',background='#f0f0f0', padx='20', pady='15', font='30', command=click_five)
five.grid(column=1, row=3)
six = Button(text='6',background='#f0f0f0', padx='20', pady='15', font='30', command=click_six)
six.grid(column=2, row=3)
seven = Button(text='7',background='#f0f0f0', padx='20', pady='15', font='30', command=click_seven)
seven.grid(column=0, row=4)
eight = Button(text='8',background='#f0f0f0', padx='20', pady='15', font='30', command=click_eight)
eight.grid(column=1, row=4)
nine = Button(text='9',background='#f0f0f0', padx='20', pady='15', font='30', command=click_nine)
nine.grid(column=2, row=4)
zero = Button(text='0',background='#f0f0f0', padx='20', pady='15', font='30', command=click_zero)
zero.grid(column=3, row=2)

#пара слов
slova = Button(text='☺',background='#f0f0f0', padx='17', pady='15', font='30', command=show)
slova.grid(column=3, row=3)

#бинды арифметики
kalk.bind('<Return>', ravno_k)
kalk.bind('+', plus_k)
kalk.bind('-', minus_k)
kalk.bind('*', umnozh_k)
kalk.bind('/', delit_k)

#бинды цифарак
kalk.bind('1', one_k)
kalk.bind('2', two_k)
kalk.bind('3', tree_k)
kalk.bind('4', four_k)
kalk.bind('5', five_k)
kalk.bind('6', six_k)
kalk.bind('7', seven_k)
kalk.bind('8', eight_k)
kalk.bind('9', nine_k)
kalk.bind('0', zero_k)

#вывод
rav = Button(text='=',background='#f0f0f0',padx='21',pady='15',font='30', command=click_result)
rav.grid(column=3, row=4)

kalk.mainloop()