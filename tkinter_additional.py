from tkinter import *

class Student:
    def __init__(self, root):
        self.root = root
        root.title("Student")

        self.label = Label(root, text="Click a button:")
        self.label.pack()

        self.click_button = Button(root, text="OK", command=self.click_message)
        self.click_button.pack()

        self.label = Label(root, text="Click a button to cancel:")
        self.label.pack()

        self.cancel_button = Button(root, text="Cancel", command=self.cancel_message)
        self.cancel_button.pack()

        self.label = Label(root, text="Click a button to exit:")
        self.label.pack()

        self.exit_button = Button(root, text="Exit", command=self.exit_btn)
        self.exit_button.pack()

    def click_message(self):
        print("Button Clicked")

    def cancel_message(self):
        print("Button Cancelled")

    def exit_btn(self):
        self.root.destroy()

root = Tk()
app = Student(root)
root.mainloop()
