import tkinter as tk 
def create():
    with open("a.txt",'wb+') as f:pass

def save():
    a = T.get("1.0","end-1c")
    with open("a.txt",'a') as f:
        f.write(a)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Text widget")
    root.geometry("650x400")
    create()
    # creating text widget
    T= tk.Text(root,height=18,width=40,bg='light cyan',font=('Times new roman',11),yscrollcommand=True,xscrollcommand=True)
    
    T.pack() # packing
    
    tk.Button(root,text="submit",command=save).pack(side='right')

    root.mainloop()
