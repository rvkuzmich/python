#Напишите программу, которая применяет вложенные циклы для рисования этого узора:
##
#  #
#   #
#    #
#     #
#      #

num_rows = 6
for r in range(num_rows):
    print('#', end = '')
    for c in range(r):
        print(' ', end = '')
    print('#')
