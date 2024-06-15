from tkinter import *
from tkinter import ttk
import time

# Constants

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
def count_down(count):
    if count > 0:
        window.after(1000, count_down, count - 1)

# UI

window = Tk()
window.title("Pomodoro")
window.geometry("500x440")
window.config(padx=75, pady=50, bg=YELLOW)


# Tomato image / timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Start button
start_button = ttk.Button(text="Start")
start_button.grid(column=0, row=2)

# Reset button
reset_button = ttk.Button(text="Reset")
reset_button.grid(column=2, row=2)

# Title
title = ttk.Label(text="Timer", font=(FONT_NAME, 30))

title.configure(background=YELLOW)
title.grid(column=1, row=0)
title.configure(padding=10)




window.mainloop()
