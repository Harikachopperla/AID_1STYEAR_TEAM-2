from tkinter import *

users = {"harika": "12345"}  

def login():
    user = username_entry.get()
    pwd = password_entry.get()
    
    if user in users and users[user] == pwd:
        message_label.config(text="Login Successful", fg="green")
    else:
        message_label.config(text="Invalid Username or Password", fg="red")

def register():
    user = username_entry.get()
    pwd = password_entry.get()

    if user == "" or pwd == "":
        message_label.config(text="Enter both username and password", fg="orange")
    elif user in users:
        message_label.config(text="Username already exists", fg="red")
    else:
        users[user] = pwd
        message_label.config(text="Account Created! You can now Login", fg="green")

root = Tk()
root.title("Login Form")
root.geometry("300x200")

username_label = Label(root, text="Username:")
username_label.pack(pady=5)
username_entry = Entry(root)
username_entry.pack(pady=5)

password_label = Label(root, text="Password:")
password_label.pack(pady=5)
password_entry = Entry(root, show="*")
password_entry.pack(pady=5)

button_frame = Frame(root)
button_frame.pack(pady=10)

register_button = Button(button_frame, text="Don't have an account?", command=register, bg="#007BFF", fg="white", activebackground="#0056b3")
register_button.grid(row=0, column=0, padx=5)

login_button = Button(button_frame, text="Login", command=login, bg="#007BFF", fg="white", activebackground="#0056b3")
login_button.grid(row=0, column=1, padx=5)

message_label = Label(root, text="")
message_label.pack()

root.mainloop()