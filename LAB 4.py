def divide3():
  usernum=int(input("Введите число для проверки: "))
  if usernum % 3 == 0:
    print("Это число делится на 3")
  else:
      print("Это число не делится на 3")
divide3()
def divide100():
    try:
     usernum=int(input("Введите число для деления на 100: "))
     result=usernum/100
     print("Результат деления на 100: " and result)
    except ValueError:
     print("Это не число.Введите число")
    except ZeroDivisionError:
     print("Введите число кроме 0")
divide100()
def magicdate():
    dateinput = input("Введите дату (ДД.ММ.ГГ.) ")
    try:
     day, month, year = map(int, dateinput.split("."))
     if day * month == int(str(year)[-2:]):
        print("Магическая дата")
        return True
     else:
        print("Не магическая дата")
        return False
    except  ValueError:
        print("Неправильно введена дата")

magicdate()


def is_lucky_ticket(ticket_number):
    if len(ticket_number) % 2 != 0:
        return False
    half_length = len(ticket_number) // 2
    first_half = map(int, ticket_number[:half_length])
    second_half = map(int, ticket_number[half_length:])
    return sum(first_half) == sum(second_half)
ticket_number = input("Введите номер билета: ")
if is_lucky_ticket(ticket_number):
    print("Билет счастливый!")
else:
    print("Билет не счастливый.")