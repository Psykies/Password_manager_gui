from tkinter import *
from tkinter import messagebox
import random
import json


# -----------------------------------Create Password------------------------------------
#for generaing a random password contaning combiabtion of letter(big or small),symbol and nnumber
def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letter = random.randint(5, 8)
    nr_number = random.randint(2, 4)
    nr_symbol = random.randint(2, 4)

    # e.g. 5 letter, 2 symbol, 2 number = JdyuE&!91
    generated_password = ""

    for letter in range(nr_letter):
        generated_password += random.choice(letters)

    for symbol in range(nr_symbol):
        generated_password += random.choice(symbols)

    for number in range(nr_number):
        generated_password += random.choice(numbers)

    output_password = ''.join(random.sample(generated_password, len(generated_password)))
    password_input.insert(0,output_password)


# ------------------------------------Save Password--------------------------------------
#function to save the contentns of the website name ,emailand password
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email" : email,
            "password": password

        }
    }
    #to check if the input is empty
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please don't leave any field empty!")
    #else store he data while checking for storing file is there or not with data also
    else:
        try:
            with open("data.json", "r") as data_file:
                #reading the old data and loading it as a python dict by using json.load
                data = json.load(data_file)

        #exception if there is no data.json file
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                #craetes a json file from the dic with json.dump
                json.dump(new_data, data_file, indent=4)

        # exception if the json file does not conataina ny data
        except json.JSONDecodeError :
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        #if everything is ok and w need to update new password for different site
        else:
            with open("data.json", "w") as data_file:
            # updating the old data with new data
                data.update(new_data)
            #wrting in the new data
                json.dump(data, data_file, indent=4)

        #clearning the text box area for website,email and password
        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)

# --------------------------------------Search-------------------------------------------
#function to search the email and password through website data provided
def search():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="The password file is missing")

    except json.JSONDecodeError:
        messagebox.showinfo(title="Error", message="There password file is Empty")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Search Result", message=f"Website : {website}\n"
                                                               f"Email : {email}\n"
                                                               f"Password : {password}")
        else:
            messagebox.showinfo(title="Error", message=f"There data is not store for {website}")
    finally:
        website_input.delete(0, END)



# --------------------------------------UI Design----------------------------------------

window = Tk()
window.title("Password Manager")
window.config(padx=150, pady=120)

# Canvas setup
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, columnspan=2)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry
website_input = Entry(width=16)
website_input.grid(row=1, column=1)
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=16)
password_input.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width = 15 , command=search)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=create_password)
generate_password_button.grid(row=3, column=2)
add_password_button = Button(text="Add", width=30, command=save)
add_password_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
