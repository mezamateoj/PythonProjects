import tkinter as tk

class MyApp():
    def __init__(self):
        self.root = tk.Tk()
        self.root.minsize(width=300, height=100)
        self.root.title('Mile to Km Converter')
        self.boiler_text()
        self.entry_user()
        self.text_display()
        self.button_action()
    
    def converter(self):
        value = float(self.entry.get())
        self.km = value * 1.609
        self.text.config(text=f'{round(self.km)}')


    def boiler_text(self):
        self.l1 = tk.Label(self.root, text="Is equal to").grid(row=1, column=0, padx=10)
        self.l2 = tk.Label(self.root, text="Miles").grid(row=0, column=2)
        self.l3 = tk.Label(self.root, text="Km").grid(row=1, column=2, padx=10, pady=5)

    def entry_user(self):
        self.entry = tk.Entry(width=15)
        self.entry.grid(row=0, column=1, padx=20, pady=5)

        
        
    def text_display(self):
        self.text = tk.Label(text='0')
        self.text.grid(row=1, column=1)



    def button_action(self):
        self.button = tk.Button(text='Calculate', command=self.converter).grid(row=2, column=1)



app = MyApp()
app.root.mainloop()