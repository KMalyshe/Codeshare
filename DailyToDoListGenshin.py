import tkinter as tk


# define window and set initial size
top = tk.Tk()
top.geometry("200x150")

# text definitions
task1 = tk.Label(top, text = "Complete Commissions.").place(x = 10,y = 10)
task2 = tk.Label(top, text = "Use Original Resin.").place(x = 10,y = 30)
task3 = tk.Label(top, text = "Complete Daily Check-In.").place(x = 10,y = 50)
task4 = tk.Label(top, text = "Gather Resources.").place(x = 10,y = 70)
task5 = tk.Label(top, text = "Visit Merchants.").place(x = 10,y = 90)
task6 = tk.Label(top, text = "Forge Mystic Ores.").place(x = 10,y = 110)

# coordinate storage
xcoord = tk.Label(top)
ycoord = tk.Label(top)

def callback(event):
    xcoord["text"] = str(event.x)
    ycoord["text"] = str(event.y)
top.bind('<Button-1>',callback)

top.mainloop()


