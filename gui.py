import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

root = tk.Tk()

root.title("HOTEL RATE SHOPPER")
root.geometry('600x400+50+50')

s= ttk.Style()
s.theme_use('clam')

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
# root.rowconfigure(0,weight=1)
# root.rowconfigure(1,weight=1)
# root.rowconfigure(2,weight=1)

start_date = ""
end_date = ""

def calender_func(arg):
    print(arg)
    def print_sel(): 
        selected_date = arg 
        if selected_date == "start":
            start_date = cal.selection_get()
            print(type(start_date), start_date)
            label_date = ttk.Label(root, text = start_date)
            label_date.grid(column=0, row=2,padx=5, pady=5)
        else:
            end_date = cal.selection_get()
            print(type(end_date), end_date)
            label_date = ttk.Label(root, text = end_date)
            label_date.grid(column=2, row=2,padx=5, pady=5)
        top.destroy()
        

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", 
                   cursor="hand1")
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

title = ttk.Label(root, text="HOTEL RATE SHOPPER")
title.grid(column=1, row=0, columnspan=1,padx=5, pady=50)
start_button = ttk.Button(root, text='Start Date', command=lambda: calender_func("start"))
start_button.grid(column=0, row=1, padx=5, pady=5)
end_button = ttk.Button(root, text='End Date', command=lambda: calender_func("end"))
end_button.grid(column=2, row=1, padx=5, pady=5)
submit_button = ttk.Button(root, text='Submit', command=lambda: print("submit"))
submit_button.grid(column=1, row=2, padx=5, pady=5)

root.mainloop()
