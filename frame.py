import tkinter as tk 

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Taking Input's")
    root.geometry("650x400")
    
    frame=tk.Frame(root)
    frame.pack()
    # as we have to put elements in this 
    # this widget should get packed before others
    tk.Label(frame,text="LEFT",fg="red").pack(side=tk.LEFT)
    tk.Label(frame,text="RIGHT",fg="green").pack(side=tk.RIGHT)
    tk.Label(frame,text="TOP",fg='blue').pack(side=tk.TOP)
    tk.Label(frame,text="BOTTOM",fg="cyan").pack(side=tk.BOTTOM)
    root.mainloop()
