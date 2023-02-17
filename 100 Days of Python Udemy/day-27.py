import tkinter

window = tkinter.Tk()
window.title('First GUI with tkinter')
window.minsize(width=500, height=300)

first_label = tkinter.Label(text="Hello, World!", fg="black", bg="white")
first_label.pack()

# button 
def click_message():
    # first_label.config(text=f'You Click Me! - count: {i[0]}')
    first_label.config(text=user.get())
    

button = tkinter.Button(text='message', command=click_message)
button.pack()

# entry component
user = tkinter.Entry()
user.get()
user.pack()

window.mainloop()