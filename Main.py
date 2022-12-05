import os
import tqdm
import csv
import socket
import tkinter
import pandas as pd
from csv import *
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageFont, ImageDraw
from pathlib import Path


#Deklarasi Client
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
host = "127.0.0.1"
port = 6969

header = ['Nama', 'TTL', 'Jenis Kelamin', 'Agama', 'Alamat', 'Pekerjaan']
tempdata = []

def raise_frame(frame):
    frame.tkraise()

def toppage(tk, box, f1, f2, frame1, frame2):
    f2.pack_forget()
    frame1.place_forget()
    frame2.place_forget()
    raise_frame(f1)
    f1.pack()

    L = Label(f1,fg='black', text="User")
    L.grid(row=2, column=0, sticky=W, pady=2)
    EA = Entry(f1, fg="white", bg="blue", width=25)
    EA.grid(row=2, column=1, pady=2)
    L = Label(f1, fg='black', text="Password")
    L.grid(row=3, column=0, sticky=W, pady=2)
    EB = Entry(f1, fg="white", bg="blue", width=25,show='*')
    EB.grid(row=3, column=1, pady=2)

    button = tkinter.Button(f1,
                            text='REGISTER',
                            bg="blue",
                            fg="White",
                            width=20,
                            command=lambda:registerpage(tk, f1, f2, frame1, frame2))
    button.grid(row=0, column=0, sticky=W, pady=2)

    button = tkinter.Button(f1,
                            text='LOGIN',
                            bg="blue",
                            fg="White",
                            width=20,
                            command=lambda:sukseslogin(EA, EB, tk, box, f1, f2, frame1, frame2))
    button.grid(row=4, column=0, sticky=W, pady=2)

    button = tkinter.Button(f1,
                            text='EXIT',
                            bg="blue",
                            fg="White",
                            width=20,
                            command=exit)
    button.grid(row=4, column=1, sticky=W, pady=2)

def adminpage(tk, box, f1, f2, frame1, frame2):
    box.config(width=500, height=510)
    f1.pack_forget()
    f2.pack_forget()
    raise_frame(frame1)
    frame1.place(height=400, width=500, relx=0.5, rely=0.4, anchor=CENTER)
    raise_frame(frame2)
    frame2.place(height=55, width=500, relx=0.5, rely=0.87, anchor=CENTER)

    # Treeview Widget
    tv1 = ttk.Treeview(frame1)
    tv1.place(relheight=1, relwidth=1)

    treeload(tv1)

    tvscroll_x = tkinter.Scrollbar(frame1,orient='horizontal',command=tv1.xview)
    tvscroll_y = tkinter.Scrollbar(frame1,orient='vertical',command=tv1.yview)
    tv1.configure(xscrollcommand=tvscroll_x.set,yscrollcommand=tvscroll_y.set)
    tvscroll_x.pack(side='bottom',fill='x')
    tvscroll_y.pack(side='right',fill='y')

    # Buttons
    ## View
    button1 = tkinter.Button(frame2,
                             text='View',
                             command=lambda:viewadmin(tv1))
    button1.place(relx=0.0, rely=0.1)
    ## Add Data
    button4 = tkinter.Button(frame2,
                             text='Add Data',
                             command=lambda:registerpage(tk, f1, f2, frame1, frame2))
    button4.place(relx=0.873, rely=0.1)

def registerpage(tk, f1, f2, frame1, frame2):
    f1.pack_forget()
    frame1.place_forget()
    frame2.place_forget()
    raise_frame(f2)
    f2.pack()
    all_E = []
    # NAMA
    L1 = Label(f2, fg='black', text="Nama")
    L1.grid(row=0, column=0, sticky=W, pady=2)
    E1 = Entry(f2, fg="white", bg="blue", width=25)
    E1.grid(row=0, column=1, pady=2)
    all_E.append(E1)
    # TTL
    L2 = Label(f2, fg='black', text="Tanggal Lahir")
    L2.grid(row=1, column=0, sticky=W, pady=2)
    E2 = Entry(f2, fg="white", bg="blue", width=25)
    E2.grid(row=1, column=1, pady=2)
    all_E.append(E2)
    # KELAMIN
    L3 = Label(f2, fg='black', text="Jenis Kelamin")
    L3.grid(row=2, column=0, sticky=W, pady=2)
    E3 = Entry(f2, fg="white", bg="blue", width=25)
    E3.grid(row=2, column=1, pady=2)
    all_E.append(E3)
    # AGAMA
    L4 = Label(f2, fg='black', text="Agama")
    L4.grid(row=3, column=0, sticky=W, pady=2)
    E4 = Entry(f2, fg="white", bg="blue", width=25)
    E4.grid(row=3, column=1, pady=2)
    all_E.append(E4)
    # ALAMAT
    L5 = Label(f2, fg='black', text="Alamat")
    L5.grid(row=4, column=0, sticky=W, pady=2)
    E5 = Entry(f2, fg="white", bg="blue", width=25)
    E5.grid(row=4, column=1, pady=2)
    all_E.append(E5)
    # PEKERJAAN
    L6 = Label(f2, fg='black', text="Pekerjaan")
    L6.grid(row=5, column=0, sticky=W, pady=2)
    E6 = Entry(f2, fg="white", bg="blue", width=25)
    E6.grid(row=5, column=1, pady=2)
    all_E.append(E6)

    # ADD
    button = tkinter.Button(f2,
                            text='TAMBAHKAN DATA',
                            bg="blue",
                            fg="White",
                            width=20,
                            command=lambda:add(all_E))
    button.grid(row=6, column=1, sticky=W, pady=2)

    # SAVE
    button = tkinter.Button(f2, text='SIMPAN DATA', bg="blue", fg="White", width=20, command=save)
    button.grid(row=7, column=1, sticky=W, pady=2)

    # UPLOAD
    button = tkinter.Button(f2, text='UPLOAD DATA', bg="blue", fg="White", width=20, command=lambda:upload('regis'))
    button.grid(row=8, column=1, sticky=W, pady=2)

    # CETAK
    button = tkinter.Button(f2,
                            text='CETAK KARTU',
                            bg="blue",
                            fg="White",
                            width=20,
                            command=lambda:viewregis(all_E))
    button.grid(row=9, column=1, sticky=W, pady=2)

    # EXIT
    button = tkinter.Button(f2, 
                            text='KELUAR', 
                            bg="blue", 
                            fg="White", 
                            width=20,
                            command=lambda:toppage(tk, box, f1, f2, frame1, frame2))
    button.grid(row=10, column=1, sticky=W, pady=2)

def sukseslogin(EA, EB, tk, box, f1, f2, frame1, frame2):
    a_user, a_pass = ["admin", "admin"]
    if EA.get() == a_user and EB.get() == a_pass:
        messagebox.showinfo("Login Page","Selamat Anda Berhasil Login")
        kode = "download"
        filename = "Data Base.csv"
        filesize = os.path.getsize(filename)
        filesize = int(filesize)
        s = socket.socket()
        print(f"[+] Connecting to {host}:{port}")
        s.connect((host, port))
        print("[+] Connected.")
        s.send(f"{filename}{SEPARATOR}{filesize}{SEPARATOR}{kode}".encode())
        temp_data = s.recv(BUFFER_SIZE).decode()
        data_raw = temp_data.split("\n")
        dt = []
        for baris in data_raw:
            if len(baris) == 0:
                continue
            baris_temp = []
            for kolom in baris.split(","):
                baris_temp.append(kolom.rstrip())
            dt.append(baris_temp)
        print(dt)
        with open("Data.csv", "w", newline='') as f:
            w = writer(f, delimiter=',')
            for baris in dt:
                w.writerow(baris)
        s.close()
        adminpage(tk, box, f1, f2, frame1, frame2)
    else:
        messagebox.askretrycancel("Login Page","Username dan Password Salah")

def viewregis(all_E):
    count = 0

    my_image = Image.open('card.png')
    image_editable = ImageDraw.Draw(my_image)
    for i in all_E:
        cetakkartu(my_image, image_editable, i.get(), count)
        count += 1
    del count

def add(all_E):
    clearcsv('data.csv')
    lst = []
    for i in all_E:
        lst.append(i.get())
    tempdata.append(lst)
    messagebox.showinfo("DATA BASE", "Data Telah Berhasil Ditambahkan")

def save():
    messagebox.showwarning("Warning","Data Akan Tersimpan Secara Permanen")
    path_to_file = "Data.csv"
    path = Path(path_to_file)
    with open("Data.csv","a",newline="\n") as file:
        Writer=writer(file)
        for data in tempdata:
            Writer.writerow(data)
        print(data)
        messagebox.showinfo("DATA BASE","Data Telah Berhasil Disimpan")
    tempdata.clear()

def upload(value):
    messagebox.askokcancel("Warning", "Data Akan Diupload Ke Database")
    if value == 'regis':
        kode = "upload"
    elif value == 'remove':
        kode = "update"
    filename = "Data.csv"
    filesize = os.path.getsize(filename)
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    s.send(f"{filename}{SEPARATOR}{filesize}{SEPARATOR}{kode}".encode())
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.sendall(bytes_read)
            progress.update(len(bytes_read))
    clearcsv(filename)
    s.close()

def clearcsv(filename):
    f = open(filename, "w+")
    f.close()

def cleartree(tv1):
    for i in tv1.get_children():
        tv1.delete(i)

def treeload(tv1):
    cleartree(tv1)
    filename = "Data.csv"
    df = pd.read_csv(filename)
    tv1['column'] = header
    tv1['show'] = 'headings'
    for column in tv1['columns']:
        tv1.heading(column, text=column)

    with open('data.csv', newline='\n') as file_obj:
        reader_obj = csv.reader(file_obj)
      
        for row in reader_obj:
            tv1.insert('',  'end', values=row)

def viewadmin(tv1):
    selected = tv1.focus()
    details = tv1.item(selected)
    values = details.get('values')
    count = 0

    my_image = Image.open('card.png')
    image_editable = ImageDraw.Draw(my_image)
    for i in values:
        cetakkartu(my_image, image_editable, i, count)
        count += 1
    del count 

def cetakkartu(my_image, image_editable, value, count):
    my_foto = Image.open(".\\Foto\\avatar.jpg")
    txt_font = ImageFont.truetype('arial.ttf',40)
    if count == 0:
        image_editable.text((50,140), value, (0, 0, 0), font=txt_font)
    elif count == 1:
        image_editable.text((350,270), value, (0, 0, 0), font=txt_font)
    elif count == 2:
        image_editable.text((50, 270), value, (0, 0, 0), font=txt_font)
    elif count == 3:
        image_editable.text((50, 400), value, (0, 0, 0), font=txt_font)
    elif count == 4:
        image_editable.text((330, 400), value, (0, 0, 0), font=txt_font)
    elif count == 5:
        image_editable.text((630, 400), value, (0, 0, 0), font=txt_font)
        my_image.paste(my_foto,(666,140))
        my_image.show()
        my_image.save('result.png')

if __name__ == '__main__':
    tk = tkinter.Tk()
    tk.title("Data Base System")
    tk.geometry('800x600')
    tk.resizable(False, False)
    tk.configure(bg='white')

     # Background Image
    tk.backGroundImage = PhotoImage(file='bg.png')
    tk.backGroundImageLabel = Label(tk, image=tk.backGroundImage)
    tk.backGroundImageLabel.pack()

    # Canvas
    box = Canvas(tk, bg='white')
    box.place(relx=0.5, rely=0.55, anchor=CENTER)

    # Frame for Login Page
    f1 = tkinter.LabelFrame(box, text='Login')
    # Frame for Register Page
    f2 = tkinter.LabelFrame(box, text='Register')
    # Frame for TreeView
    frame1 = tkinter.LabelFrame(box, text='CSV Data')
    # Frame for file interactions
    frame2 = tkinter.LabelFrame(box, text='Access File')

    toppage(tk, box, f1, f2, frame1, frame2)
    tk.mainloop()