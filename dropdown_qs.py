from tkinter import *

def fun1():
    print("This is for New Project")

def fun2():
    print("This is for New")

def fun3():
    print("This is for New Scratch File")

def fun4():
    print("This is for Open File")

def fun5():
    print("This is for Save As")

root = Tk()

mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)
mymenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New Project...", command=fun1)
submenu.add_command(label="New..", command=fun2)
submenu.add_separator()
submenu.add_command(label="New Scratch File", command=fun3)
submenu.add_command(label="Open..", command=fun4)
submenu.add_separator()
submenu.add_command(label="Save AS..", command=fun5)
submenu.add_command(label="Exit", command=root.quit)

newmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit", menu=newmenu)
newmenu.add_command(label="Undo Typing..", command=fun1)
newmenu.add_command(label="Redo", command=fun1)
newmenu.add_separator()
newmenu.add_command(label="Cut", command=fun1)
newmenu.add_command(label="Copy..", command=fun1)
newmenu.add_separator()
newmenu.add_command(label="Copy path/Reference..", command=fun1)
newmenu.add_command(label="Paste..", command=fun1)

newmenu1 = Menu(mymenu)
mymenu.add_cascade(label="View", menu=newmenu1)
newmenu1.add_command(label="Tool Windows", command=fun1)
newmenu1.add_command(label="Appearance", command=fun1)
newmenu1.add_separator()
newmenu1.add_command(label="Quick Definition", command=fun1)
newmenu1.add_command(label="Parameter Info", command=fun1)
newmenu1.add_separator()
newmenu1.add_command(label="Type Info", command=fun1)
newmenu1.add_command(label="Context Info", command=fun1)

newmenu2 = Menu(mymenu)
mymenu.add_cascade(label="Navigate", menu=newmenu2)
newmenu2.add_command(label="Back", command=fun1)
newmenu2.add_command(label="Forward", command=fun1)
newmenu2.add_separator()
newmenu2.add_command(label="Search Forward", command=fun1)
newmenu2.add_command(label="Class..", command=fun1)
newmenu2.add_separator()
newmenu2.add_command(label="File..", command=fun1)
newmenu2.add_command(label="Symbol..", command=fun1)

newmenu3 = Menu(mymenu)
mymenu.add_cascade(label="Code", menu=newmenu3)
newmenu3.add_command(label="Implement Methods..", command=fun1)
newmenu3.add_command(label="Generate", command=fun1)
newmenu3.add_separator()
newmenu3.add_command(label="Code Completion", command=fun1)
newmenu3.add_command(label="Inspect Code..", command=fun1)
newmenu3.add_separator()
newmenu3.add_command(label="Code Cleanup", command=fun1)
newmenu3.add_command(label="Override Method", command=fun1)

root.mainloop()
