import tkinter as tk 
def display(event):
    """
    When we will be pressing any key, bind function passes event by default.
    This will generate error if you don't include event as first parameter
    """
    tk.Label(root,text="Up Key pressed").pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Binding key")
    root.geometry("650x400")
    root.bind("<Up>",display)
    root.mainloop()
