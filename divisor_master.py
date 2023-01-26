#Реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000. Модуль содержит функции:
#1. проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами)

def prime_numbers(x):
    if x>0 and x<1000:
        if x == 1:
            return 'Число ' + str(x) + ' не является простым'
        for i in range(2, (x//2)+1):
            if x % i == 0:
                return 'Число ' + str(x) + ' не является простым'
        else:
            return 'Число ' + str(x) + ' является простым'
    else:
        return 'Ошибка. Пожалуйста введите число от 1 до 1000'

if __name__ == '__main__':
    print(prime_numbers(5))
    print(prime_numbers(40))
    print(prime_numbers(34))

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
    print(number_divisor(5))
    print(number_divisor(40))
    print(number_divisor(34))

#3. выводит самый большой простой делитель числа
def max_prime_divisor(x):
    if x > 0 and x < 1000:
        prime_divisors = []
        number_divisor(x)
        for i in divisor:
            if i == 1:
                continue
            for l in range(2, (i//2)+1):
                if i % l == 0:
                    break
            else:
                prime_divisors.append(i)
        result = 'Самый большой простой делитель числа ' + str(x) + ' : ' + str(prime_divisors[-1])
        return result
    else:
        return 'Ошибка. Пожалуйста введите число от 1 до 1000'

if __name__ == '__main__':
    print(max_prime_divisor(5))
    print(max_prime_divisor(34))
    print(max_prime_divisor(40))