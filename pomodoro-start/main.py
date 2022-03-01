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
reps = 0
timerr = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timerr)
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text,text="00.00")
    check.config(text="")
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60
    reps +=1
    if reps % 2 == 1:
        count_down(work)
        timer.config(text="Work",fg=GREEN,background=YELLOW)
    elif reps % 8 == 0:
        count_down(long)
        timer.config(text="Break", fg=RED, background=YELLOW)
    elif reps % 2 == 0:
        count_down(short)
        timer.config(text="Break", fg=PINK, background=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/ 60)
    count_sec = count % 60
    if count_sec==0:
        count_sec = "00"
    for num in range(10):
        if count_sec == num:
            count_sec = "0" + str(num)

    canvas.itemconfig( timer_text , text=f"{count_min}:{count_sec}")

    if count > 0:
        global timerr
        timerr = window.after(1000, count_down,count-1)
    else:
        start_timer()
        mark =""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += "✔"
        check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)

timer = Label(font=(FONT_NAME, 40, "normal"))
timer.config(text="Timer",fg=GREEN,background=YELLOW)
timer.grid(column=1, row=0)

check = Label(font=(FONT_NAME, 20, "normal"))
check.config(fg=GREEN,background=YELLOW)
check.grid(column=1, row=3)

start_buton = Button(text="Start",background=YELLOW,highlightthickness=0,highlightbackground=YELLOW)
start_buton.config(command=start_timer)
start_buton.grid(column=0, row=2)

reset_buton = Button(text="Reset",background=YELLOW,highlightthickness=0,highlightbackground=YELLOW)
reset_buton.config(command=reset_timer)
reset_buton.grid(column=2, row=2)



window.mainloop()