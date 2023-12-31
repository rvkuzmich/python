#Сложный процент. Когда банк начисляет процентный доход по сложной ставке на остаток счета, он начисляет процентный доход не только на основную сумму, которая была внесена на депозитный счет,
#но и на процентный доход, который накапливался в течение долгого времени. Предположим, что вы хотите внести немного денег на сберегательный счет и заработать доход по сложной ставке в течение определенного
#количества лет. Ниже приведена формула для вычисления остатка счета после конкретного количества лет:
#A = P(1+r/n)^nt
#где A — денежная сумма на счете после конкретного количества лет; P — основная сумма, которая была внесена на счет в начале; r — годовая процентная ставка; n — частота начисления процентного дохода в год;
#t — конкретное количество лет. Напишите программу, которая выполняет для вас расчеты. Программа должна попросить пользователя ввести:
#• основную сумму, внесенную на сберегательный счет в самом начале;
#• годовую процентную ставку, начисляемую на остаток счета;
#• частоту начисления процентного дохода в год (например, если проценты начисляются ежемесячно, то ввести 12; если процентный доход начисляется ежеквартально, то ввести 4);
#• количество лет, в течение которых сберегательный счет будет зарабатывать процентный доход.
#После того как входные данные будут введены, программа должна рассчитать и показать сумму денег, которая будет на счету после заданного количества лет.
p = float(input('Введите основную сумму, внесенную на сберегательный счет: '))
r = float(input('Укажите годовую процентную ставку: ')) / 100
n = float(input('Укажите частоту начисления процентного дохода в год: '))
t = int(input('Укажите количество лет, в течение которых сберегательный счет будет зарабатывать процентный доход: '))
a = p * (1 + r / n) ** (n * t)
print(f'Через {t} лет у вас будет {a:.2f} рублей')
