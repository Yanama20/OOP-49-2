#O(1) Константная сложность
#Доступ к элементу списка по индексу

# def get_element(lst, index):
#     return lst[index]
#
# lst = [1,2,3,4,5]

#O(n) Линейная скорость
#Сумма элементов списка

# def sum_of_numbers(lst):
#     total = 0
#     for i in lst:
#         total += i
#     return total
# lst = [1,2,3,4,5,6,7,8,9,10]

#O(n^2)Квадратичная скорость
#Поиск всех пар в списке

# lst = [1,2,3]
# def pairs_in_list(lst):
#     pairs = []
#     for i in range(len(lst)):
#         for j in range(len(lst)):
#             pairs.append((lst[i], lst[j]))
#     return pairs
# print(pairs_in_list(lst))

#O(log(n))Логарифмическая скорость
#Бинарный поиск

# def binary_search(lst,target):
#     left, right = 0, len(lst)-1
#     result = 0
#     while left <= right:
#         middle = (left + right) // 2
#         if lst[middle] == target:
#             result = lst[middle]
#             break
#         elif lst[middle] < target:
#             right = middle - 1
#         elif lst[middle] > target:
#             left = middle + 1
#         return result
#
# lst = [1,2,3,4,5,6,7,8,9]
# print(binary_search(lst,6))

