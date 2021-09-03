import tkinter as tk
from tkinter import messagebox
import winsound

counter = 25*60
running = False
phase = 'Pom'

def set_time(i):
    m, s = divmod(i, 60)  
    display_time = ('{:02d}:{:02d}'.format(m, s))
    lbl_value["text"] = display_time

def subtract():
    global running
    global counter
    if running: 
        if counter > 0:  
            set_time(counter)
            print(counter)
            counter -= 1
        else:
            running = False
            winsound.MessageBeep()
            messagebox.showinfo("Time's up!", "Good session!")
    if not running: 
        pass
    window.after(1000,subtract)




def Pom():
    global counter
    global phase
    counter = 25*60
    phase = 'Pom'
    set_time(counter)

def sb(): 
    global counter
    global phase
    counter = 5*60
    phase = 'sb' 
    set_time(counter)

def lb(): 
    global counter
    global phase
    counter = 10*60
    phase = 'lb'
    set_time(counter)

def start(): 
    global counter
    global running
    global phase
    running = True
    btn_pom['state']='disabled'
    btn_shortbreak['state'] = 'disabled' 
    btn_longbreak['state'] = 'disabled' 
    btn_start['state'] = 'disabled'
    btn_stop['state'] = 'normal'
    btn_reset['state'] = 'disabled'
    print(phase + ": " + str(running))
    set_time(counter)
 

def stop():
    global running
    running = False
    btn_pom['state']='normal'
    btn_shortbreak['state'] = 'normal' 
    btn_longbreak['state'] = 'normal' 
    btn_start['state'] = 'normal'
    btn_stop['state'] = 'normal'
    btn_reset['state'] = 'normal' 
    print(phase + ": " + str(running))

def reset():
    global counter
    global running
    global phase
    running = False
    if phase == 'Pom': 
        counter = 25*60 
    elif phase == 'sb': 
        counter = 5*60
    else:  
        counter = 10*60
    btn_pom['state']='normal'
    btn_shortbreak['state'] = 'normal' 
    btn_longbreak['state'] = 'normal' 
    btn_start['state'] = 'normal'
    btn_stop['state'] = 'normal'
    btn_reset['state'] = 'normal'  
    print(phase + ": " + str(running))
    set_time(counter)

window = tk.Tk()
window.title = "Pomodoro" 


window.rowconfigure([0,1,2], minsize=40, weight=6)
window.columnconfigure([0, 1, 2], minsize=40, weight=6)

btn_pom = tk.Button(window, text="Pomodoro", font = ("Arial", 12, "bold"), bg="#2ba6cb", fg="white", command = Pom)
btn_pom.grid(row=0, column=0, sticky="nsew")

btn_shortbreak = tk.Button(master=window, text="Short Break", font = ("Arial", 12, "bold"), bg="#2ba6cb", fg="white", command = sb)
btn_shortbreak.grid(row=0, column=1, sticky="nsew")

btn_longbreak = tk.Button(master=window, text="Long Break", font = ("Arial", 12, "bold"), bg="#2ba6cb", fg="white",  command = lb)
btn_longbreak.grid(row=0, column=2, sticky="nsew")

lbl_value = tk.Label(master=window, text='{:02d}:{:02d}'.format(25, 0), font = ("Arial", 25, "bold"))
lbl_value.grid(row=1, columnspan= 3)

btn_start = tk.Button(window, text="Start", font = ("Arial", 12, "bold"), bg="#5da423", fg="white",  command = start)
btn_start.grid(row=2, column=0, sticky="nsew")

btn_stop = tk.Button(master=window, text="Stop", font = ("Arial", 12, "bold"), bg="#c60f13", fg="white", command = stop)
btn_stop.grid(row=2, column=1, sticky="nsew")

btn_reset = tk.Button(master=window, text="Reset", font = ("Arial", 12, "bold"), bg="#e9e9e9",  command = reset)
btn_reset.grid(row=2, column=2, sticky="nsew")

window.after(1000,subtract)
window.mainloop()
