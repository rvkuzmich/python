#Мелкая монета для зарплаты. Напишите программу, которая вычисляет денежную сумму, которую человек заработает в течение периода времени, если в первый день его
#зарплата составит одну копейку, во второй день две копейки и каждый последующий день будет удваиваться. Программа должна запросить у пользователя количество дней,
#вывести таблицу, показывающую зарплату за каждый день, и затем показать заработную плату до налоговых и прочих удержаний в конце периода. Итоговый результат должен
#быть выведен в рублях, а не в количестве копеек.

days = int(input('Введите количество дней получения зарплаты мелкой монетой: '))
print('День\tЗарплата за день')
print('------------------------')
dsal = 1
salary = 0.0
for d in range(1, days+1):
    if d == 1:
        daily_salary = dsal / 100
    else:
        dsal += dsal
        daily_salary = dsal / 100
    salary += daily_salary
    print(d, daily_salary, sep = '\t')
    print()
print(f'Заработная плата за весь период до налоговых и прочих удержаний составит: {salary} рублей.')