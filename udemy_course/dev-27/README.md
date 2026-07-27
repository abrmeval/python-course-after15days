# Tkinter

It is a python package tthat helps buildiing GUIs. It is Python's de facto standard GUI.

```python
import tkinter

# We create an object that defines a window
window = tkinter.Tk()

# We set a title to the window
window.title("My first GUI program")

#Minimun size of the window
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))

 # To pack the label to the window screen. This actually places the label to the screen
my_label.pack()



# a loop to keep the window showing up without exiting until closed
window.mainloop()
```

# Advanced python arguments

## Keyword arguments

```python
def my_func(a, b, c)
    pass

my_func(c=3, a=1, b=4)
```

## Default values

```python
def my_func(a =1, b=2, c=3)
    pass

my_func(b=5)
```

## Unlimited arguments

The **\*** tells python to accept any number of arguments.
You would iterate through the args to access every value.
**args** will hold a **tuple** with n number of values.

```python
def my_func(*args)
    for n in args:
        print(n)

my_func(2, 5, 6, 7)
```

## \*\*kwargs: Many keyworded arguments

The **\*\*** tells python to accept any number of arguments.
You would iterate through the kwargs to access every value or access one value by key.
**kwargs** will hold a **dictionary** with n number of values.

```python
def my_func(**kwargs)
    print(kwargs["add"])
    print(kwargs["multiply"])

    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)

my_func(add=3, multiply=5)

#-------------------------------------------

def calculate(n, **kwargs):
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5) # -> 25

#-------------------------------------------
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.make = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.model) # -> None
```
