import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from tkcalendar import Calendar

from datetime import date
import concurrent.futures
from selenium import webdriver

from functions import get_hotel_m_rate, get_hotel_h_rate, get_hotel_s_rate
from charting import plot_chart


def calender_func(arg):
    def print_sel(): 
        selected_date = arg 
        if selected_date == "start":
            start_date.set(cal.selection_get())
            start_box = ttk.Entry(root, width=11,textvariable = start_date)
            start_box.grid(column=0, row=2,sticky="E", padx=5, pady=5)    
        else:
            end_date.set(cal.selection_get())
            end_box = ttk.Entry(root, width=11, textvariable = end_date)
            end_box.grid(column=2, row=2,sticky="W",padx=5, pady=5)
        
        top.destroy()
            
    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", 
                   cursor="hand1")
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

def handleSubmit():
    arr_date = date.fromisoformat(start_date.get())
    dep_date = date.fromisoformat(end_date.get())
    num_days = (dep_date - arr_date).days
    s_x_axis, s_y_axis = get_hotel_s_rate(arr_date, num_days)
   
    #SETUP CHROME DRIVER
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver1 = webdriver.Chrome(options=options)
    driver2 = webdriver.Chrome(options=options)

    #FETHCING RATES IN PARALLEL BY LAUNCHING TWO BROWSER
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_m = executor.submit(get_hotel_m_rate, arr_date, num_days, driver1)
        future_h = executor.submit(get_hotel_h_rate, arr_date, num_days, driver2)
        try:
            (m_x_axis, m_y_axis) = future_m.result()
            (h_x_axis, h_y_axis) = future_h.result()
            plot_chart(h_x_axis, h_y_axis, m_y_axis, s_y_axis)
        except:
            showerror("Error", "Opps something went wrong")
        finally:
            driver1.close()
            driver2.close()
        
        
#SETUP AND LAYOUT
root = tk.Tk()

root.title("HOTEL RATE SHOPPER")
root.geometry('600x450+50+50')
root.config(bg='#4a7a8c')

s= ttk.Style()
s.theme_use('clam')

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)

start_date = tk.StringVar()
end_date = tk.StringVar()

img = tk.PhotoImage(file='logo.png')
logo = ttk.Label(root,image=img,background="grey")
logo.grid(column=1, row=0, columnspan=1,padx=5, pady=50)

start_button = ttk.Button(root, text='Start Date', command=lambda: calender_func("start"))
start_button.grid(column=0, row=1, sticky="E", padx=5, pady=5)

end_button = ttk.Button(root, text='End Date', command=lambda: calender_func("end"))
end_button.grid(column=2, row=1, sticky="W", padx=5, pady=5)

submit_button = ttk.Button(root, text='Submit', command=handleSubmit)
submit_button.grid(column=1, row=3, padx=5, pady=5)
notice_label = ttk.Label(root, text="Max 28 days",background='#4a7a8c')
notice_label.grid(column=1, row=4)


root.mainloop()
