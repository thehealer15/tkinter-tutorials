import tkinter as tk 

def fun():
    global hold_entry
    tk.Label(root,text=str(hold_entry.get()),font=("Times New Roman",20,'italic')).pack(side='bottom')
    hold_entry.set("")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Taking Input's")
    root.geometry("650x400")
    
    

    # our app will take one input
    # when submitted it will show in label

    hold_entry = tk.StringVar() # to hold input value of entry

    etry= tk.Entry(root,textvariable=hold_entry,font=("Source code Pro",12,'bold'),show="*")
    btn=tk.Button(root,text="Submit",command=fun)
    etry.pack()
    tk.Label(root,text="\n").pack()
    btn.pack()

    root.mainloop()


"""
    basic syntax:
    entry_obj = tk.Entry(parent window, possible arg)
    bg => backgroud color of entry widget
    it can be font, bd (border default value is 2 px)
    show ( when we put password on instagram or facebook, it shows
        as * we can achive by show method
     )
    textVariable => this will hold variable value (must be StringVar class)

    Predefined Functions:
    entry_obj.get() => will return input in entry widget
    entry_obj.delete() => clear's input
    """"""
"""