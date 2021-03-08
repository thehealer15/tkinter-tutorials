import tkinter as tk 


def fun():
    """
    This function will be triggered when we will click button
    """
    tk.Label(root,text="clicked").pack()
    # this is another method to packing a widget
    # no need to create instances of Label but dis advantage is 
    # we can't use for furthur work

if __name__ == "__main__":
    """
    Writing main is standard practice 
    if this file is imported in other python file this code will not work
    if this code is run here only ther this main will be run
    """
    # creating main window
    root= tk.Tk()
    root.geometry("450x300")
    root.title("Creating Buttons")

    btn = tk.Button(root,text="Click Me",command=fun)
    """
    syntax:
    Button(parent window, text="This will apprear on button", commad= pass refrence of fun)
    Note: in command =  pass refrence of function to call i.e. write name of fun don't use ()
    using () will call out function
    """
    
    btn.pack()
    # pack button

    root.mainloop()