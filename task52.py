#Калории за счет жиров и углеводов. Диетолог работает в спортивном клубе и дает рекомендации клиентам в отношении диеты. В рамках своих рекомендаций он запрашивает у клиентов количество граммов жиров и углеводов, которые они употребили за день.
#Затем на основе приведенной ниже формулы он вычисляет количество калорий, которые получаются в результате употребления жиров:
#калории от жиров = граммы жиров × 9.
#Затем на основе еще одной формулы он вычисляет количество калорий, которые получаются в результате употребления углеводов:
#калории от углеводов = граммы углеводов × 4.
#Диетолог просит вас написать программу, которая выполнит эти расчеты.
def main():
    daily_fat_consumtion = dfc_input()
    daily_carbohydrate_consumption = dcc_input()
    fat_calories = fat_cal_calc(daily_fat_consumtion)
    carbohydrate_calories = carbohydrate_cal_calc(daily_carbohydrate_consumption)
    print(f'В течение дня получено {fat_calories:d} калорий от жиров и {carbohydrate_calories} калорий от углеводов')
def dfc_input():
    fats = int(input('Укажите количество граммов жиров употребленных за день: '))
    return fats
def dcc_input():
    carbs = int(input('Укажите количество граммов углеводов употребленных за день: '))
    return carbs
def fat_cal_calc(val):
    fat_calories = val * 9
    return fat_calories
def carbohydrate_cal_calc(val):
    carb_calories = val * 4
    return carb_calories
main()
