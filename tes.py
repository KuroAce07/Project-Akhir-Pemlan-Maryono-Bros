import tkinter
from csv import *
from tkinter import *
from tkinter import messagebox



def login(tk):
    button=tkinter.Button(tk, text='REGISTER', bg="blue", fg="White", width=20)
    button.grid(row = 0, column = 0, sticky = W, pady = 2)
    L0 = Label(tk,bg='purple',fg='green',text="                                   ")
    L0.grid(row = 1, column = 0, sticky = W, pady = 2)
    L0 = Label(tk,bg='purple',fg='green',text="                                   ")
    L0.grid(row = 1, column = 1, sticky = W, pady = 2)
    L1 = Label(tk,bg='white',fg='green',text="User")
    L1.grid(row = 2, column = 0, sticky = W, pady = 2)
    E1 = Entry(fg="white", bg="blue", width=25)
    E1.grid(row = 2, column = 1, pady = 2)
    L2 = Label(tk,bg='white',fg='green',text="Password")
    L2.grid(row = 3, column = 0, sticky = W, pady = 2)
    E2 = Entry(fg="white", bg="blue", width=25)
    E2.grid(row = 3, column = 1, pady = 2)
    button=tkinter.Button(tk, text='LOGIN', bg="blue", fg="White", width=20, command=lambda:sukseslogin(E1,E2))
    button.grid(row = 4, column = 0, sticky = W, pady = 2)
    button=tkinter.Button(tk, text='EXIT', bg="blue", fg="White", width=20, command=quit)
    button.grid(row = 4, column = 1, sticky = W, pady = 2)
    
def sukseslogin(E1,E2):
    a_user, a_pass = ["admin", "admin"]
    if E1.get() == a_user and E2.get() == a_pass:
        messagebox.showinfo("Login Page","Selamat Anda Berhasil Login")
    else:
        messagebox.askretrycancel("Login Page","Username dan Password Salah")
    
tk = tkinter.Tk()
login(tk)
tk.mainloop()




'''from tkinter import *


def raise_frame(frame):
    frame.tkraise()

root = Tk()

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')


Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
Label(f1, text='FRAME 1').pack()

Label(f2, text='FRAME 2').pack()
Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

Label(f3, text='FRAME 3').pack(side='left')
Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

Label(f4, text='FRAME 4').pack()
Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)
root.mainloop()'''