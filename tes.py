from PIL import Image, ImageFont, ImageDraw 

my_image = Image.open("tes.png")
title_font = ImageFont.load_default()
title_text = "Gabriel Ramadhani"
image_editable = ImageDraw.Draw(my_image)
image_editable.text((15,15), title_text, (237, 230, 211), font=title_font)
my_image.save("result.png")
