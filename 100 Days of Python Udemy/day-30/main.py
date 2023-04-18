# making the password manager work with the Json database
import tkinter as tk
from tkinter import messagebox
import os
from generator import password
import json

script_dir = os.path.dirname(__file__) # the dir of this script

class PasswordManager():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Password Manager')
        self.root.config(padx=50, pady=50)
        self.canvas()
        self.website()
        self.email()
        self.password()
        self.add()
        

    def canvas(self):
        self.photo = tk.PhotoImage(file=os.path.join(script_dir, "logo.png"))
        self.canvas = tk.Canvas(width=200, height=200)
        self.canvas.create_image(100, 100, image=self.photo)
        self.canvas.grid(row=0, column=1)

    def website(self):
        self.website_label = tk.Label(self.root, text='Website: ')
        self.website_label.grid(row=1, column=0)

        self.website_entry = tk.Entry(self.root, width=35)
        self.website_entry.grid(row=1, column=1)
        self.website_entry.focus()

        self.search_button = tk.Button(self.root, text='Search', width=14, command=self.search_data)
        self.search_button.grid(row=1, column=2)

    def email(self):
        self.email_label = tk.Label(self.root, text='Email/Username: ')
        self.email_label.grid(row=2, column=0)

        self.email_entry = tk.Entry(self.root, width=35)
        self.email_entry.grid(row=2, column=1)
        self.email_entry.insert(0, 'mezamateoj@gmail.com')

    def password(self):
        self.password_label = tk.Label(self.root, text='Password: ')
        self.password_label.grid(row=3, column=0)

        self.password_entry = tk.Entry(self.root, width=35)
        self.password_entry.grid(row=3, column=1)

        self.generate_button = tk.Button(self.root, text='Generate Password', command=self.generate_password)
        self.generate_button.grid(row=3, column=2)

    def generate_password(self):
        self.password_entry.delete(0, 'end')
        self.password_entry.insert(0, password())

    def add(self):
        self.pop = False
        self.add_button = tk.Button(self.root, text='Add', width=45, command=self.save)
        self.add_button.grid(row=4, column=1, columnspan=2)
        

    # make a function to save the data to a file
    def save(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        new_data = {website:
                        {'email': email,
                        'password': password
                        }
                    }
        # create a messagebox to confirm the data
        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title='Oops', message='Please make sure you haven\'t left any fields empty')
        else:
            is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email} \nPassword: {password} \nSave?')
            if is_ok:
                try:
                    with open(r'C:\Users\mezam\Desktop\password_data.json', 'r') as data_file:
                        # read old data
                        data = json.load(data_file)
            
                except FileNotFoundError:
                    with open(r'C:\Users\mezam\Desktop\password_data.json', 'w') as data_file:
                        # save updated data
                        json.dump(new_data, data_file, indent=4)
                        self.clear_text()
                else:
                    data.update(new_data)

                    with open(r'C:\Users\mezam\Desktop\password_data.json', 'w') as data_file:
                        # save updated data
                        json.dump(data, data_file, indent=4)
                        self.clear_text()
            else:
                self.clear_text()

          
    def clear_text(self):
        # self.email_entry.delete(0, 'end')
        self.password_entry.delete(0, tk.END)
        self.website_entry.delete(0, tk.END)

    def search_data(self):
        website = self.website_entry.get()
        try:
            with open(r'C:\Users\mezam\Desktop\password_data.json', 'r') as data_file:
                # read old data
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title='Error', message='No Data File Found')
        else:
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title=website, message=f'Email: {email} \nPassword: {password}')
            else:
                messagebox.showinfo(title='Error', message=f'No details for {website} exists')




app = PasswordManager()
app.root.mainloop()