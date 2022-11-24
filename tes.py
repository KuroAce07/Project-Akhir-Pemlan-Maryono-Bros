import tkinter
import csv
from tkinter import *
from PIL import Image, ImageFont, ImageDraw 

def click():
    nama = E1.get()
    my_image = Image.open("tes.png")
    title_font = ImageFont.truetype("arial.ttf",50)
    title_text = nama
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((50,140), title_text, (0, 0, 0), font=title_font)
    my_image.show()
    my_image.save("result.png")

tk = tkinter.Tk()
tk.title("Data Base System")
#canvas=tkinter.Canvas(tk, width=300, height=300)
#canvas.grid()
tk.geometry()
tk.configure(bg='purple')
#NAMA
L1 = Label(tk,bg='purple',fg='white',text="Nama")
L1.grid(row = 0, column = 0, sticky = W, pady = 2)
E1 = Entry(fg="white", bg="blue", width=25)
E1.grid(row = 0, column = 1, pady = 2)
#TTL
L2 = Label(tk,bg='purple',fg='white', text="Tempat Tanggal Lahir")
L2.grid(row = 1, column = 0, sticky = W, pady = 2)
E2 = Entry(fg="white", bg="blue", width=25)
E2.grid(row = 1, column = 1, pady = 2)
#KELAMIN
L3 = Label(tk,bg='purple',fg='white', text="Jenis Kelamin")
L3.grid(row = 2, column = 0, sticky = W, pady = 2)
E3 = Entry(fg="white", bg="blue", width=25)
E3.grid(row = 2, column = 1, pady = 2)
#AGAMA
L4 = Label(tk,bg='purple',fg='white', text="Agama")
L4.grid(row = 3, column = 0, sticky = W, pady = 2)
E4 = Entry(fg="white", bg="blue", width=25)
E4.grid(row = 3, column = 1, pady = 2)
#ALAMAT
L5 = Label(tk,bg='purple',fg='white', text="Alamat")
L5.grid(row = 4, column = 0, sticky = W, pady = 2)
E5 = Entry(fg="white", bg="blue", width=25)
E5.grid(row = 4, column = 1, pady = 2)
#PEKERJAAN
L6 = Label(tk,bg='purple',fg='white', text="Pekerjaan")
L6.grid(row = 5, column = 0, sticky = W, pady = 2)
E6 = Entry(fg="white", bg="blue", width=25)
E6.grid(row = 5, column = 1, pady = 2)
button=tkinter.Button(tk, text='Translate', bg="blue", fg="White", width=10, command=click)
button.grid()
tk.mainloop()

#NOTE GA EFEKTIF BISA PAKE LOOP DAN TIDAK PERLU STORE SETIAP GET ENTRY DAN FONT JUGA BISA BERSAMA