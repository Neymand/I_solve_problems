#import random
import tkinter as tk
import secrets
from PIL import Image, ImageTk

letters = 'qwertyuiopasdfghjklzxcvbnm'
number = '1234567890'
up_reg = 'QWERTYUIOPASDFGHJKLZXCVBNM'
symbols = "-=;'[]\,./~!@#$%^&*()_+{}:|<>?"



def create_password(length, *args):
    password = ''
    for i in range(length):
        password += secrets.choice(''.join(args))
    return password

def generate_password():
    length = int(length_var.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    use_uppercase = uppercase_var.get()

    combo = ''
    if use_letters:
        combo += letters
    if use_numbers:
        combo += number
    if use_symbols:
        combo += symbols
    if use_uppercase:
        combo += up_reg

    password = create_password(length, combo)
    result_var.set(password)

root = tk.Tk()

root.geometry('648x414')

# Поля для ввода параметров пароля
length_label = tk.Label(root, text="Длина пароля:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_var = tk.StringVar(value="")
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.grid(row=0, column=1, padx=10, pady=10)

letters_var = tk.BooleanVar(value=True)
letters_check = tk.Checkbutton(root, text="Использовать буквы", variable=letters_var)
letters_check.grid(row=1, column=0, padx=10, pady=10)

numbers_var = tk.BooleanVar(value=True)
numbers_check = tk.Checkbutton(root, text="Использовать цифры", variable=numbers_var)
numbers_check.grid(row=2, column=0, padx=10, pady=10)

symbols_var = tk.BooleanVar(value=False)
symbols_check = tk.Checkbutton(root, text="Использовать специальные символы", variable=symbols_var)
symbols_check.grid(row=1, column=1, padx=10, pady=10)

uppercase_var = tk.BooleanVar(value=False)
uppercase_check = tk.Checkbutton(root, text="Использовать заглавные буквы", variable=uppercase_var)
uppercase_check.grid(row=2, column=1, padx=10, pady=10)

# Кнопка генерации пароля
generate_button = tk.Button(root, text="Создать пароль", command=generate_password)
generate_button.grid(row=120, column=0, columnspan=5, padx=50, pady=10)

# Поле для вывода пароля
result_var = tk.StringVar(value="")
result_label = tk.Label(root, textvariable=result_var)
result_entry = tk.Entry(root, textvariable=result_var)
result_entry.grid(row=40, column=0, columnspan=2, padx=10, pady=10)



root.mainloop()










