#Оценщик малярных работ. Малярная компания установила, что на каждые 10 квадратных метров поверхности стены требуется 5 литров краски и 8 часов работы. Компания взимает за работу 2000 руб. в час. Напишите программу,
#которая просит пользователя ввести площадь поверхности окрашиваемой стены и цену 5-литровой емкости краски. Программа должна показать следующие данные:
#• количество требуемых емкостей краски;
#• количество затраченных рабочих часов;
#• стоимость краски;
#• стоимость работы;
#• общая стоимость малярных работ.

import math
WORKHOUR_PRICE = 2000
WALL_SURFACE_HOURRATE = 0.8
WALL_SURFACE_PAINT_RATE = 0.1
def main():
    surface_square = float(input('Укажите площадь поверхности окрашиваемой стены в квадратных метрах: '))
    one_paint_price = float(input('Укажите стоимость 5-литровой емкости краски: '))
    paint_num = paint_num_calc(surface_square)
    workhours = workhours_calc(surface_square)
    paint_price = price_calc(paint_num, one_paint_price)
    works_price = works_price_calc(workhours)
    total_price = sum_calc(paint_price, works_price)
    print(f'На малярные работы потребуется:\n{paint_num} 5-литровых емкостей краски\n{workhours} часов работы\nСтоимость краски составит {paint_price:.2f} рублей' +
    f'\nСтоимость работ составит {works_price:.2f} рублей\nОбщая стоимость составит {total_price:.2f} рублей')
def paint_num_calc(square):
    return math.ceil(square * WALL_SURFACE_PAINT_RATE)
def workhours_calc(square):
    return math.ceil(square * WALL_SURFACE_HOURRATE)
def price_calc(pnum, pprice):
    return pnum * pprice
def works_price_calc(hours):
    return hours * WORKHOUR_PRICE
def sum_calc(summand1, summand2):
    return(summand1 + summand2)
main()
