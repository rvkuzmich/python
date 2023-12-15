#Месячный налог с продаж. Розничная компания должна зарегистрировать отчет о месячном налоге с продаж с указанием общего налога с продаж за месяц и взимаемых сумм муниципального и федерального налогов с продаж.
#Федеральный налог с продаж составляет 5%, муниципальный налог с продаж — 2,5%. Напишите программу, которая просит пользователя ввести общий объем продаж за месяц. Из этого значения приложение должно рассчитать и показать:
#• сумму муниципального налога с продаж;
#• сумму федерального налога с продаж;
#• общий налог с продаж (муниципальный плюс федеральный).

FEDERAL_TAX_RATE = 0.05
MUNICIPAL_TAX_RATE = 0.025
def main():
    sell_value = float(input('Введите общий объем продаж за месяц:'))
    municipal_tax = mt_calc(sell_value)
    federal_tax = ft_calc(sell_value)
    total_tax = sum_calc(municipal_tax, federal_tax)
    print(f'Муниципальный налог с продаж составил {municipal_tax:.2f} рублей\nфедеральный налог составил {federal_tax:.2f} рублей' +
    f'\nОбщий налог с продаж {total_tax:.2f} рублей')
def mt_calc(value):
    return value * MUNICIPAL_TAX_RATE
def ft_calc(value):
    return value * FEDERAL_TAX_RATE
def sum_calc(summand1, summand2):
    return summand1 + summand2
main()
