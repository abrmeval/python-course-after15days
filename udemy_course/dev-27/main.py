import tkinter

# We create an object that defines a window
window = tkinter.Tk()

# We set a title to the window
window.title("My first GUI program")

# Minimun size of the window
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))

# To pack the label to the window screen. This actually places the label to the screen
# my_label.pack(side="left")
my_label.pack()

# To configure properties of a component, we can do it in two ways:
# Get access the prop as it was in a dictionary
my_label["text"] = "New text"
# Use the config method to set the different properties
my_label.config(text="New text")


# Button
def button_clicked():
    # my_label["text"] = "Buton got clicked"
    input_txt = input.get()
    my_label["text"] = input_txt
    print("I got clicked")


button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()


# Entry 
# To define an input text box
input = tkinter.Entry(width=10)
input.pack()

# Return the input as a string
input.get()

# a loop to keep the window showing up without exiting until closed
window.mainloop()
