import tkinter

# We create an object that defines a window
window = tkinter.Tk()

# We set a title to the window
window.title("My first GUI program")

# Minimun size of the window
window.minsize(width=500, height=300)
# padx and pady to add padding
window.config(padx=15, pady=15)


# Button clicked handler
def button_clicked():
    # my_label["text"] = "Buton got clicked"
    input_txt = input.get()
    my_label["text"] = input_txt
    print("I got clicked")


# Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))

# To pack the label to the window screen. This actually places the label to the screen
# my_label.pack(side="left")
# my_label.pack()

# Another layout manager, to show a component to the screen besides pack
# This method is so specific by specifying coordinates
# my_label.place(x=100)

# Another way to put elements into the screen is by using grid
# If i use grid in this element to be shown, i will need to use grid for all the elements, we cannot mix layout managers
my_label.grid(column=0, row=0)

# To configure properties of a component, we can do it in two ways:
# Get access the prop as it was in a dictionary
my_label["text"] = "New text"

# Use the config method to set the different properties
# padx and pady to add padding
my_label.config(text="New text", padx=50, pady=50)

# Button

button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)


# New Button

new_button = tkinter.Button(text="Click me 2", command=button_clicked)
new_button.grid(column=2, row=0)


# Entry
# To define an input text box
input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

# Return the input as a string
input.get()

# a loop to keep the window showing up without exiting until closed
window.mainloop()
