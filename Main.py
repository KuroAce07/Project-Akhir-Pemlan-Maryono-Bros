import tkinter
from csv import *
from tkinter import *
from PIL import Image, ImageFont, ImageDraw 
from tkinter import messagebox

tk = tkinter.Tk()
tk.title("Data Base System")
#canvas=tkinter.Canvas(tk, width=300, height=300)
#canvas.grid()
tk.geometry()
tk.configure(bg='purple')
data = []

def cetak():
    my_image = Image.open("card.png")
    #NAMA
    nama = E1.get()
    nama_font = ImageFont.truetype("arial.ttf",40)
    nama_text = nama
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((50,140), nama_text, (0, 0, 0), font=nama_font)
    #TTL
    ttl = E2.get()
    ttl_font = ImageFont.truetype("arial.ttf",40)
    ttl_text = ttl
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((350,270), ttl_text, (0, 0, 0), font=ttl_font)
    #KELAMIN
    kelamin = E3.get()
    kelamin_font = ImageFont.truetype("arial.ttf",40)
    kelamin_text = kelamin
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((50,270), kelamin_text, (0, 0, 0), font=kelamin_font)
    #AGAMA
    agama = E4.get()
    agama_font = ImageFont.truetype("arial.ttf",40)
    agama_text = agama
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((50,400), agama_text, (0, 0, 0), font=agama_font)
    #ALAMAT
    alamat = E5.get()
    alamat_font = ImageFont.truetype("arial.ttf",40)
    alamat_text = alamat
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((330,400), alamat_text, (0, 0, 0), font=alamat_font)
    #PEKERJAAN
    job = E6.get()
    job_font = ImageFont.truetype("arial.ttf",40)
    job_text = job
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((630,400), job_text, (0, 0, 0), font=job_font)
    my_image.show()
    my_image.save(nama+".png")

def add():
    lst = [E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get()]
    data.append(lst)
    messagebox.showinfo("Information","Data Telah Berhasil Ditambahkan")

def save():
    with open("data.csv","w") as file:
        Writer=writer(file)
        Writer.writerow(["Nama","TTL","Kelamin","Agama","Alamat","Pekerjaan"])
        Writer.writerows(data)
        messagebox.showinfo("Information","Saved succesfully")

def delete():
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)
    E5.delete(0,END)
    E6.delete(0,END)

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
#ADD
button=tkinter.Button(tk, text='TAMBAHKAN DATA', bg="blue", fg="White", width=20, command=add)
button.grid(row = 6, column = 1, sticky = W, pady = 2)
#SAVE
button=tkinter.Button(tk, text='SIMPAN DATA', bg="blue", fg="White", width=20, command=save)
button.grid(row = 7, column = 1, sticky = W, pady = 2)
#CETAK
button=tkinter.Button(tk, text='CETAK KARTU', bg="blue", fg="White", width=20, command=cetak)
button.grid(row = 8, column = 1, sticky = W, pady = 2)
#EXIT
button=tkinter.Button(tk, text='KELUAR', bg="blue", fg="White", width=20, command=tk.quit)
button.grid(row = 9, column = 1, sticky = W, pady = 2)
tk.mainloop()