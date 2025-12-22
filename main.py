def max_number(a, b):
    if a > b:
        return a
    if a < b:
        return b
    else:
        return "Values are same"

def empty_function():
    pass

def even_numbers(n):
    values = [numbers for numbers in range (0, n+1) if numbers % 2 == 0]
    for numeral in values:
        yield numeral

def test_max_number():
    assert max_number(0, 2) == 2, "Ошибка, Б должно быть больше, чем А"
    assert max_number(-3, -6) == -3, "Ошибка, А должно быть больше, чем Б "
    assert max_number(0, 0) == "Values are same", "Ошибка, значения одинаковы"


try:
    user_value = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
    exit()

for number in even_numbers(user_value): # пример работы функции even_numbers():
    print(number)


