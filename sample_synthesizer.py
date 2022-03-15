from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
from base64 import b64encode
from secrets import token_hex
from random import randint
from os import path, mkdir
from sys import argv

def generate(mod, num):
    key = token_hex(3)

    img = Image.new(mode="RGB", size=(300, 100), color=(255, 255, 255))
    id = ImageDraw.Draw(img)
    if mod and "obstruct" in mod:
        for i in range(0, 10):
            id.line((randint(1, 300), randint(1, 100), randint(1, 300), randint(1, 100)), fill=128)
    font_large = ImageFont.truetype("fonts/DejaVuSansMono.ttf", size=20)
    x, y = (120+(randint(-2,2)*10), 40+(randint(-2,2)*10))
    id.text((x, y), key, font=font_large, fill=(0, 0, 0))
    
    img = img.filter(ImageFilter.SMOOTH_MORE)
    img = img.convert("L")
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixel = img.getpixel((i, j))
            if pixel < 90:
                img.putpixel((i,j), 0)
            else:
                img.putpixel((i,j), 255)
    img.save("./samples/test.png", format="PNG")

    tw, th = id.textsize(key, font=font_large)
    single = tw/len(key)
    for char_idx in range(len(key)):
        loc = x+(char_idx*(single))
        if not path.isdir(f"./samples/{key[char_idx]}"):
            mkdir(f"./samples/{key[char_idx]}")
        img.crop((loc, y, loc+single, y+th)).save(f"./samples/{key[char_idx]}/{num}.png", format="PNG")
for i in range(500):
    print(f"doing {i}")
    generate(["obstruct"], i)