import tkinter as tk

window = tk.Tk()

window.title("Address book")

window.geometry("400x400")


# LABEL
title = tk.Label(text = "Hello sir.  Welcome to Address Book", font=("Times New Roman",20))
title.grid(column=0, row=0)


# BUTTON
button1 = tk.Button(text = 'ADD', bg='green')
button1.grid(column=1,row=4)

button2 = tk.Button(text = 'EDIT',bg= 'yellow')
button2.grid(column=2,row=4)

button3 = tk.Button(text = 'DELETE',bg='red')
button3.grid(column=3,row=4)

button4 = tk.Button(text = 'SORT BY NAME',bg='sky blue')
button4.grid(column=4,row=4)

# ENTRY FIELD
entryfield1 = tk.Entry()
entryfield1.grid(column=0, row=9)

# Text field
textfiled = tk.Text(master=window,height=10,width=30)
textfiled.grid()

window.mainloop()