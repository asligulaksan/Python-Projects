from tkinter import *
from tkinter import messagebox
import pyperclip
import json

BG="#F5F5F5"
BLACK = "#121212"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random

# Generating password
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]

    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    passwordd = ''.join(password_list)

    password_entry.insert(0, f"{passwordd}")
    pyperclip.copy(passwordd) #Enables to ctrl+v

# ---------------------------- SEARCH BUTTON ------------------------------- #

#
def search_machine():
    save_website = website_entry.get()
    if len(save_website)==0:
        dont_leave = messagebox.showinfo(title="Opss",
                                            message="Please give a website")

    else:
        try:
            with open("data.json", mode="r") as data:
                # Reading old data
                data_file = json.load(data)
                if save_website in data_file:
                    email_data=data_file[save_website]["email"]
                    pass_data = data_file[save_website]["password"]

                info = messagebox.showinfo(title=save_website,
                                                message=f"Email: {email_data} \nPassword: {pass_data}")
                print(info)

        except FileNotFoundError:
            messagebox.showinfo(title="Opps",
                                   message=f"No Data File Found")
        except UnboundLocalError:
            messagebox.showinfo(title="Opps",
                                   message=f"No details for the website exits")
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def saving_data():
    # getting the data in entries
    save_website = website_entry.get()
    save_email = email_entry.get()
    save_pass = password_entry.get()
    new_data={
        save_website: {
            "email": save_email,
            "password": save_pass,
        }
    }
    # checking if the entries are filled, if not shows message to the user
    if len(save_website)==0 or len(save_pass) == 0:
        dont_leave = messagebox.showinfo(title="Opss",
                                       message="Please don't leave any fields empty!")
    # saving the data if the entries are filled
    else:
        try:
            with open("data.json", mode="r") as data:
                #Reading old data
                data_file = json.load(data)
                # Updating old data with new data
                data_file.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as data:
                #Saving the updating data (Careful, mode!)
                json.dump(new_data,data, indent=4)
        else:
            with open("data.json", mode="w") as data:
                #Saving the updating data (Careful, mode!)
                json.dump(data_file, data, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
# creating screen
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg=BG)

# creating canvas
canvas = Canvas(width=200,height=200, highlightthickness=0,background=BG)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1, row=0)

# putting labels
website = Label(justify="center")
website.config(text="Website:",bg=BG,fg=BLACK)
website.grid(column=0, row=1)

email = Label(justify="center")
email.config(text="Email/Username:",bg=BG,fg=BLACK)
email.grid(column=0, row=2)

password_label = Label(justify="center")
password_label.config(text="Password:",bg=BG,fg=BLACK)
password_label.grid(column=0, row=3)

# creating entries
website_entry = Entry(width=18,background=BG,highlightbackground=BG,justify="left",fg=BLACK)
website_entry.focus()
website_entry.grid(column=1,row=1)

email_entry = Entry(width=38,highlightbackground=BG,fg=BLACK)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0,"asligul@gmail.com")
email_entry.config(background=BG)

password_entry = Entry(width=18,justify="left")
password_entry.config(background=BG,highlightbackground=BG,fg=BLACK)
password_entry.grid(column=1,row=3)

# adding buttons and its functions
generate_pass = Button(text="Generate Password",background=BG,highlightthickness=1,
                       highlightbackground=BG,command=password_generator)
generate_pass.config(width=16)
generate_pass.grid(column=2, row=3)

add = Button(text="Add",background=BG,highlightthickness=1,highlightbackground=BG,command=saving_data)
add.config(width=36)
add.grid(column=1, row=4,columnspan=2)

search = Button(text="Search",background=BG,highlightthickness=1,highlightbackground=BG,command=search_machine)
search.config(width=16)
search.grid(column=2, row=1)


window.mainloop()