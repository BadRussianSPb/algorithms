def even_namb(n, k, evens=0):
    if k == 0:
        return evens
    else:
        if (n % 10) % 2 == 0:
            return even_namb(n // 10, k - 1, evens + 1)
        else:
            return even_namb(n // 10, k - 1, evens)


n = input('Введите натуральное число: ')
k = len(n)
n = int(n)
result = even_namb(n, k)
k -= result
print('Нечетных числе:', k, '. Четных чисел:', result)
