#Налог с продаж. Напишите программу, которая попросит пользователя ввести величину покупки. Затем программа должна вычислить федеральный и региональный налоги с продаж.
#Допустим, что федеральный налог с продаж составляет 5%, а региональный — 2.5%. Программа должна показать сумму покупки, федеральный налог с продаж, региональный налог с продаж,
#общий налог с продаж и общую сумму продажи (т. е. сумму покупки и общего налога с продаж). Подсказка: для представления 2.5% используйте значение 0.025, для представления 5% — 0.05.
subtotal = float(input('Введите величину покупки: '))
taxf = subtotal * 0.05
taxr = subtotal * 0.025
total = subtotal + taxf + taxr
print(f'Сумма покупки составила {subtotal:.2f}, ' + f'Федеральный налог с продаж составляет {taxf:.2f}, ' + f'Региональный налог с продаж составляет {taxr:.2f}, ' + f'Общий налог с продаж {taxf + taxr}, ' + f'Общая сумма продажи {total:.2f}')
