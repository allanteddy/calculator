from tkinter import *

root = Tk()
root.title("simple calculator")

e = Entry(root, width=50)
e.grid(row=0, column=0, columnspan=3)


def button_press(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))


def clear():
    e.delete(0, END)


def addition():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)


def equal():
    var = e.get()
    e.delete(0, END)

    if math == 'addition':
        e.insert(0, str(f_num + int(var)))

    if math == 'subtraction':
        e.insert(0, str(f_num - int(var)))

    if math == 'multiplication':
        e.insert(0, str(f_num * int(var)))

    if math == 'division':
        e.insert(0, str(f_num / int(var)))


def subtraction():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)
    pass


def multiplication():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)


def division():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)


# define buttons
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_press(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_press(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_press(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_press(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_press(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_press(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_press(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_press(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_press(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_press(0))
button_add = Button(root, text='+', padx=40, pady=20, command=addition)
button_sub = Button(root, text='-', padx=41, pady=20, command=subtraction)
button_mul = Button(root, text='x', padx=41, pady=20, command=multiplication)
button_div = Button(root, text='/', padx=39, pady=20, command=division)
button_equal = Button(root, text='=', padx=90, pady=20, command=equal)
button_clear = Button(root, text='clear', padx=80, pady=20, command=clear)

# put buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()
