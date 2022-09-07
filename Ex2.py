# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов
# будут: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

num1 = 1
num2 = 2
sumer = num2
i = 2
border = 4000000

print(num1, num2, sep=' ', end=' ')

while num2 <= border:
    temp = num1 + num2
    if temp > border:
        break
    num1 = num2
    num2 = temp
    print(num2, end=' ')
    if num2 % 2 == 0:
        sumer += num2

print()
print('Sum of even numbers:', sumer)
