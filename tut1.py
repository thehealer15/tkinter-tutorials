import tkinter as tk
'''
It's inbuilt GUI lib. provided in 33 mb python we download
for python 3 or 3+, it's tkinter
for python version less than 3, it's Tkinter
'''

root= tk.Tk()  
# root is main window of GUI, it has no parent

root.geometry("400x300")
'''
syntax:
window.geometry("widthxheight")
'''
root.title("First GUI application")
'''
syntax:
window.title("Title you want")
'''

label = tk.Label(root,text="Hello World",font=("Times New Roman",23))
'''
Label is widget as name suggest it's  
used to display text or image on the screen
syntax:
Label(parentGUI,text="Something",font=("Times New Roman",23)) 
It can have many arguements like padx,pady,underline, image
We will see in upcoming tutorial's 
'''

label.pack(side='bottom')
'''
The pack() Method −
This method allows widgets in blocks before placing them in the parent widget.
The grid() Method  − 
This method allows widgets in a table-like structure in the parent widget.
The place() Method − 
This methods allows widgets by placing them in a specific position in the parent widget
there are 3 methods to pack a widget
1. grid(row=0,column=0)
2. pack() # default arguemnt is top, can have arguments like
side= 'left' or side='right'
Note: This is valid side='left' or side=LEFT, it's a standard practice to write global variables in capital
3. place() it can have x,y i.e. position or height and width as argurments 
'''
root.mainloop()
# the infinite event loop. 