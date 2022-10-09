# Задайте натуральное число N. 
# Напишите программу, которая составит список 
# простых множителей числа N.

def main():
    i = 2
    multipliers = []
    num_n = int(input('Введите число: ')) 
    while i * i <= num_n:
        while num_n % i == 0:
            multipliers.append(i)
            num_n /= i
        i += 1
    if num_n > 1:
        multipliers.append(int(num_n))
    print(multipliers)

main()