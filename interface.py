from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from behavior import check, register


def main_window(): 
	''' lauches main window '''
	root = Tk()
	root.title("Login system")
	root.geometry("450x350")

	def to_sign_in():
		root.destroy()
		sign_in_window()

	def to_sign_up():
		root.destroy()
		sign_up_window()

	sign_in = ttk.Button(root, text = "Sign in", command = to_sign_in)
	sign_in.place(x = 174, y = 225)

	sign_up = ttk.Button(root, text = "Sign up", command = to_sign_up)
	sign_up.place(x = 174, y = 175)

	welcome_label = ttk.Label(root, text = "Welcome!")
	welcome_label.config(font=("Courier", 44))
	welcome_label.place(x = 90, y = 75)

	root.mainloop()


def sign_in_window():
	''' lauches sign in window '''
	root = Tk()
	root.title("Sign in")
	root.geometry("450x350")

	username_input=Entry(root)
	username_input.place(x = 176, y = 135)
	
	password_input=Entry(root, show="*")
	password_input.place(x = 176, y = 185)

	def get_pass_and_username():
		username = username_input.get()
		password = password_input.get()
		if check(username, password) == True:
			root = Tk()
			root.title("Congrats!")
			root.geometry("450x350")
			welcome_label = ttk.Label(root, text = "You are inside!")
			welcome_label.config(font=("Courier", 24))
			welcome_label.place(x = 77, y = 125)

	def congratulations_window():
		get_pass_and_username()
		root.destroy()

	label_main = ttk.Label(root, text = "ACCESS TO YOUR ACCOUNT")
	label_main.config(font=("Courier", 14))
	label_main.place(x = 102, y = 70)

	label_username = ttk.Label(root, text = "Username")
	label_username.config(font=("Courier", 12))
	label_username.place(x = 80, y = 136)

	label_password = ttk.Label(root, text = "Password")
	label_password.config(font=("Courier", 12))
	label_password.place(x = 80, y = 188)

	user_pass_get = ttk.Button(root, text = "Sign in", command = congratulations_window)
	user_pass_get.place(x = 189, y = 252)

	root.mainloop()


def sign_up_window():
	''' lauches registration window '''
	root = Tk()
	root.title("Sign up")
	root.geometry("470x350")

	label_main = ttk.Label(root, text = "CREATE NEW ACCOUNT")
	label_main.config(font=("Courier", 14))
	label_main.place(x = 132, y = 50)

	username_input=Entry(root)
	username_input.place(x = 180, y = 110)

	label_username = ttk.Label(root, text = "Username")
	label_username.config(font=("Courier", 12))
	label_username.place(x = 80, y = 111)
	
	password_input=Entry(root, show="*")
	password_input.place(x = 180, y = 150)

	label_password= ttk.Label(root, text = "Password")
	label_password.config(font=("Courier", 12))
	label_password.place(x = 80, y = 151)

	password_input_confirm=Entry(root, show="*")
	password_input_confirm.place(x = 180, y = 190)

	label_confirm= ttk.Label(root, text = "Confirm")
	label_confirm.config(font=("Courier", 12))
	label_confirm.place(x = 80, y = 192)
	
	def get_pass_and_username():
		username = username_input.get()

		password = password_input.get()
		confirm = password_input_confirm.get()

		if register(username, password, confirm) == True:
			root = Tk()
			root.title("Status")
			root.title("Congrats!")
			root.geometry("450x350")
			welcome_label = ttk.Label(root, text = "Registered!")
			welcome_label.config(font=("Courier", 34))
			welcome_label.place(x = 77, y = 125)
		else:
			root = Tk()
			root.title("Something goes wrong!")
			root.geometry("450x350")
			welcome_label = ttk.Label(root, text = "Try again!")
			welcome_label.config(font=("Courier", 34))
			welcome_label.place(x = 77, y = 125)
	user_pass_get = ttk.Button(root, text = "Sign up", command = get_pass_and_username)
	user_pass_get.place(x =190, y=258)	
	
	root.mainloop() 


main_window()


