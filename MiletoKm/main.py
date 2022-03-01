from tkinter import *
# creating the screen
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20) # adding padding

#Entry
input = Entry(width=10)
input.grid(column=1,row=0)

#Labels
miles = Label(font=("Arial", 12, "normal"))
miles.config(text="Miles")
miles.grid(column=2, row=0)

km = Label(font=("Arial", 12, "normal"))
km.config(text="Km")
km.grid(column=2, row=1)

equal = Label(font=("Arial", 12, "normal"))
equal.config(text="is equal to")
equal.grid(column=0, row=1)

answer = Label(font=("Arial", 12, "normal"))
answer.config(text="0")
answer.grid(column=1, row=1)

#Button
def miles_to_km():
    mile = float(input.get())
    kilometer = mile*1.609
    answer.config(text=f"{kilometer}")

button = Button(text="Calculate",command=miles_to_km)
button.grid(column=1,row=2)


window.mainloop()