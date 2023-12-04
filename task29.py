#Калькулятор времени. Напишите программу, которая просит пользователя ввести количество секунд и работает следующим образом.
#• В минуте 60 секунд. Если число введенных пользователем секунд больше или равно 60, то программа должна преобразовать число секунд в минуты и секунды.
#• В часе 3 600 секунд. Если число введенных пользователем секунд больше или равно 3 600, то программа должна преобразовать число секунд в часы, минуты и секунды.
#• В дне 86 400 секунд. Если число введенных пользователем секунд больше или равно 86 400, то программа должна преобразовать число секунд в дни, часы, минуты и секунды.
seconds = int(input('Введите желаемое количество секунд: '))
if seconds >= 60 and seconds < 3600:
    minutes = seconds // 60
    new_sec = seconds - (minutes * 60)
    print(f'Преобразованное число - {minutes} минут и {new_sec} секунд')
elif seconds >= 3600 and seconds < 86400:
    hour = seconds // 3600
    new_sec = seconds - (hour*3600)
    if new_sec >= 60:
        minutes = new_sec // 60
        new_sec = new_sec - (minutes * 60)
    else:
        minutes = 0
    print(f'Преобразованное число - {hour} часов {minutes} минут и {new_sec} секунд')
elif seconds >= 86400:
    days = seconds // 86400
    new_sec = seconds - (days*86400)
    if new_sec >= 3600 and new_sec < 86400:
        hour = new_sec // 3600
        new_sec = new_sec - (hour * 3600)
    else:
        hour = 0
    if new_sec >= 60 and new_sec < 3600:
        minutes = new_sec // 60
        new_sec = new_sec - (minutes * 60)
    else:
        minutes = 0
    print(f'Преобразованное число - {days} дней {hour} часов {minutes} минут и {new_sec} секунд')
