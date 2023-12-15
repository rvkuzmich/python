#Математический тест. Напишите программу, которая позволяет проводить простые математические тесты. Она должна показать два случайных числа, которые должны быть просуммированы вот так:
#  247
#+ 129
#Эта программа должна давать обучаемому возможность вводить ответ. Если ответ правильный, то должно быть показано поздравительное сообщение. Если ответ неправильный, то должно быть показано сообщение с правильным ответом.
import random
def main():
    go_on = 'д'
    print('Эта программа создана для проведения простых математических тестов')
    print()
    while go_on == 'д':
        num1 = random.randrange(1000)
        num2 = random.randrange(1000)
        print('Введите правильный ответ:')
        print(num1)
        print('+')
        print(num2)
        sum = int(input())
        if sum == num1 + num2:
            print('Поздравляем! Ваш ответ верный!')
        else:
            print(f'К сожалению вы ошиблись, правильный ответ {num1 + num2}')
        go_on = input('Продолжить? (д)а, (н)ет)')
        while go_on != 'д' and go_on != 'н':
            go_on = input('Продолжить? (д)а, (н)ет)')
main()