import tkinter

def click_message():
    first_label.config(text=user.get())


window = tkinter.Tk()
window.title('First GUI with tkinter')
window.minsize(width=500, height=300)
window.config(padx=15, pady=15)

# label widget
first_label = tkinter.Label(text="Hello, World!", fg="black", bg="white").grid(column=0, row=0)


# button widget
button = tkinter.Button(text='message', command=click_message).grid(column=1, row=1)

# button number 2 widget
button_2 = tkinter.Button(text='new button').grid(column=2, row=0)

# entry component widget
user = tkinter.Entry()
user.get()
user.grid(column=3, row=2)


window.mainloop()