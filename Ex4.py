"""
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром,
полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""

i = 999
j = 999
current = 0
max = 0

while i > 99:
    while j > 99:
        multi = i * j
        string = str(multi)
        multi_new = int(string[::-1])
        if ((multi == multi_new) and (multi > max)):
            max = multi
        j -= 1
    i -= 1
    j = 999

print(max)
