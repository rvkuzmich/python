#Калькулятор сосисок для пикника. Допустим, что сосиски упакованы в пакеты по 10 штук, а булочки — в пакеты по 8 штук. Напишите программу, которая вычисляет
#количество упаковок с сосисками и количество упаковок с булочками, необходимых для пикника с минимальными остатками. Программа должна запросить у пользователя
#количество участников пикника и количество хот-догов, которые будут предложены каждому участнику. Программа должна показать приведенные ниже подробности:
#• минимально необходимое количество упаковок с сосисками;
#• минимально необходимое количество упаковок с булочками;
#• количество оставшихся сосисок;
#• количество оставшихся булочек.
import math
sausage_bag = 10
bun_bag = 8
participant = int(input('Введите количество участников пикника: '))
hot_dogs_n = float(input('Сколько хот-догов получит каждый участник? '))
hot_dogs = participant * hot_dogs_n
min_sausage_bags = math.ceil(hot_dogs / sausage_bag)
min_bun_bags = math.ceil(hot_dogs / bun_bag)
sausage_left = int(min_sausage_bags * sausage_bag - hot_dogs)
bun_left = int(min_bun_bags * bun_bag - hot_dogs)
print (f'Минимально необходимое количество упаковок с сосисками: {min_sausage_bags}')
print (f'Минимально необходимое количество упаковок с булочками: {min_bun_bags}')
print (f'Количество оставшихся сосисок: {sausage_left}, количество оставщихся булочек: {bun_left}')
