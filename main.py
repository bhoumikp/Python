from random import *
from tkinter import *
from tkinter import messagebox
from pyperclip import *
import json


# --------------------------------------*Search*------------------------------------------- #

def search_password():
	search_website = websiteEntry.get()
	search_username = emailEntry.get()
	if search_website == '' or search_username == '':
		messagebox.showinfo(title='Oops!', message='Please Enter Website and Email/Username.')
	else:
		try:
			with open('data.json', 'r') as search_file:
				search_data = json.load(search_file)
		except FileNotFoundError:
			messagebox.showinfo(title='Error!', message='No Data File Found.')
		except:
			messagebox.showinfo(title='Error!', message='Data file is empty! Please add password first.')
		else:
			try:
				found_password = [search_data[web]['Password'] for web in search_data if web == search_website and search_data[web]['Username'] == search_username][0]
			except IndexError:
				messagebox.showinfo(title='Error!', message=f'No details for {search_website} exists.')		
			else:
				messagebox.showinfo(title=search_website, message=f'Email/Username: {search_username}\nPassword: {found_password}')
				copy(found_password)
				websiteEntry.delete(0, END)
				emailEntry.delete(0, END)
				passwordEntry.delete(0, END)
				websiteEntry.focus()				

# --------------------------------------*Generate Password*-------------------------------- #

def generate_password():
	alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

	random_alphabets = [choice(alphabets) for _ in range(randint(8, 10))]
	random_symols = [choice(symbols) for _ in range(randint(2, 4))]
	random_numbers = [choice(numbers) for _ in range(randint(2, 4))]
	
	passtring = random_numbers + random_symols + random_alphabets
	shuffle(passtring)

	passwordEntry.delete(0, END)
	passwordEntry.insert(0, ''.join(passtring))

	copy(passwordEntry.get())

# --------------------------------------*Add Passwords*------------------------------------ #

def add_password():
	website = websiteEntry.get()
	username = emailEntry.get()
	password = passwordEntry.get()

	info = {website: {"Username": username, "Password": password}}

	if website == '' or username == '' or password == '':
		messagebox.showwarning(title='Oops!', message='Please make sure you haven`t left any fields empty and try again. ')
	else:
		try:
			with open('data.json', 'r') as read_file:
				json_data = json.load(read_file)
		except:
			with open('data.json', 'w') as write_file:
				json.dump(info, write_file, indent=4)
		else:
			json_data.update(info)
			with open('data.json', 'w') as write_file:
				json.dump(json_data, write_file, indent=4)
		finally:
			messagebox.showinfo(title='Congratulations!', message=f'Password added successfully.\nWebsite: {website}\nEmail/Username: {username}\nPassword: {password}')
			websiteEntry.delete(0, END)
			emailEntry.delete(0, END)
			passwordEntry.delete(0, END)
			websiteEntry.focus()

# --------------------------------------*Style*-------------------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title('Password Manager')


canvas = Canvas(width=200, height=200)
logoFile = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logoFile)
canvas.grid(row=0, column=0, columnspan=3)


# Labels
websiteLabel = Label(text='Website Name: ')
websiteLabel.grid(row=1, column=0)

emailLabel = Label(text='Email/Username: ')
emailLabel.grid(row=2, column=0)

passwordLabel = Label(text='Password: ')
passwordLabel.grid(row=3, column=0)


#Entries
websiteEntry = Entry(width=32)
websiteEntry.grid(row=1, column=1, pady=5)
websiteEntry.focus()

emailEntry = Entry(width=51)
emailEntry.grid(row=2, column=1, columnspan=2)

passwordEntry = Entry(width=32)
passwordEntry.grid(row=3, column=1)


# Buttons
generateBtn = Button(text='Generate', width=15, command=generate_password)
generateBtn.grid(row=3, column=2)

searchBtn = Button(text='Search', width=15, command=search_password)
searchBtn.grid(row=1, column=2)

addBtn = Button(text='Add', width=48, command=add_password)
addBtn.grid(row=4, column=1, columnspan=2, pady=5)


window.mainloop()
