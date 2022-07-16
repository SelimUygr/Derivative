from tkinter import *

from derivative import deriv
from drawDerivative import draw

# Setting up the gui window
window = Tk()
window.maxsize(600,200)
window.minsize(600,200)
window.title("Derivative of Polynomal")

# Label of the entry
label = Label(window,text="Example input: 4*x**4 + 3*x**2 + 2*x**4 + 3*x + 1")
label.grid(row=0,column=0,pady=(30,5),padx=(80,10))

# Getting the input(entry)
text_input = Entry(window)
text_input.grid(row=0,column=1,pady=(30,5))

# Create function for button click
def calculate():
    function_input = text_input.get()
    result = deriv(function_input)
    Label(window,text="Derivitive of the function is: ").grid(row=2,column=0,sticky=E,pady=(20,0))
    Label(window,text=result).grid(row=2,column=1,sticky=W,pady=(20,0))
    print(result)
    draw(result)

# Create the button for calculation to start
calculate_button = Button(window,text="Calculate",command=calculate,width=10)
calculate_button.grid(row=1,column=1)

# Create button for exit program
exit_button = Button(window,text="Exit",command=window.destroy,width=10)
exit_button.grid(row=1,column=0)
window.mainloop()


