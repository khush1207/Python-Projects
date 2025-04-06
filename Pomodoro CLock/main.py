from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = "None"
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer")
    label2.config(text="")
    global rep
    rep = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global rep
    rep += 1
    work = WORK_MIN * 60
    s_break = SHORT_BREAK_MIN * 60
    l_break = LONG_BREAK_MIN * 60
    if rep % 8 == 0:
        label1.config(text="Break", fg=RED)
        count_down(l_break)
    elif rep % 2 == 0:
        label1.config(text="Break", fg=PINK)
        count_down(s_break)
    else:
        label1.config(text="Work time", fg=GREEN)
        count_down(work)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec in range(0, 10):
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        r = [2, 4, 6]
        for n in r:
            marks = "✔"
        label2.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Timer")
window.config(padx=50, pady=50, bg=YELLOW)

label1 = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
label1.grid(column=2, row=0)
label2 = Label(fg=PINK, bg=YELLOW)
label2.grid(column=2, row=3)

button1 = Button(text="Start", command=start_timer)
button1.grid(column=0, row=2)
button2 = Button(text="Reset", command=reset)
button2.grid(column=3, row=2)

# Canvas Widget - to lay things one on other
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# high_light_thickness is used to remove the border of the image
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
canvas.grid(column=2, row=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

window.mainloop()
