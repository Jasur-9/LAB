def t1():
    import os
    from PIL import Image
    os.mkdir("photos")
    k = 0
    for i in os.listdir("great5"):
        img_path = os.path.join("great5", i)
        img = Image.open(img_path)
        img = img.resize((img.width // 3, img.height // 3))
        k += 1
        img.save(f"photos/img{k}.jpg")
t1()

def t2():
    import os
    from PIL import Image
    os.mkdir("photos")
    k = 0
    for i in os.listdir("great5"):
        if i.endswith(".jpg") or i.endswith(".png"):
         img_path = os.path.join("great5", i)
         img = Image.open(img_path)
         img = img.resize((img.width // 3, img.height // 3))
         k += 1
         img.save(f"photos/img{k}.jpg")
t2()

def t3():
    import csv
    result = 0
    print('Нужно купить:')
    with open('01data.csv') as file:
        file = csv.reader(file)
        for i in file:
            name = i[0]
            count = int(i[1])
            price = int(i[2])
            result += count * price
            print(f'{name} - {count} шт. за {price} руб.')
    print(f'Итоговая сумма: {result} руб.')
t3()