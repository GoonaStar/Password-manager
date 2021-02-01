from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passsword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    user_website_input = website_entry.get()
    user_email_input = username_entry.get()
    user_password_input = password_entry.get()

    if len(user_website_input) == 0 or len(user_password_input) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave empty fields")
    else:
        is_ok = messagebox.askokcancel(title=user_website_input,
                                       message=f"These are the details entered : \nEmail: {user_email_input}\n "
                                               f"Password: {user_password_input}\n Save?")

        if is_ok:
            with open("data.txt", mode="a") as data:
                list_input = f"{user_website_input} | {user_email_input} | {user_password_input}\n"
                data.write(list_input)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = Image.open("images.png")
image = image.resize((150, 150))
password_img = ImageTk.PhotoImage(image)
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, columnspan=2, row=1)
website_entry.focus()

username_label = Label(text="Username/Email:")
username_label.grid(column=0, row=2)

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "thibalo@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_button = ttk.Button(text="Generate Password", command=generate_passsword)
generate_password_button.grid(column=2, row=3)

button_add = ttk.Button(text="add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)
window.mainloop()
