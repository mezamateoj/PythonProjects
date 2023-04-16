import datetime
import tkinter as tk
import os
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


script_dir = os.path.dirname(__file__) # the dir of this script

class Pomodoro():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Pomodoro')
        self.root.config(padx=100, pady=50, bg=YELLOW)
        self.title()
        self.tomato()
        # self.start()
        # self.reset()
        self.check_mark()

        # self.timer_label = tk.Label(self.root, text="25:00", font=(FONT_NAME, 22, 'bold'),bg=RED)
        # self.timer_label.grid(row=1, column=1, columnspan=3, pady=10)
        
    
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.grid(row=2, column=0, pady=10)
        
        
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_timer, state="disabled")
        self.stop_button.grid(row=2, column=1, pady=10)
        
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_timer, state="disabled")
        self.reset_button.grid(row=2, column=2, pady=10)

        self.timer_running = False
        self.minutes = 25
        self.seconds = 0
        self.timer_id = None
                        
    def title(self):
        self.title = tk.Label(self.root, text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, 'bold'))
        self.title.grid(row=0, column=1)

    def tomato(self):
        self.photo = tk.PhotoImage(file=os.path.join(script_dir, "tomato.png"))
        self.canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.canvas.create_image(100, 112, image=self.photo)
        self.change = self.canvas.create_text(100, 130, text='25:00', fill='white', font=(FONT_NAME, 22, 'bold'))
        self.canvas.grid(row=1, column=1)


    def check_mark(self):
        self.check = tk.Label(self.root, text='✔', bg=YELLOW, fg=GREEN)
        self.check.grid(row=3, column=1)

    def start_timer(self):
        self.timer_running = True
        self.start_button #.config(state="disabled")
        self.stop_button.config(state="normal")
        self.reset_button #.config(state="disabled")
        self.update_timer()

    def stop_timer(self):
        self.timer_running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.reset_button.config(state="normal")
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

    def reset_timer(self):
        self.timer_running = False
        self.minutes = 25
        self.seconds = 0
        self.canvas.itemconfigure(self.change, text='25:00')
        # self.timer_label.config(text="25:00")
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.reset_button.config(state="disabled")
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

    def update_timer(self):
        if self.timer_running:
            if self.minutes == 0 and self.seconds == 0:
                self.timer_running = False
                self.start_button.config(state="normal")
                self.stop_button.config(state="disabled")
                self.reset_button.config(state="normal")
                return
            elif self.seconds == 0:
                self.minutes -= 1
                self.seconds = 59
            else:
                self.seconds -= 1
            time_string = "{:02d}:{:02d}".format(self.minutes, self.seconds)
            self.canvas.itemconfigure(self.change, text=time_string)
            self.timer_id = self.root.after(1000, self.update_timer)


app = Pomodoro()
app.root.mainloop()

