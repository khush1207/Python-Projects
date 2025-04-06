from tkinter import *
import random
from tkinter import messagebox   # messagebox is yet another module, therefore a module does not get imported with *
import pyperclip  # This module make copying and pasting job easier with the help of clipboard
import json
new_data = {}
p = ""
e = ""
w = ""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    p = "".join(password_list)
    i_pass.insert(0, p)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_clicked():
    # Creating a dialogue box for confirmation of their details
    global p, e, w
    p = i_pass.get()
    e = i_user.get()
    w = i_web.get()
    global new_data
    new_data = {
        w: {
            "email": e,
            "password": p,
        }
    }

    if len(i_web.get()) == 0 or len(i_user.get()) == 0 or len(i_pass.get()) == 0:
        messagebox.showwarning(title="Opps!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=w, message=f"The details entered are:\nEmail: {e}"f"\nPassword: {p}\n"
                                                        f"Are you sure you want to confirm?")
        if is_ok:
            try:
                # Creating a Jason data file to search easily through the file
                with open("data_manager.json", mode="r") as file:
                    # Read old data
                    data = json.load(file)

            except FileNotFoundError:
                with open("data_manager.json", mode="w") as file:
                    # Saving updated data
                    json.dump(new_data, file, indent=4)

            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data_manager.json", mode="w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)

            finally:
                # To delete the entries to make new entries
                i_web.delete(0, END)
                i_user.delete(0, END)
                i_pass.delete(0, END)
                i_web.focus()
        pyperclip.copy(p)  # Directly paste where you wanted to. No need to copy first
        pyperclip.paste()

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    global p, e, w
    try:
        with open("data_manager.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="File Empty", message="Make a new entry first.")
        if len(i_web.get()) == 0:
            messagebox.showwarning(title="Opps!", message="Please write what is to be searched!")
    else:
        if i_web.get() in data:
            email = data[i_web.get()]["email"]
            pass_word = data[i_web.get()]["password"]
            messagebox.showinfo(title=i_web.get(), message=f"Email: {email}\nPassword: {pass_word}")
        else:
            messagebox.showwarning(title="Opps!", message=f"No entry for website {i_web.get()} made.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website = Label(text="Website :", font=("Arial", 10))
website.grid(column=0, row=1)
website.config(padx=10, pady=10)
user_name = Label(text="Email/UserName :", font=("Arial", 10))
user_name.grid(column=0, row=2)
user_name.config(padx=10, pady=10)
password = Label(text="Password :", font=("Arial", 10))
password.grid(column=0, row=3)
password.config(padx=10, pady=10)

i_web = Entry(width=33)
i_web.grid(column=1, row=1)
i_web.focus()  # To already show up the cursor in the website field when the program launches
i_user = Entry(width=52)
i_user.grid(column=1, row=2, columnspan=2)
# i_user.insert(0, "angela@gmail.com")  This method is used to have predefined value to a certain textbox
i_pass = Entry(width=33)
i_pass.grid(column=1, row=3)

b_pass = Button(text="Generate Password", highlightthickness=0, width=15, command=generate_password)
b_pass.grid(column=2, row=3)
b_add = Button(text="Add", width=44, highlightthickness=0, command=add_clicked)
b_add.grid(column=1, row=4, columnspan=2)
b_search = Button(text="Search", highlightthickness=0, width=15, command=find_password)
b_search.grid(column=2, row=1)

window.mainloop()
