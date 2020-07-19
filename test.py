from tkinter import *

root = Tk()
root.wm_title("Thank You For Using Our App")
photo = PhotoImage(file="ips.png")

label = Label(root,image=photo)
label.pack()
root.mainloop()
