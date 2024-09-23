def capitals():
    dict_capitals={
        'Франция': 'Париж', 'Германия': 'Берлин', 'Италия': 'Рим',
        'Испания': 'Мадрид', 'Португалия': 'Лиссабон', 'Австрия': 'Вена'
    }
    country = input("Введите страну, чтобы узнать её столицу: ")
    if country in dict_capitals:
        print(f"Столица {country} - {dict_capitals[country]}")
    else:
        print("Такая страна не найдена в списке.")
    sorted_countries = sorted(dict_capitals.keys())
    print("\nСтраны в алфавитном порядке:")
    for country in sorted_countries:
        print(f"{country} - {dict_capitals[country]}")
capitals()

def erudit():
    score={
        1 : ['А','В','Е','И','Н','О','Р','С','Т'],
        2 : ['Д','К','Л','М','П','У'],
        3 : ['Б','Г','Ё','Ь','Я'],
        4 : ['Й','Ы'],
        5 : ['Ж','З','Х','Ц','Ч'],
        8 : ['Ш','Э','Ю',],
        10 : ['Ф','Щ','Ъ',]
    }
    userword = input("Введите слово ")
    userword=userword.upper()
    d=0
    for i in userword:
        for k in score:
            if i in score[k]:
                d+=k
    print('Ваши очки в игре эрудит: ' , d)
erudit()