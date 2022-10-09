# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def main():
    k = int(input('Введите число: '))
    factors_list = []
    string = ''
    for i in range(k):
        factors_list.append(random.randint(0,100))
        print(factors_list)
    for j in range(k):
        if j < k:
            string += f'{factors_list[j]} x^{k - j} + '

        else:
            string += f'{factors_list[j]} x^{k - j} = 0'

    outfile = open('Ex4.txt', 'w')

    outfile.write(string)
    outfile.close()

main()

      