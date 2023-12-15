#Расходы на автомобиль. Напишите программу, которая просит пользователя ввести месячные расходы на следующие нужды, связанные с его автомобилем: платеж по кредиту, страховка, бензин, машинное масло, шины и техобслуживание.
#Затем программа должна показать общую месячную стоимость и общую годовую стоимость этих расходов.

def main():
    loan = float(input('Укажите ежемесячный платеж по кредиту за автомобиль: '))
    insurance = float(input('Укажите ежемесячный платеж по страховке за автомобиль: '))
    gas = float(input('Укажите ежемесячный расход на бензин: '))
    oil = float(input('Укажите ежемесячный расход на машинное масло: '))
    tires = float(input('Укажите ежемесячный расход на шины: '))
    maintenance = float(input('Укажиите ежемесячный расход на техобслуживание: '))
    month_expense = car_expense_month_calc(loan, insurance, gas, oil, tires, maintenance)
    year_expense = car_expense_year_calc(month_expense)
    print(f'Месячные расходы на автомобиль составляют {month_expense} руб.\nОбщая годовая стоимость расходов составляет {year_expense} руб')
def car_expense_month_calc(num1, num2, num3, num4, num5, num6):
    return (num1 + num2 + num3 + num4 +  num5 + num6)
def car_expense_year_calc(num):
    return num * 12
main()
