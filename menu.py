from tkinter import *
from time import *

root = Tk()
root.geometry('600x600')
root.config(background='aquamarine')
root.title('Menu')

menubar = Menu(root)

root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_command(label='Save as')
filemenu.add_command(label='Close')
Edit = Menu(menubar, tearoff=0)
filemenu.add_cascade(label='Edit' , menu=Edit)
Edit.add_command(label='Undo') 
Edit.add_command(label='Redo')
Edit.add_command(label='Cut')
Edit.add_command(label='Copy')
Edit.add_command(label='Paste')
Edit.add_command(label='Delete')
Edit.add_command(label='Select All')
Edit.add_separator()
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

root.mainloop()
