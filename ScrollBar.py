import tkinter as tk 

if __name__ == "__main__":
    root = tk.Tk()
    root.title("ScrollBar")
    root.geometry("650x400")

    scroll_bar = tk.Scrollbar(root) 
    # creating GUI
    scroll_bar.pack( side = tk.RIGHT, 
                    fill = tk.Y ) 
   # tk.Y is global variable
  
    
    mylist = tk.Listbox(root,  
                    yscrollcommand = scroll_bar.set ) 
   #yscrollcommand because we wanted up to down scrolling
    for i in range(1, 500): 
        mylist.insert(tk.END,  str(i))  
        # inserts 
    mylist.pack( side = tk.LEFT, fill = tk.BOTH )    
    scroll_bar.config( command = mylist.yview ) # most important
   #why yview because we wanted up to down scrolling 
    
    root.mainloop()
