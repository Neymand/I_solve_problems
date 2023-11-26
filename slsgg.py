import tkinter as tk
from PIL import ImageTk, Image

win = tk.Tk()
win.title('Генератор паролей')
h = 165
w = 330
win.geometry(f'{w}x{h}')
win.config(bg='black')

img = Image.open('2023-07-12_11-27-40.png')
image = ImageTk.PhotoImage(img)


def resize_big():
    win.geometry('648x414')
    # BackGround image


    background_label = tk.Label(win, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
def resize_mini():
    win.geometry('330x165')
    win.config(bg='black')


main_menu = tk.Menu(win)
win.config(menu=main_menu)

r_menu = tk.Menu(main_menu)
main_menu.add_cascade(label='Size', menu=r_menu)
r_menu.add_cascade(label='Full', command=resize_big)
r_menu.add_cascade(label='Mini', command=resize_mini)

win.mainloop()