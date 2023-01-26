def factor_num(x):
    number = x
    i = 2
    global prim_fact
    prim_fact = []
    while i * i <= x:
        while x % i == 0:
            prim_fact.append(i)
            x //= i
        i += 1
    if x > 1:
        prim_fact.append(x)

    prim_fact.sort()
    num_dict = dict()

    dict_degree = {
        0: "\u2070",
        1: "",
        2: "\u00B2",
        3: "\u00B3",
        4: "\u2074",
        5: "\u2075",
        6: "\u2076",
        7: "\u2077",
        8: "\u2078",
        9: "\u2079",
        10: "\u00B9" + "\u2070",
        11: "\u00B9" + "\u00B9"
    }

    for i in prim_fact:
        if i in num_dict:
            num_dict[i] += 1
        else:
            num_dict[i] = 1
    degree_numbers = []
    for key, value in num_dict.items():
        degree_numbers.append(str(key) + dict_degree[value])

    result = str(number) + ' = '

    for i in degree_numbers:
        result += i + ' * '

    return  result[:-2]

if __name__ == '__main__':
    print(factor_num(500))
    print(factor_num(332))
    print(factor_num(2844))
    print(factor_num(21412543634))

def max_divisor(x):
    factor_num(x)
    result = 'Самый большой делитель числа ' + str(x) + ' : ' + str(prim_fact[-1])
    return result

if __name__ == '__main__':
    print(max_divisor(500))
    print(max_divisor(332))
    print(max_divisor(2844))
    print(max_divisor(21412543634))