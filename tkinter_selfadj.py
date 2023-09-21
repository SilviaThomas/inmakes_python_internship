from tkinter import *
root=Tk()
label1=Label(root,text="hii",fg="red",bg="blue")
label1.pack(fill=X)
label2=Label(root,text="hello",fg="blue",bg="red")
label2.pack(side=LEFT,fill=Y)

root.mainloop()