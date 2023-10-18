import json
import tkinter
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

GHOST_WHITE = "#F8F8FF"
FONT_NAME = "Arial"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += ([random.choice(letters) for char in range(nr_letters)])
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    password = password.join(password_list)

    #print(f"{new_password}")
    print(f"Your password is: {password}")
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details_to_file():
    website = len(website_entry.get())
    password = len(password_entry.get())
    new_data = {
        website_entry.get(): {
            "email": username_entry.get(),
            "password": password_entry.get(),
        }
    }
    if website and password:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: \nEmail: {username_entry.get()}"
                                                                  f"\nPassword: {password_entry.get()} \n Click OK to save")
        if is_ok:
            try:
                with open("password_manager.json", "r") as data_file:
                    # Reading the old data
                    data = json.load(data_file)
                    # Updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                with open("password_manager.json", "w") as data_file:
                    # Create a new file if there is an exception
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("password_manager.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showerror(title="Error", message="You left some fields empty.")


def find_password():
    website = website_entry.get()
    try:
        with open("password_manager.json", "r") as data_file:
            # Reading the password manger json file
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    else:
        if website in data:
            messagebox.showinfo(title="Password found",
                                message=f"Email: {data[website]['email']} \n Password: {data[website]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg=GHOST_WHITE)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=GHOST_WHITE)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text=f"Website:", font=(FONT_NAME, 20), fg="black", bg=GHOST_WHITE)
website_label.grid(column=0, row=1)

website_entry = Entry(width=35, fg="black", bg=GHOST_WHITE, highlightthickness=0)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_label = Label(text=f"Email/Username:", font=(FONT_NAME, 20), fg="black", bg=GHOST_WHITE)
username_label.grid(column=0, row=2)

username_entry = Entry(width=35, fg="black", bg=GHOST_WHITE, highlightthickness=0)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "hksg2012@gmail.com")

password_label = Label(text=f"Password:", font=(FONT_NAME, 20), fg="black", bg=GHOST_WHITE)
password_label.grid(column=0, row=3)

password_entry = Entry(width=18, fg="black", bg=GHOST_WHITE, highlightthickness=0)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", highlightthickness=0, fg="black", bg=GHOST_WHITE, width=12, command=generate_password)
generate_button.grid(column=2, row=3)

search_button = Button(text="Search", highlightthickness=0, fg="black", bg=GHOST_WHITE, width=12, command=find_password)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", fg="black", bg=GHOST_WHITE, width=33, borderwidth=0, command=save_details_to_file)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()