import random
import requests
import tkinter as tk
import tkinter.font
from tkinter import font
from tkinter import ttk

# Anna did all the API code for converting the currency and choosing what currencies to covert to and from
Token = "y5wKbpbovhejqeK3H7wP14Mxi27wr0jxbvZMGqRk"
url = "https://api.currencyapi.com/v3/latest?apikey=y5wKbpbovhejqeK3H7wP14Mxi27wr0jxbvZMGqRk".format(Token)

res = requests.get(url)
data = res.json()


def write_text():
    label.config(text="")


def indropdown_pressed(event):
    initem = dropdownin.get()
    print("Dropdown pressed. Selected item:", initem)


def outdropdown_pressed(event):
    outitem = dropdownout.get()
    print("Dropdown pressed. Selected item:", outitem)


exchange_rates = data["data"]
available_currencies = ""
for currency in exchange_rates.keys():
    available_currencies += currency + ", "
print(data)
available_currencies = available_currencies[:-2]
print("Available currencies: " + available_currencies)

# Create the main window
window = tk.Tk()
window.title("CURRENCY CONVERTER (100% FREE) CRACKED")
frame = tk.Frame(window)
frame.pack()
window.geometry("800x400")
# Define the Futura font for the title
title_font = font.Font(family="Futura", size=22, weight="bold")

# Define the Futura font for the buttons
button_font = font.Font(family="Futura", size=14, weight="bold")
convert_font = font.Font(family="Futura", size=12, weight="bold")
# Define the button colors
button_color = "#0583D2"
# Button background color

# Create a label for the title
title_label = tk.Label(window, text="CURRENCY CONVERTER (100% FREE) CRACKED", font=title_font)
title_label.pack(pady=20)


def button_pressed():
    from_currency = dropdownin.get()
    to_currency = dropdownout.get()
    text = Inputtext.get("1.0", "end")
    print(text)
    amount = float(text)
    Output = (data['data'][to_currency]['value'] / data['data'][from_currency]['value']) * amount
    print(Output)
    Outputtext.config(text=Output)


# Create the Input textbox
Inputtext = tk.Text(window, width=22, height=1, font=button_font, bg=button_color, bd=0, relief=tk.SOLID)
Inputtext.pack(side="left", padx=(90, 10))

# Create the Output button
Outputtext = tk.Label(window, width=20, font=button_font, bg=button_color, bd=0, relief=tk.SOLID)
Outputtext.pack(side="right", padx=(10, 90))

convertbutton = tk.Button(window, text="CONVERT", width=8, height=1, command=button_pressed, font=convert_font)
convertbutton.place(x=355, y=200)

# Create the input currency button
button3 = tk.Button(window, text="Select Country:", width=20, font=button_font, bg=button_color,
bd=0, relief=tk.SOLID)
button3.place(x=90, y=170)

dropdownin = ttk.Combobox(window, values=["CAD", "USD", "UAH"])
dropdownin.place(x=90, y=150)

# Create the output dropdown
button4 = tk.Button(window, text="Select Country:", width=20, font=button_font, bg=button_color, bd=0, relief=tk.SOLID)
button4.place(x=465, y=170)

dropdownout = ttk.Combobox(window, values=["CAD", "USD", "UAH"])
dropdownout.place(x=465, y=150)


def on_leave(event):
    event.widget.config(bg=button_color)

dropdownin.bind("<<ComboboxSelected>>", indropdown_pressed)

dropdownout.bind("<<ComboboxSelected>>", outdropdown_pressed)


# Start the main loop
window.mainloop()
