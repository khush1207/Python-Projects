from tkinter import *
import pandas
import random
from tkinter import simpledialog  # To ask user the input
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}

try:
    d = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/data_manager.csv")
    dict_data = data.to_dict(orient="records")
else:
    data = pandas.read_csv("data/data_manager.csv")


def flip_card():
    ans = simpledialog.askstring(title="ANSWER", prompt=f"What to do you think {random_word["Hindi"]} mean in English?")
    canvas.itemconfig(image, image=back_image)
    canvas.itemconfig(text_1, text="ENGLISH", fill="white")
    canvas.itemconfig(text_2, text=random_word["English"], fill="white")
    if ans == random_word["English"]:
        messagebox.showinfo(title="ANSWER", message="You got the answer correct!\nClick on ✔️")
        dict_data.remove(random_word)
        d = pandas.DataFrame(dict_data)
        d.to_csv("words_to_learn.csv")
    else:
        messagebox.showinfo(title="ANSWER", message="Uh..Ohh!! Better luck next time.\nCLick on ❌")


def change_word():
    global random_word
    random_word = random.choice(dict_data)
    canvas.itemconfig(text_1, text="HINDI", fill="black")
    canvas.itemconfig(text_2, text=f"{random_word["Hindi"]}", fill="black")
    canvas.itemconfig(image, image=front_image)
    window.after(1000, func=flip_card)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=510, height=330, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
image = canvas.create_image(255, 165, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)
text_1 = canvas.create_text(250, 100, text="", font=("Arial", 20, "italic"))
text_2 = canvas.create_text(250, 185, text="", font=("Arial", 40, "bold"))

tick_img = PhotoImage(file="images/right.png")
tick = Button(image=tick_img, highlightthickness=0, command=change_word)
tick.grid(column=1, row=2)
wrong_img = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_img, highlightthickness=0, command=change_word)
wrong.grid(column=0, row=2)

window.mainloop()
