# вариант 12
# составить функцию суммирования числового ряда
def summ(a):  # функция, выводящая сумму числового ряда
    print(sum(a))


try: # обработчик исключений
    nums = map(int, input('Введите ряд чисел через пробел: ').split())  # ввод числового ряда через пробел
    summ(nums)  # вызов функции 
except Exception as ex:  # обработка исключений с выводом текста ошибки
    print(ex)
