from tkinter import *
from tkinter import messagebox
import time

root = Tk()

root['bg'] = 'white'
root.title('Сортировка')
root.geometry('730x350')

root.resizable(width=False, height=False)

def btn1_click():
    if countInput.get() == '' or distanceInput.get() == '' or priceInput.get() == '':
        messagebox.showerror(title='Ошибка!', message='Введите все значения!')
    else:
        count = int(countInput.get())
        distances = str(distanceInput.get()).split()
        prices = str(priceInput.get()).split()
        if len(distances) < count:
            messagebox.showerror(title='Ошибка!', message='Введите расстояния для каждого сотрудника!')
            distanceInput.config(background='yellow')
        elif len(prices) < count:
            messagebox.showerror(title='Ошибка!', message='Введите тарифы для каждого сотрудника!')
            priceInput.config(background='yellow')
            distanceInput.config(background='white')
        else:
            text1.grid_forget()
            countInput.grid_forget()
            space1.grid_forget()
            text2.grid_forget()
            distanceInput.grid_forget()
            space2.grid_forget()
            text3.grid_forget()
            priceInput.grid_forget()
            space3.grid_forget()
            btn1.grid_forget()
            distances = list(map(int, distances))
            prices = list(map(int, prices))
            distances.sort(reverse=True)
            prices.sort()
            text = Label(frame, text="Сотрудников стоит распределить следующим образом:",
                          bg='white')
            text.grid(row=1, column=2)
            text = Label(frame, text=" ",
                         bg='white')
            text.grid(row=2, column=2, )
            for i in range(len(distances)):
                textl = Label(frame, text=f"{i + 1} сотрудник:",
                              bg='white')
                textl.grid(row=i + 3, column=1)
                textm = Label(frame, text=f"Расстояние - {distances[i]} км;",
                              bg='white')
                textm.grid(row=i + 3, column=2)
                textr = Label(frame, text=f"Тариф - {prices[i]} руб/мин",
                              bg='white')
                textr.grid(row=i + 3, column=3)




frame = Frame(root, bg='white')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

text1 = Label(frame, text="Введите количество сотрудников (число, без пробелов и любых знаков)", bg='white')
text1.grid(row=2, column=1)

countInput = Entry(frame, bg='white', width=70)
countInput.grid(row=3, column=1)

space1 = Label(frame, text="", bg='white')
space1.grid(row=4, column=1)

text2 = Label(frame, text="Введите через пробел значения расстояния от работы до дома для каждого сотрудника(в километрах) ", bg='white')
text2.grid(row=5, column=1)

distanceInput = Entry(frame, bg='white', width=70)
distanceInput.grid(row=6, column=1)

space2 = Label(frame, text="", bg='white')
space2.grid(row=7, column=1)

text3 = Label(frame, text="Введите через пробел стоимость проезда одного километра для разных тарифов", bg='white')
text3.grid(row=8, column=1)

priceInput = Entry(frame, bg='white', width=70)
priceInput.grid(row=9, column=1)

space3 = Label(frame, text="", bg='white')
space3.grid(row=10, column=1)

btn1 = Button(frame, text='Ввод', bg='white', command=btn1_click, width=5, height=1)
btn1.grid(row=11, column=1)

mainloop()