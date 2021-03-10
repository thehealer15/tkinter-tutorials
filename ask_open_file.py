import tkinter as tk 
from tkinter.filedialog import askopenfile
from tkinter import messagebox as mb
# you must import this

def browse():
    location= askopenfile(filetypes=[('Text Files','*.py')])
    '''
 askopeenfile(mode=, filetypes=[(‘any name you want to display in browsing window’, ‘extensions of file type’)]) 
    mode can be r or w 
    '''
    
    if(location!=None):
        c=location.read()
        mb.INFO("File found")
    else:
        mb.showerror("Please put file")
        
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Taking Input's")
    root.geometry("650x400")
    tk.Label(root,text="Upload Resume\n").pack()
    
    tk.Button(root,text="Select file",command=browse).pack()

    root.mainloop()