"""Алгоритм сортировки выбором легко объясняется, код действительно достаточно простой
его недостаток в том что он медленно работает, время увеличивается вместе с увеличением массива.
Быстрее и лучше работает алгоритм Быстрая сортировка. Его тут нет."""

a = [3, 6, 4, 12, 44, 5, 64, 1, 7, 4, 7, 4, 2, 22, 7, 2, 7, 1, 7, -2, -6]

def findSmallest(arr):
    """
    Нахождение индекса, минимального значения в списке
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    """
    Функция сортировки выбором, которая так же использует предыдущию функцию
    """
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort(a))
