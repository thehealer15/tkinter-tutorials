import tkinter as tk 

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Canvas")
    root.geometry("650x400")

    canvas_widget= tk.Canvas(root,height = 250, width = 300,bg='green')

    # Some general methods:
    oval_widget=canvas_widget.create_oval(108, 120, 320, 40,fill="red")
    # fill method= to fill color 
    
    ARC = canvas_widget.create_arc(10,12,541,123,start=0,extent=220,fill='blue')

    # creating line:
    l=canvas_widget.create_line(102,21,432,122,fill='cyan')


    canvas_widget.pack()
    root.mainloop()
