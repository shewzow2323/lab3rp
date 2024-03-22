# x1 = (input("Введите первое число: - "))
# x2 = (input("Введите втророе число: - "))
# x3 = (input("Введите третье число: - "))
# min_by_list_X123 = min(x1, x2, x3)
# print("Ваш список чисел", x1, " ", x2, " ", x3, "Ваше минимальное число: ", min_by_list_X123)

# z1 = 3
# z2 = 3
# z3 = 0

# if 1< z1 <= 50:
#     print(z1)
# if 1< z2 <= 50:
#     print(z2)  
# if 1< z3 <= 50:
#     print(z3)  


# x1 = 4
# for x2 in range(1, 10):
#     print(x1*x2) 


# sum = 0
# count = 0
# print("Введите последовательность целых чисел (для завершения введите 0):")
# while True:
#     num = int(input("Введите число: "))
#     if num == 0:
#         break
#     sum += num
#     count += 1
# print("Сумма всех чисел: ", sum)
# print("Количество чисел: ", count)


# x = input("Введите слово, предложение или произвольный набор: ")

# countA = x.lower().count("а")
# replaceA = x.replace('а', '')

# print("После удаления символов 'а':", replaceA)
# print("Количество удаленных 'а':", countA)



# import sys

# array = [int(x) for x in sys.argv[1:]]
# max_e = max(array)

# count_small_max = sum(1 for num in array if num < max_e)
# sum_bolshe_5 = sum(num for num in array if num > 5)

# print("Максимальный элемент:", max_e)
# print("Количество чисел, меньших максимального:", count_small_max)
# print("Сумма чисел, больших 5:", sum_bolshe_5)

