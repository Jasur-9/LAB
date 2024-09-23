def t1():
 from PIL import Image
 a = "snwleopards.jpg"
 with Image.open(a)as img:
  img.load()
  im_crop = img.crop((350, 50, 600, 400))
  im_crop.save("cropped.jpg")
t1()
def t2():
    from PIL import Image
    открытки = {
        "День рождения": "birthday_card.jpg",
        "Новый год": "new_year_card.jpg",
        "8 Марта": "women_day_card.jpg",
        "День Победы": "victory_day_card.jpg"
    }

    праздник = input("Введите название праздника: ")
    имя_получателя = input("Введите имя человека, которого вы хотите поздравить: ")

    if праздник in открытки:
        card = открытки[праздник]
        print(f"Открытка для праздника '{праздник}':")
        img = Image.open(card)
        img.show()
    else:
        print("Извините, нет открытки для указанного праздника.")


t2()
from PIL import ImageDraw
from PIL import ImageFont
def t3():
    from PIL import Image
    открытки = {
        "День рождения": "birthday_card.jpg",
        "Новый год": "new_year_card.jpg",
        "8 Марта": "women_day_card.jpg",
        "День Победы": "victory_day_card.jpg"
    }

    праздник = input("Введите название праздника: ")
    name = input("Введите имя человека, которого вы хотите поздравить: ") + " , поздравляю!"

    if праздник in открытки:
        card = открытки[праздник]
        img = Image.open(card)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('arial.ttf', 36)
        draw.text((50, 50), name, font=font, fill=(0, 0, 100))
        img.save("congrats.png")
        img.show()
    else:
        print("Извините, нет открытки для указанного праздника.")
t3()