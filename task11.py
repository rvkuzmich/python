#Процент учащихся обоего пола. Напишите программу, которая запрашивает у пользователя количество учащихся мужского и женского пола, зарегистрированных в учебной
#группе. Программа должна показать процент учащихся мужского и женского пола. Подсказка: предположим, что в учебной группе 8 юношей и 12 девушек, т. е. всего
#20 учащихся. Процент юношей можно рассчитать, как 8/20 = 0.4, или 40%. Процент девушек: 12/20 = 0.6, или 60%.
boys = int(input('Укажите количество юношей в группе'))
girls = int(input('Укажите количество девушек в группе'))
total = boys + girls
boyp = boys / total * 100
girlp = girls / total * 100
print(f'Процент юношей в группе составляет {boyp}%, процент девушек – {girlp}%')
