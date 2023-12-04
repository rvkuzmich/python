#Цвета колеса рулетки. На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов:
#• карман 0 — зеленый;
#• для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером — черный;
#• для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером — красный;
#• для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером — черный;
#• для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером — красный.
#Напишите программу, которая просит пользователя ввести номер кармана и показывает, является ли этот карман зеленым, красным или черным.
#Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.
pocket_number = int(input('Введине номер кармана колеса: '))
if pocket_number < 0 or pocket_number > 36:
    print ('Ошибка! Число вне диапазона колеса.')
elif pocket_number == 0:
    print('Этот карман зеленый')
elif (pocket_number >= 1 and pocket_number <= 10) or (pocket_number >= 29 and pocket_number <= 36):
    if pocket_number % 2 == 0:
        print('Этот карман черный')
    else:
        print('Этот карман красный')
elif (pocket_number >= 11 and pocket_number <= 18) or (pocket_number >= 19 and pocket_number <= 28):
    if pocket_number % 2 == 0:
        print('Этот карман красный')
    else:
        print('Этот карман черный')
