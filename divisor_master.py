#Реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000. Модуль содержит функции:
#1. проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами)

def prime_numbers(x):
    if x>0 and x<1000:
        for i in range(2, (x//2)+1):
            if x % i == 0:
                return 'Число не является простым'
        else:
            return 'Число является простым'
    else:
        return 'Ошибка. Пожалуйста введите число от 1 до 1000'

if __name__ == '__main__':
    print(prime_numbers(12))

#2. выводит список всех делителей числа
def number_divisor(x):
    if x > 0 and x < 1000:
        global divisor
        divisor = []
        for i in range(1, x+1):
            if x % i == 0:
                divisor.append(i)
        result = 'Все делители числа ' + str(x) + ' : ' + str(divisor)
        return result
    else:
        return 'Ошибка. Пожалуйста введите число от 1 до 1000'

if __name__ == '__main__':
    print(number_divisor(35))

#3. выводит самый большой простой делитель числа
def max_prime_divisor(x):
    prime_divisors = []
    number_divisor(x)
    for i in divisor:
        for l in range(2, ((i//2)+1)):
            if l % i == 0:
                continue
            else:
                prime_divisors.append(i)
    return prime_divisors

print(max_prime_divisor(35))