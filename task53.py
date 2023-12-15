#Сидячие места на стадионе. На стадионе имеется три категории сидячих мест. Места класса A стоят 20 долларов, места класса B — 15 долларов, места класса C — 10 долларов.
#Напишите программу, которая запрашивает, сколько билетов каждого класса было продано, и затем выводит сумму дохода, полученного от продажи билетов.

CLASS_A = 'A'
CLASS_A_PRICE = 20
CLASS_B = 'B'
CLASS_B_PRICE = 15
CLASS_C = 'C'
CLASS_C_PRICE = 10
def main():
    a_class_sold = sold_input(CLASS_A)
    b_class_sold = sold_input(CLASS_B)
    c_class_sold = sold_input(CLASS_C)
    a_class = income_calc(a_class_sold, CLASS_A_PRICE)
    b_class = income_calc(b_class_sold, CLASS_B_PRICE)
    c_class = income_calc(c_class_sold, CLASS_C_PRICE)
    overall_income = sum_calc(a_class, b_class, c_class)
    print(f'Доход от продажи билетов составил {overall_income} рублей')
def sold_input(class_rate):
    sold_num = int(input(f'Сколько было продано билетов класса {class_rate}? '))
    return sold_num
def income_calc(sold, price):
    return sold * price
def sum_calc(summand1, summand2, summand3):
    return (summand1 + summand2 + summand3)
main()
