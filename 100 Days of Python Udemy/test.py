# def add(*args):
#     arguments_list = [x for x in args]
#     return sum(arguments_list)

# class Model:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get('make')  # Use get so if argument does not exist returns none.
#         self.model = kwargs.get('model')

# new_car = Model(make='Nissan')
# print(new_car.model) 
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
root.mainloop()