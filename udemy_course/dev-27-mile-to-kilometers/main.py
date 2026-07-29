import tkinter

# We create an object that defines a window
window = tkinter.Tk()

# We set a title to the window
window.title("Mile to Kilometer Converter")

window.minsize(width=400, height=250)
window.config(padx=10, pady=10)

equal_label = tkinter.Label(text="is equal to", font=("Arial", 12))
equal_label.config(justify="right")
equal_label.grid(column=0, row=1, padx=(60, 0))

result_label = tkinter.Label(text="0", font=("Arial", 12))
result_label.config(justify="center")
result_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km", font=("Arial", 12))
km_label.config(justify="left", padx=0)
km_label.grid(column=2, row=1)

miles_label = tkinter.Label(text="Miles", font=("Arial", 12))
miles_label.config(justify="left", padx=5)
miles_label.grid(column=2, row=0)


input = tkinter.Entry(width=10, font=("Arial", 12))
input.insert(tkinter.END, string="0")
miles_label.config(pady=20)
input.grid(column=1, row=0)


def button_clicked():
    try:
        miles = float(input.get())
        kms = round(miles * 1.609344, 5) if miles > 0 else 0
        kms.config(text=f"{kms}")
    except Exception as err:
        result_label.config(text="0")
        print(err)


new_button = tkinter.Button(
    text="Calculate", font=("Arial", 12), command=button_clicked
)
new_button.grid(column=1, row=2, pady=(20, 0))


window.mainloop()
