def t1():
 import json

 with open('products2.JSON', 'r', encoding='UTF-8') as file:
     data = json.load(file)
     for product in data['products']:
       print(f"Название: {product['name']} Цена: {product['price']}")
       print(f"Вес: {product['weight']}")
     if product['available']:
        print("В наличии")
     else:
      print("Нет в наличии!")
t1()

def t2():
    import json

    with open('products2.JSON', 'r', encoding='UTF-8') as file:
        data = json.load(file)
        name = input("Введите название продукта: ")
        price = int(input("Введите цену продукта: "))
        available = input("Доступен ли продукт (да/нет): ").lower() == 'да'
        weight = int(input("Введите вес продукта: "))

    newproduct = {
        "name": name,
        "price": price,
        "available": available,
        "weight": weight
    }

    data["products"].append(newproduct)

    with open('products2.JSON', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)

    print("Итоговой файл JSON:")
    print(json.dumps(data, indent=4))

t2()

def t3():
    import json
    file = {}
    with open('en-ru.txt', 'r', encoding='utf-8') as f:
        for line in f:
            en_word, ru_words = line.strip().split('-')
            for ru_word in ru_words.split(','):
                if ru_word not in file:
                    file[ru_word] = [en_word]
                else:
                    file[ru_word].append(en_word)

    with open('for10/ru-en.txt', 'w', encoding='utf-8') as f:
        for ru_word in sorted(file.keys()):
            en_words = ','.join(sorted(file[ru_word]))
            f.write(f'{ru_word}-{en_words}\n')

    with open('en-ru.json', 'w', encoding='utf-8') as f:
        json.dump(file, f, ensure_ascii=False, indent=4)

t3()