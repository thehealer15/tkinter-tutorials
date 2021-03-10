from tkinter import *
from tkinter import messagebox as mb

if __name__ == "__main__":
    root = Tk() 
    root.title("Study Message Box")
    root.geometry("800x500") 
  
    Label(root, text ="Let's study messageBox", font = ("Source code Pro",28)).pack() 
    
    mb.showinfo("Heading", "Message") # information
    mb.showwarning("Heading", "Message") # warning user
    mb.showerror("Heading of error", "Message") # telling error
    mb.askquestion("Heading", "question") # asking questions
    mb.askokcancel("Heading", "want to continue") # ok or cancel 2 buttons
    mb.askyesno("Heading", "question") # yes no 
    mb.askretrycancel("Heading", "try again? ") # ask retry or cancel  
    
    root.mainloop()