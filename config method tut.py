import tkinter as tk 

def change():
    label.config(text="Changed")
    # widget.config(the argument you want to change="value")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Real Time updating")
    root.geometry("650x400")
    
    label= tk.Label(root,text="Before click")
    label.pack()
    # as we need to grab it again in order to change text
    # store it as instance

    tk.Button(root,text="Click Me to change text",command=change).pack()
    # when we press button, text will be changed
    root.mainloop()
