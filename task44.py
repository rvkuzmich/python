#Популяция. Напишите программу, которая предсказывает приблизительный размер популяции организмов. Приложение должно использовать текстовые поля, чтобы дать пользователю ввести стартовое количество организмов,
#среднесуточное увеличение популяции (как процент) и количество дней, которые организмам будет дано на размножение.

population = float(input('Введите стартовое количество организмов популяции: '))
upscale = int(input('Введите среднесуточное увеличение популяции в процентах: '))
days = int(input('Введите количество дней для размножения: '))
print()
print('День\t\tПопуляция')
print('-------------------------')
for d in range(1, days+1):
    if d == 1:
        population += 0
        print(d, population, sep = '\t\t')
    else:
        population += population * upscale / 100
        print(f'{d}\t\t{population:.2f}')
