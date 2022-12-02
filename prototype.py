import tkinter
from csv import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageFont, ImageDraw 
from tkinter import messagebox
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 6969
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def raise_frame(frame):
    frame.tkraise()

def sukseslogin():
    a_user, a_pass = ["admin", "admin"]
    if EA.get() == a_user and EB.get() == a_pass:
        messagebox.showinfo("Login Page","Selamat Anda Berhasil Login")
    else:
        messagebox.askretrycancel("Login Page","Username dan Password Salah")

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
    messagebox.showinfo("DATA BASE","Data Telah Berhasil Ditambahkan")

def save():
    with open("data.csv","w") as file:
        Writer=writer(file)
        Writer.writerow(["Nama","TTL","Kelamin","Agama","Alamat","Pekerjaan"])
        Writer.writerows(data)
        messagebox.showinfo("DATA BASE","Saved succesfully")

def delete():
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)
    E5.delete(0,END)
    E6.delete(0,END)

def upload():
    print("[STARTING] Server is starting.")
    """ Staring a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Bind the IP and PORT to the server. """
    server.bind(ADDR)

    """ Server is listening, i.e., server is now waiting for the client to connected. """
    server.listen()
    print("[LISTENING] Server is listening.")

    while True:
        """ Server has accepted the connection from the client. """
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        """ Receiving the filename from the client. """
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename.")
        file = open(filename, "w")
        conn.send("Filename received.".encode(FORMAT))

        """ Receiving the file data from the client. """
        data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the file data.")
        file.write(data)
        conn.send("File data received".encode(FORMAT))

        """ Closing the file. """
        file.close()

        """ Closing the connection from the client. """
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")

tk = tkinter.Tk()
tk.title("Data Base System")
tk.geometry()
tk.configure(bg='purple')
data = []
f1 = Frame(tk)
f2 = Frame(tk)
f3 = Frame(tk)
f4 = Frame(tk)
for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')
raise_frame(f1)
#LOGIN PAGE
button=tkinter.Button(f1, text='REGISTER', bg="blue", fg="White", width=20,command=lambda:raise_frame(f2))
button.grid(row = 0, column = 0, sticky = W, pady = 2)
L = Label(f1,bg='purple',fg='green',text="                                   ")
L.grid(row = 1, column = 0, sticky = W, pady = 2)
L = Label(f1,bg='white',fg='green',text="User")
L.grid(row = 2, column = 0, sticky = W, pady = 2)
EA = Entry(f1,fg="white", bg="blue", width=25)
EA.grid(row = 2, column = 1, pady = 2)
L = Label(f1,bg='white',fg='green',text="Password")
L.grid(row = 3, column = 0, sticky = W, pady = 2)
EB = Entry(f1,fg="white", bg="blue", width=25)
EB.grid(row = 3, column = 1, pady = 2)
button=tkinter.Button(f1, text='LOGIN', bg="blue", fg="White", width=20, command=sukseslogin)
button.grid(row = 4, column = 0, sticky = W, pady = 2)
button=tkinter.Button(f1, text='EXIT', bg="blue", fg="White", width=20, command=exit )
button.grid(row = 4, column = 1, sticky = W, pady = 2)
#NAMA
L1 = Label(f2,bg='purple',fg='white',text="Nama")
L1.grid(row = 0, column = 0, sticky = W, pady = 2)
E1 = Entry(f2,fg="white", bg="blue", width=25)
E1.grid(row = 0, column = 1, pady = 2)
#TTL
L2 = Label(f2,bg='purple',fg='white', text="Tempat Tanggal Lahir")
L2.grid(row = 1, column = 0, sticky = W, pady = 2)
E2 = Entry(f2,fg="white", bg="blue", width=25)
E2.grid(row = 1, column = 1, pady = 2)
#KELAMIN
L3 = Label(f2,bg='purple',fg='white', text="Jenis Kelamin")
L3.grid(row = 2, column = 0, sticky = W, pady = 2)
E3 = Entry(f2,fg="white", bg="blue", width=25)
E3.grid(row = 2, column = 1, pady = 2)
#AGAMA
L4 = Label(f2,bg='purple',fg='white', text="Agama")
L4.grid(row = 3, column = 0, sticky = W, pady = 2)
E4 = Entry(f2,fg="white", bg="blue", width=25)
E4.grid(row = 3, column = 1, pady = 2)
#ALAMAT
L5 = Label(f2,bg='purple',fg='white', text="Alamat")
L5.grid(row = 4, column = 0, sticky = W, pady = 2)
E5 = Entry(f2,fg="white", bg="blue", width=25)
E5.grid(row = 4, column = 1, pady = 2)
#PEKERJAAN
L6 = Label(f2,bg='purple',fg='white', text="Pekerjaan")
L6.grid(row = 5, column = 0, sticky = W, pady = 2)
E6 = Entry(f2,fg="white", bg="blue", width=25)
E6.grid(row = 5, column = 1, pady = 2)
#ADD
button=tkinter.Button(f2, text='TAMBAHKAN DATA', bg="blue", fg="White", width=20, command=add)
button.grid(row = 6, column = 1, sticky = W, pady = 2)
#SAVE
button=tkinter.Button(f2, text='SIMPAN DATA', bg="blue", fg="White", width=20, command=save)
button.grid(row = 7, column = 1, sticky = W, pady = 2)
#UPLOAD
button=tkinter.Button(f2, text='UPLOAD DATA', bg="blue", fg="White", width=20, command=upload)
button.grid(row = 8, column = 1, sticky = W, pady = 2)
#CETAK
button=tkinter.Button(f2, text='CETAK KARTU', bg="blue", fg="White", width=20, command=cetak)
button.grid(row = 9, column = 1, sticky = W, pady = 2)
#EXIT
button=tkinter.Button(f2, text='KELUAR', bg="blue", fg="White", width=20, command=tk.quit)
button.grid(row = 10, column = 1, sticky = W, pady = 2)
tk.mainloop()
# Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).grid()
# Label(f1, text='FRAME 1').grid()
# Label(f2, text='FRAME 2').grid()
# Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).grid()

# Label(f3, text='FRAME 3').grid()
# Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).grid()

# Label(f4, text='FRAME 4').grid()
# Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).grid()




