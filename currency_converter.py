from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('310x340+500+200')
window.title('Currency Converter')
window.resizable(height=FALSE, width=FALSE)

# colors for the application
primary = '#081F4D'
secondary = '#0083FF'
white = '#FFFFFF'

# the top frame
top_frame = Frame(window, bg=primary, width=300, height=80)
top_frame.grid(row=0, column=0)
# label for the text Currency Converter
name_label = Label(top_frame, text='Currency Converter', bg=primary, fg=white, pady=30, padx=24, justify=CENTER, font=('Poppins 20 bold'))
name_label.grid(row=0, column=0)

# the top frame
top_frame = Frame(window, bg=primary, width=300, height=80)
top_frame.grid(row=0, column=0)
# label for the text Currency Converter
name_label = Label(top_frame, text='Currency Converter', bg=primary, fg=white, pady=30, padx=24, justify=CENTER, font=('Poppins 20 bold'))
name_label.grid(row=0, column=0)
# the bottom frame
bottom_frame = Frame(window, width=300, height=250)
bottom_frame.grid(row=1, column=0)
# widgets inside the bottom frame
from_currency_label = Label(bottom_frame, text='FROM:', font=('Poppins 10 bold'), justify=LEFT)
from_currency_label.place(x=5, y=10)
to_currency_label = Label(bottom_frame, text='TO:', font=('Poppins 10 bold'), justify=RIGHT)
to_currency_label.place(x=160, y=10)
# this is the combobox for holding from_currencies
from_currency_combo = ttk.Combobox(bottom_frame, width=14, font=('Poppins 10 bold'))
from_currency_combo.place(x=5, y=30)
# this is the combobox for holding to_currencies
to_currency_combo = ttk.Combobox(bottom_frame, width=14, font=('Poppins 10 bold'))
to_currency_combo.place(x=160, y=30)
# the label for AMOUNT
amount_label = Label(bottom_frame, text='AMOUNT:', font=('Poppins 10 bold'))
amount_label.place(x=5, y=55)
# entry for amount
amount_entry = Entry(bottom_frame, width=25, font=('Poppins 15 bold'))
amount_entry.place(x=5, y=80)
# an empty label for displaying the result
result_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
result_label.place(x=5, y=115)
# an empty label for displaying the time
time_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
time_label.place(x=5, y=135)
# the clickable button for converting the currency
convert_button = Button(bottom_frame, text="CONVERT", bg=secondary, fg=white, font=('Poppins 10 bold'))
convert_button.place(x=5, y=165)

window.mainloop()
