from tkinter import *

#Front_end side code

window = Tk()
window.title("Calculator")
window.configure(bg='#CEDDDB')
window.geometry("400x450")

input_field = Entry(window,)
button_1 = Button(window,command=lambda:click(),text="1",width=10)
input_field.grid(columnspan=6,ipadx=150)

button_1.grid()


expression=""
def click():
    print("Button clicked")

x=click()
window.mainloop()