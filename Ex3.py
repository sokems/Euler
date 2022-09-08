"""Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?"""

import math

num = 600851475143
i = math.ceil(math.sqrt(num))
j = 2
result = -1

while i > 2:
    check = False
    if num % i == 0:
        while j < i:
            if i % j == 0:
                check = True
                break
            j += 1
        if not check:
            result = i
    if result != -1:
        break
    j = 2
    i -= 1

print(result)