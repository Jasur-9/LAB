def t1():
  from PIL import Image
  a = "sw.jpg"
  with Image.open(a) as img:
   img.load()
   img.show()
   w, h = img.size
   format = img.format
   mode = img.mode
   print('Ширина: ',w)
   print('Высота: ',h)
   print('Формат: ', format)
   print('Цвет: ',mode)
t1()

def t2():
  from PIL import Image
  b="sw.jpg"
  with Image.open(b) as img:
   img.load()

   img2 = img.resize((img.width //3, img.height //3))
   img2.save('sw_resize.jpg')

   img3 = img.transpose(img2.FLIP_LEFT_RIGHT)
   img3.save("sw_flipped.jpg")

   img = img2.rotate(180)
   img = img.transpose(img2.FLIP_LEFT_RIGHT)
   img.save("sw_mir.jpg")

t2()

def t3():
    from PIL import Image, ImageFilter
    for i in range(1, 6):
        img = Image.open(str(i) + '.jpg')
        img = img.filter(ImageFilter.EMBOSS)
        img.save('embossed_' + str(i) + '.jpg')
t3()

def t4():
    from PIL import Image
    img = Image.open('sw.png')
    watermark = Image.open('mark.png')
    img.paste(watermark, (0,0), watermark)
    img.save('watermark.png')
t4()