
#Задайте последовательность чисел. Напишите программу,
#которая выведет список неповторяющихся элементов исходной последовательности.
import random
from types import new_class

def main():
    
    sequence = []
    length = int(input('Введите длину списка: '))

    for i in range(length):
        casual = random.randint(1,11)
        sequence.append(casual)
    print(sequence)

    new_list = []
    [new_list.append(i) for i in sequence if i not in new_list]
    new_list.sort()

    print('список не повторяющихся элементов: ', new_list)

main()
