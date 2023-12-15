#Кинетическая энергия. Из физики известно, что движущееся тело имеет кинетическую энергию. Приведенная ниже формула может использоваться для определения кинетической энергии движущегося тела:
#KE = 1/2mv^2,
#где KE — это кинетическая энергия; m — масса тела, кг; v — скорость тела, м/с.
#Напишите функцию kinetic_energy, которая в качестве аргументов принимает массу тела (в килограммах) и его скорость (в метрах в секунду). Данная функция должна вернуть величину кинетической энергии этого тела.
#Напишите программу, которая просит пользователя ввести значения массы и скорости, а затем вызывает функцию kinetic_energy, чтобы получить кинетическую энергию тела.

def main():
    print('Данная программа предназначена для расчета кинетической энергии тела')
    print()
    mass = float(input('Введите массу тела в килограммах:'))
    speed = float(input('Введите скорость тела в м/с:'))
    ke = kinetic_energy(mass, speed)
    print(f'Кинетическая энергия тела равна {ke} Дж')
def kinetic_energy(mass, speed):
    return mass * speed ** 2 / 2
main()
