
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	nr_letters = randint(8, 10)
	nr_symbols = randint(2, 4)
	nr_numbers = randint(2, 4)

	password_lettes = [choice(letters) for _ in range(nr_letters)]
	password_symbols = [choice(symbols) for _ in range(nr_symbols)]
	password_numbers = [choice(numbers) for _ in range(nr_numbers)]

	password_list = password_symbols + password_lettes + password_numbers
	shuffle(password_list)

	password = ''.join(password_list)

	password_entry.insert(0, password)
	pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
	website = website_entry.get()
	password = password_entry.get()
	email = Email_entry.get()
	new_data = {
	website : {
		'email': email,
		'password': password
	}
	}
	if len(website) == 0 or len(password) == 0:
		messagebox.askokcancel(message='One or more of the entries was not entered')

	else:
		try:
			with open('data.json', 'r') as file:
				data = json.load(file)
				data.update(new_data)
		except:
			with open('data.json', 'w') as file:
				json.dump(new_data, file, indent=4)
		else:
			with open('data.json', 'w') as file:
				json.dump(data, file, indent=4)

		finally:
			website_entry.delete(0, 'end')
			password_entry.delete(0, 'end' )
			messagebox.showinfo(message=f'Your {website} entries saved successfully')


def search():
	website = website_entry.get()
	with open('data.json', 'r') as file:
		data = json.load(file)
		for key, value in data.items():
			if key.lower() == website.lower():
				email = value['email']
				password = value['password']
				messagebox.showinfo(message=f'Your website details are\nwebsite:  {key}\nEmail: {email}\nPassword: {password}')
			else:
				messagebox.showinfo(message='Entry does not exit')

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)

image = PhotoImage(file='logo.png')
canvas_image = canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1,  row=1)
website_entry.focus()

search_button = Button(text='search', width=21, command=search)
search_button.grid(column=2, row=1)


Email_label = Label(text="Email/Username:")
Email_label.grid(column=0, row=2)

Email_entry = Entry(width=43)
Email_entry.grid(column=1, columnspan=2, row=2)
Email_entry.insert(0, 'dummy@gmail.com')

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

gen_button = Button(text='Generate Password', width=21, command=gen_password)
gen_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=add)
add_button.grid(column=1, columnspan=2, row=4)



window.mainloop()
