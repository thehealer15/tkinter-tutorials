import tkinter as tk 

def createFile():
    with open("Contacts.txt",'w') as f:
        f.write("Name,Contact Number\n")

def update_file(a,b):
    with open("Contacts.txt",'a') as f:
        f.write(f"{a},{b}\n")
    tk.Label(root,text="Saved Successfully").pack(side='bottom')

def fun():
    a= name_of_person.get()
    b=num.get()
    update_file(a,b)
    name_of_person.set("")
    num.set("")
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Contacts")
    root.geometry("650x400")
    createFile()
    name_of_person = tk.StringVar()
    num= tk.StringVar()

    # creating widget of Name and contact Number
    tk.Label(root,text="Enter Name\n").pack(side='top')
    name_wid=tk.Entry(root,textvariable=name_of_person)
    name_wid.pack(side='top')
    tk.Label(root,text="Enter Number\n").pack(side='top')
    num_wid =  tk.Entry(root,textvariable=num)
    num_wid.pack(side='top');

    tk.Button(root,text='submit',command=fun).pack(side='top')

    root.mainloop()
