from tkinter import *

CNF={
    'font':('',24),
    'bg':'#333333',
    'fg':'orange'
}

CNF_GRID={
    'padx':10,
    'pady':20
}




def Register():
    





















root=Tk()
root.config(bg='#333333')

Button(root,CNF,text='Register').grid(row=1,column=1,cnf=CNF_GRID)
Button(root,CNF,text='Login').grid(row=1,column=2,cnf=CNF_GRID)
Button(root,CNF,text='Strong password').grid(row=2,column=1,cnf=CNF_GRID)
Button(root,CNF,text='Change password').grid(row=2,column=2,cnf=CNF_GRID)

root.mainloop()