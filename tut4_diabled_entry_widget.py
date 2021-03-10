import tkinter as tk 

def fun():
    pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Disabled Input's")
    root.geometry("650x400")

    hold_entry= tk.StringVar()
    # create variable to hold value to be shown
    hold_entry.set("Disbled Text"); # you must do by this way
    etry= tk.Entry(root,textvariable=hold_entry,font=("Source code Pro",12,'bold'),state='disabled')
    etry.pack()

    tk.Button(root,text="submit",command=fun).pack()
    root.mainloop()