import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letter = [random.choice(letters) for letter in range(nr_letters)]
    random_symbol = [random.choice(symbols) for symbol in range(nr_symbols)]
    random_number = [random.choice(numbers) for number in range(nr_numbers)]

    password = random_letter + random_symbol + random_number
    random.shuffle(password)
    password = "".join(password)
    entry_pass.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = entry_website.get()
    user = entry_user.get()
    pass_get = entry_pass.get()
    new_data = {
        website: {
            "email": user,
            "password": pass_get
        }
    }

    print(type(website))

    if website == "" or pass_get == "":
        messagebox.showwarning(title="Empty field", message="Please input value into the field")

    else:
        try:
            with open("passwords.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("passwords.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_pass.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = entry_website.get().title()

    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
        try:
            messagebox.showinfo(website, f"Email: {data[website]["email"]}\nPassword: {data[website]["password"]}")
        except KeyError:
            messagebox.showerror("Error", f"No details for {website} exists")
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
padlock = canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

# website label
lbl_website = Label(text="Website:", font=("Arial", 12))
lbl_website.grid(column=0, row=1)

# email/user label
lbl_username = Label(text="Email/Username:", font=("Arial", 12))
lbl_username.grid(column=0, row=2)

# password label
lbl_password = Label(text="Password:", font=("Arial", 12))
lbl_password.grid(column=0, row=3)

# website input
entry_website = Entry(width=20)
entry_website.focus()
entry_website.grid(column=1, row=1)

# email/user input
entry_user = Entry(width=35)
entry_user.insert(END, "tracymcgravy@gmail.com")
entry_user.grid(column=1, row=2, columnspan=2)

# password output
entry_pass = Entry(width=19)
entry_pass.grid(column=1, row=3)

# add button
btn_add = Button(text="Add", width=30, command=add_password)
btn_add.grid(column=1, row=4, columnspan=2)

# generate pass button
btn_generate = Button(text="Generate Password",width=13, command=generate_pass)
btn_generate.grid(column=2, row=3)

# search button
btn_generate = Button(text="Search",width=14, command=find_password)
btn_generate.grid(column=2, row=1)

window.mainloop()
