# Требуется сложить два целых числа А и В.
#
# Входные данные
# В единственной строке входного файла INPUT.TXT записаны два натуральных числа через пробел.
# Значения чисел не превышают 10^9.
#
# Выходные данные
# В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — сумму чисел А и В.
#
# Пример
# №	INPUT.TXT	OUTPUT.TXT
# 1	 2 3	    5

# Чтение входных данных из файла
with open('INPUT.TXT', 'r') as input_file:
    data = input_file.readline().split()
    a = int(data[0])
    b = int(data[1])

# Вычисление суммы
result = a + b

# Запись результата в выходной файл
with open('OUTPUT.TXT', 'w') as output_file:
    output_file.write(str(result))

print(result)