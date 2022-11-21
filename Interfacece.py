import tkinter
from tkinter import *
from PIL import Image, ImageFont, ImageDraw 

def click():
    my_image = Image.open("tes.png")
    title_font = ImageFont.truetype("arial.ttf",50)
    title_text = "Gabriel Ramadhani"
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((50,140), title_text, (0, 0, 0), font=title_font)
    my_image.show()
    my_image.save("result.png")
    
tk = tkinter.Tk()
tk.title("Data Base System")
canvas=tkinter.Canvas(tk, width=300, height=300)
canvas.pack()
L1 = Label(tk, text="Nama")
L1.pack(side = LEFT)
button=tkinter.Button(tk, text='Enter', bg="Purple", fg="White", width=10, command=click)
button.pack(side = BOTTOM)
tk.mainloop()