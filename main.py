import tkinter as tk
from tkinter import ttk

#Create the main window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

#Ttk widgets
label = ttk.Label(master=window,text='This is a test')
label.pack()

text = tk.Text(master=window)
text.pack()

entry = ttk.Entry(master=window)
entry.pack()

another_label = ttk.Label(master=window, text='my label')
another_label.pack()

def button_func():
        print('A button was pressed.')

button = ttk.Button(master=window, text='A Button',command=button_func)
button.pack()

def exercise_button_func():
        print('Hello')

exercise_button = ttk.Button(master=window,text='Print Hello',command=exercise_button_func)
exercise_button.pack()

#Run app
window.mainloop()

