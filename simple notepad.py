import tkinter as tk 
import tkinter.messagebox as mb
def create():
   with open("a.txt",'wb+') as f:pass

def save():
    create()
    a = T.get("1.0","end-1c")
    with open("temp.txt",'a') as f:
       f.write(a)


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

    
# .add_command(label="name of menu item", function to be called when clicked)
    file.add_separator() # add's a line
    file.add_command(label="Save ",command=save)
    file.add_separator()
    file.add_command(label="exit",command=root.destroy)
    T= tk.Text(root,height=18,width=40,bg='light cyan',font=('Times new roman',11))
    T.pack()

    root.config(menu=menu)
    # this is to real time configuration of menu
    # this is method packing but it makes programmer enable to real time update
    root.mainloop()
