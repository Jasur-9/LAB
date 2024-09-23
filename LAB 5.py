def guessnum():
 import random
 random_numbers = [random.randint(1, 5) for _ in range(5)]
 user_number = int(input("Введите число: "))
 if user_number in random_numbers:
    print("Поздравляю, Вы угадали число!")
 else:
    print("Нет такого числа!")
 print("Исходный список:", random_numbers)

guessnum()

def rep():
 import random
 list = [random.randint(1, 10) for _ in range(5)]
 duplicates = []
 for item in list:
  if list.count(item)>1 and item not in duplicates:
        duplicates.append(item)
 if duplicates:
    print("Повторяющиеся элементы:", duplicates)
    print (list)
 else:
    print("Повторяющихся элементов нет")
    print(list)
rep()

def holidays():
 days=('Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье', )
 restdays=int(input("Сколько дней отдыха вы хотите?"))
 weekend=days[-restdays:]
 workdays=days[:-restdays]
 print("Ваши выходные дни:",",".join(weekend))
 print("Ваши рабочие дни:",",".join(workdays))
holidays()

def groups():
 import random
 group1 = ['Панков', 'Молчанова', 'Абрамо', 'Колесников', 'Кондратьев', 'Тихонов', 'Лебедева', 'Родионов', 'Медведев', 'Романова']
 group2 = ['Воробьев', 'Пономарева', 'Морозов', 'Филатов', 'Золотарева', 'Давыдова', 'Матвеева', 'Попов', 'Коновалов', 'Павлов']
 print("Группа 1:", group1)
 print("Группа 2:", group2)
 team1 = random.sample(group1, 5)
 team2 = random.sample(group2, 5)
 sport_team = tuple(team1 + team2)
 print("Спортивная команда:", sport_team)
 print("Длина кортежа:", len(sport_team))
 sorted_sport_team = sorted(sport_team)
 print("Отсортированная команда по алфавиту:", sorted_sport_team)
 ivanov_count = sport_team.count("Иванов")
 if ivanov_count > 0:
    print("Студент с фамилией 'Иванов' входит в команду. Количество вхождений:", ivanov_count)
 else:
    print("Студент с фамилией 'Иванов' нету в команде.")
groups()