#Список простых чисел. Это упражнение предполагает, что вы уже написали функцию is_prime в упражнении 17. Напишите еще одну программу, которая показывает все простые числа от 1 до 100. В программе должен быть цикл, который вызывает функцию is_prime.

def main():
    print('Программа показывает все простые числа от 1 до 100')
    print()
    for number in range(1,101):
        if is_prime(number):
            print(number, end=' ')
def is_prime(value):
    for i in range(2, value):
        if value % i == 0:
            return False
    return True
main()
