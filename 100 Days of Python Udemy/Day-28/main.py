import tkinter as tk
import os
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
script_dir = os.path.dirname(__file__) # the dir of this script

class Pomodoro():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Pomodoro')
        self.root.config(padx=100, pady=50, bg=YELLOW)
        self.title()
        self.tomato()
        self.start()
        self.reset()
        self.check_mark()
                    
    def title(self):
        self.title = tk.Label(self.root, text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, 'bold'))
        self.title.grid(row=0, column=1)

    def tomato(self):
        self.photo = tk.PhotoImage(file=os.path.join(script_dir, "tomato.png"))
        self.canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.canvas.create_image(100, 112, image=self.photo)
        self.canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 28, 'bold'))
        self.canvas.grid(row=1, column=1)


    def start(self):
        self.start = tk.Button(text='Start').grid(row=2, column=0)

    def reset(self):
        self.reset = tk.Button(text='Reset').grid(row=2, column=2)

    def check_mark(self):
        self.check = tk.Label(self.root, text='✔', bg=YELLOW, fg=GREEN)
        self.check.grid(row=3, column=1)





        


app = Pomodoro()
app.root.mainloop()





# window.mainloop()

