#Модернизация программы расчета налога с продаж. В упражнении 6 по программированию из главы 2 рассматривалась программа расчета налога с продаж. Требовалось написать программу,
#которая вычисляет и показывает региональный и федеральный налоги с продаж, взимаемые при покупке. Если эта программа уже вами написана, модернизируйте ее так, чтобы подзадачи
#были помещены в функции. Если вы ее еще не написали, то напишите с использованием функций.

def main():
    FEDERAL = 0.05
    REGIONAL = 0.025
    subtotal = float(input('Введите величину покупки: '))
    taxf = federal_tax_calc(subtotal)
    taxr = regional_tax_calc(subtotal)
    total = sum_calc_3num(subtotal, taxf, taxr)
    print(f'Сумма покупки составила {subtotal:.2f};\nФедеральный налог с продаж составляет {taxf:.2f};\nРегиональный налог с продаж составляет {taxr:.2f};\nОбщий налог с продаж {taxf + taxr};\nОбщая сумма продажи {total:.2f}')
def federal_tax_calc(num):
    return num * FEDERAL
def regional_tax_calc(num):
    return num * REGIONAL
def sum_calc_3num(num1, num2, num3):
    return (num1 + num2 + num3)
main()
