import tkinter as tk 

def createFile():
    with open("Data.txt",'w') as f:
        f.write("Name,Age\n")

def update_file(a,b):
    with open("Data.txt",'a') as f:
        f.write(f"{a},{b}\n")

def fun():
    a= name_of_person.get()
    b=education.get()
    update_file(a,b)
    name_of_person.set("")
    education.set("")
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Taking Input's")
    root.geometry("650x400")
    createFile()
    name_of_person = tk.StringVar()
    education= tk.StringVar()

    # creating widget of userID and password
    tk.Label(root,text="Enter Name\n").pack(side='top')
    ID=tk.Entry(root,textvariable=name_of_person)
    ID.pack(side='top')
    tk.Label(root,text="Enter Age\n").pack(side='top')
    educa_wid =  tk.Entry(root,textvariable=education,type=number)
    educa_wid.pack(side='top');

    tk.Button(root,text='submit',command=fun).pack(side='top')

    root.mainloop()
