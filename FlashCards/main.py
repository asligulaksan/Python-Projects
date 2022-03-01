from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
words_to_learn = {}
french_text = ""
english_text = ""

# If there is the first time you are playing the game, please delete "words_to_lear.csv"
# Reading the data
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

# French word screen
def generate_french_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title,text = "Frech",fill="black")
    canvas.itemconfig(card_word, text=current_card["French"],fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, english_rep)

# English word that is the translation of French Word
def english_rep():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)

# If the word is known, removing it from the "words_to_learn.csv" file to not see in the next game
def is_known():
    data_dict.remove(current_card)
    data_file = pandas.DataFrame(data_dict)
    data_file.to_csv("data/words_to_learn.csv")
    generate_french_word()

# Creating the screen
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,english_rep)

# Placing the "right" button: if its pressed, the word is removed from "words_to_learn.csv" and new word is generated.
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0,bg=BACKGROUND_COLOR,command=is_known)
right_button.grid(row=1, column=1)

# Placing the "wrong" button: if its pressed, it is not removed from the "words_to_learn.csv" and new word is generated.
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0,bg=BACKGROUND_COLOR,command=generate_french_word)
wrong_button.grid(row=1, column=0)

if right_button:
    pass

# Creating the Canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400,150,text="",font=("Arial",40,"italic"),fill="black")
card_word = canvas.create_text(400,263,text=f"",font=("Arial",60,"bold"),fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


generate_french_word()

window.mainloop()



