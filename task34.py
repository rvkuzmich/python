#Анализ бюджета. Напишите программу, которая просит пользователя ввести сумму, выделенную им на один месяц. Затем цикл должен предложить пользователю ввести суммы отдельных статей
#его расходов за месяц и подсчитать их нарастающим итогом. По завершению цикла программа должна вывести сэкономленную или перерасходованную сумму.

balance = float(input('Какую сумму вам выдали на месяц?'))
cost_item = int(input('Укажите количество статей расходов: '))
total = 0.0
for c in range(cost_item):
    expense = float(input(f'Укажите затраты по {c+1} статье расходов: '))
    total += expense
balance -= total
if balance > 0:
    print(f'Поздравляем, вам удалось сэкономить {balance} рублей!')
elif balance < 0:
    print(f'К сожалению, у вас перерасход {abs(balance)} рублей.')
else:
    print('Вы вышли в 0.')
