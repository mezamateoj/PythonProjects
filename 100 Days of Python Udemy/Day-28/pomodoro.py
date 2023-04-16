import tkinter as tk

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")
        
        self.timer_label = tk.Label(master, text="25:00", font=("Arial", 30))
        self.timer_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.grid(row=1, column=0, pady=10)
        
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer, state="disabled")
        self.stop_button.grid(row=1, column=1, pady=10)
        
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer, state="disabled")
        self.reset_button.grid(row=1, column=2, pady=10)
        
        self.timer_running = False
        self.minutes = 25
        self.seconds = 0
        self.timer_id = None
        
    def start_timer(self):
        self.timer_running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.reset_button.config(state="disabled")
        self.update_timer()
        
    def stop_timer(self):
        self.timer_running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.reset_button.config(state="normal")
        if self.timer_id:
            self.master.after_cancel(self.timer_id)
        
    def reset_timer(self):
        self.timer_running = False
        self.minutes = 25
        self.seconds = 0
        self.timer_label.config(text="25:00")
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.reset_button.config(state="disabled")
        if self.timer_id:
            self.master.after_cancel(self.timer_id)
        
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
            self.timer_label.config(text=time_string)
            self.timer_id = self.master.after(1000, self.update_timer)
        
root = tk.Tk()
my_timer = PomodoroTimer(root)
root.mainloop()
