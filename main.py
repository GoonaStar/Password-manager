from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from random import choice, randint, shuffle
import pyperclip
import json

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

# ---------------------------- SEARCH PASSWORD -----------------------------

def find_password():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            input_website = website_entry.get()
            mail_related = data[input_website]["email"]
            password_related = data[input_website]["password"]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found")
    except KeyError:
        messagebox.showinfo(title="Error", message="No details for this website exists")
    else:
        messagebox.showinfo(title=input_website, message=f"Email: {mail_related}\n Password: {password_related}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    user_website_input = website_entry.get()
    user_email_input = username_entry.get()
    user_password_input = password_entry.get()
    new_data = {
        user_website_input: {
            "email": user_email_input,
            "password": user_password_input,
                     }
    }

    if len(user_website_input) == 0 or len(user_password_input) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave empty fields")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
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

button_search = Button(text="Search", width= 14, command=find_password)
button_search.grid(column=2, row =1)

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
