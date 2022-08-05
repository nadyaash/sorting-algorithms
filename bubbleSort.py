# Сортировка пузырьком.
# Каждую итерацию максимальный элемент «всплывает» как пузырек к концу массива
# O(n ** 2)

# 1
def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1): # на какое место будем ставим наибольший элемент
        for j in range(i): # проходим по не отсортированной последовательности
            if array[j] > array[j + 1]: # если порядок элементов неправильный
                # меняем местами пары
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array

print(bubble_sort([-8, 9, 4, 11, 3]))

# 2/ Реализация с оптимизацией
def bubble_sort_opt(array):
    for i in range(len(array) - 1, 0, -1):
        flag = False  # False - не было обменов, True - был хотя бы 1 обмен
        for j in range(i):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True  # меняем флажок

        if flag == False:  # если значение флага не поменялось
            return array


print(bubble_sort_opt([-8, 9, 4, 11, 3]))

# 3/сама.циклами. по возрастанию
def bubble_sama(lst): 
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

print(bubble_sama([-8, 9, 4, 11, 3]))
