#Вычисление факториала числа. В математике запись в форме n! обозначает факториал неотрицательного целого числа n. Факториал n — это произведение всех неотрицательных целых чисел от 1 до n.
#Например, 7! = 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5040 и 4! = 1 x 2 x 3 x 4 = 24. Напишите программу, которая позволяет пользователю ввести неотрицательное целое число, а затем применяет цикл для
#вычисления факториала этого числа и показывает факториал.

num = int(input('Введите целое неотрицательное число: '))
fact = 1
for n in range(1, num+1):
    fact = fact * n
print(f'Факториал числа {num} равен {fact}')
