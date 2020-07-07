from tkinter import *

#Program side
expression = ""




def press(num):
    global expression
    expression = expression + str(num)

    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set('error')
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")





#Front_end side code
if __name__ == "__main__":
    window = Tk()
    window.title("Calculator")
    window.configure(bg='#CEDDDB')
    window.geometry("376x250")
    equation = StringVar()

    input_field = Entry(window,textvariable= equation)
    input_field.grid(columnspan=6, ipadx=150)
    equation.set('Enter...')
    #Buttons
    button_1 = Button(window,command=lambda:press(1),text="1",width=10,bg='#CEDDDB')
    button_2 = Button(window,command=lambda : press(2),text = '2',width=10,bg='#CEDDDB')
    button_3 = Button(window,command=lambda :press(3),text = '3',width = 10,bg='#CEDDDB')
    button_add = Button(window,command= lambda :press('+'),text = '+',width = 7,height = 3,bg='#6E5057')
    button_4 = Button(window,command = lambda :press(4),text = '4', width = 10,bg='#CEDDDB')
    button_5 = Button(window,command = lambda :press(5),text = '5',width = 10,bg='#CEDDDB')
    button_6 = Button(window,command = lambda :press(6),text = '6',width = 10,bg='#CEDDDB')
    button_differance = Button(window,command = lambda :press('-'),text = '-',width = 7,height = 3,bg='#6E5057')
    button_7 = Button(window,command= lambda :press(7),text= '7',width=10,bg='#CEDDDB')
    button_8 = Button(window,command=lambda :press(8),text='8',width = 10,bg='#CEDDDB')
    button_9 = Button(window,command=lambda :press(9),text= '9',width= 10,bg='#CEDDDB')
    button_product = Button(window,command=lambda :press('*'),text='x',width=7,height=3,bg='#6E5057')
    button_0 = Button(window,command=lambda :press(0),text='0',width=10,bg='#CEDDDB')
    button_division = Button(window,command=lambda :press('/'),text='÷',width=7,height=3,bg='#6E5057')
    button_equation = Button(window,command=lambda :equalpress(),text = '=',width = 10,height = 3,bg='#C33D3D')
    button_clear = Button(window,command=lambda :clear(),text='C',width=10,height=3,bg='#393838')



#grid
    button_1.grid(row=1,column=0)
    button_2.grid(row=1,column=1)
    button_3.grid(row = 1, column = 2)
    button_add.grid(row = 1, column = 3)
    button_4.grid(row = 2, column = 0)
    button_5.grid(row = 2,column = 1)
    button_6.grid(row=2, column = 2)
    button_differance.grid(row=2,column= 3)
    button_7.grid(row=3, column = 0)
    button_8.grid(row=3,column=1)
    button_9.grid(row=3,column=2)
    button_product.grid(row=3,column=3)
    button_0.grid(row=4,column=0)
    button_division.grid(row=4,column= 3)
    button_equation.grid(row=4,column = 1)
    button_clear.grid(row=4,column=2)


window.mainloop()