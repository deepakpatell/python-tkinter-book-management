from tkinter import*

master=Tk()

def e1_delete():
    e1.delete(first=0,last=22)

e1=Entry(master, width=20)
e1.pack()

B=Button(master, text="Submit", command=e1_delete)
B.pack()

master.mainloop
