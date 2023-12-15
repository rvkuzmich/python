#Средний балл и его уровень. Напишите программу, которая просит пользователя ввести пять экзаменационных оценок (баллов). Программа должна показать буквенный уровень для каждой оценки и средний балл. Предусмотрите в программе функции:
#• calc_average — функция должна принимать в качестве аргументов пять балльных оценок и возвращать средний балл;
#• determine_grade — функция должна принимать в качестве аргумента балльную оценку и возвращать буквенный уровень оценки, опираясь на классификацию.

output = 'Введите экзаменационную оценку:'
def main():
    print('Программа высчитывает средний балл и определяет уровень знаний')
    print()
    grade1 = grade_input(output)
    grade2 = grade_input(output)
    grade3 = grade_input(output)
    grade4 = grade_input(output)
    grade5 = grade_input(output)
    average = calc_average(grade1, grade2, grade3, grade4, grade5)
    grade = determine_grade(average)
    print(f'Ваш средний балл - {average}\nВаш уровень знаний - {grade}')
def grade_input(value):
    num = int(input(f'{value}'))
    return num
def calc_average(gr1, gr2, gr3, gr4, gr5):
    return ((gr1 + gr2 + gr3 + gr4 + gr5) / 5)
def determine_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80 and average < 90:
        return 'B'
    elif average >= 70 and average < 80:
        return 'C'
    elif average >= 60 and average < 70:
        return 'D'
    else:
        return 'F'
main()
