import tkinter as tk 
import tkinter.messagebox as mb

def new():
   mb.showinfo("New FIle", "New File created")
def save():
    mb.showinfo("Saved", "SuccessFully saved")
    
if __name__ == "__main__":
    # basic window
    root = tk.Tk()
    root.title("Menu ")
    root.geometry("650x400")
    
    menu=tk.Menu(root)    
    # menu widget created
    
    file=tk.Menu(menu,tearoff=0)
    menu.add_cascade(label='File',menu=file)
    # a cascade of name file is added now we can insert many elements into this
    # this will be added downwards

    file.add_command(label="New File",command=new)
# .add_command(label="name of menu item", function to be called when clicked)
    file.add_separator() # add's a line
    file.add_command(label="Save ",command=save)
    file.add_separator()
    file.add_command(label="exit",command=root.destroy)
    
    root.config(menu=menu)
    # this is to real time configuration of menu
    # this is method packing but it makes programmer enable to real time update
    root.mainloop()
