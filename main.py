from tkinter import *

root = Tk()
root.title("Calc")
root.geometry('200x300')
root.resizable(False, False)

c1 = Entry(width=20)
c2 = Entry(width=20)
p = Button(text='+')
m = Button(text='-')
mul = Button(text='*')
de = Button(text='/')
r1 = Label(text='Результат:')
r = Label(bg='white', width=20)
c = Button(text='Очистить')

def res_p(event):
    try:
        n1 = int(c1.get())
        n2 = int(c2.get())
        res = n1+n2
        r['text'] = res
    except ValueError:
        r['text'] = 'Введите числа'

def res_m(event):
    try:
        n1 = int(c1.get())
        n2 = int(c2.get())
        res = n1-n2
        r['text'] = res
    except ValueError:
        r['text'] = 'Введите числа'

def res_mul(event):
    try:
        n1 = int(c1.get())
        n2 = int(c2.get())
        res = n1*n2
        r['text'] = res
    except ValueError:
        r['text'] = 'Введите числа'

def res_de(event):
    try:
        n1 = int(c1.get())
        n2 = int(c2.get())
        res = n1/n2
        r['text'] = res
    except ZeroDivisionError:
        r['text'] = 'Делить на 0 нельзя'
    except ValueError:
        r['text'] = 'Введите числа'

def clear(event):
    r['text'] = ''
    c1.delete(0, 'end')
    c2.delete(0, 'end')

p.bind("<Button-1>", res_p)
m.bind("<Button-1>", res_m)
mul.bind("<Button-1>", res_mul)
de.bind("<Button-1>", res_de)
c.bind("<Button-1>", clear)

c1.pack()
c2.pack()
p.pack()
m.pack()
mul.pack()
de.pack()
r1.pack()
r.pack()
c.pack()

root.mainloop()
