# Вариант 12
# Дана непустая строка S и целое число N (> 0). Вывести строку, содержащую символы
# строки S, между которыми вставлено по N символов «*» (звездочка).
s = 'пример'
print(s)
n = int(input('Введите количество "*", которое будет между буквами строки (>0): '))
if n > 0 and len(s) > 0:
    print(f'Измененная строка:\n{("*" * n).join(s)}')
else:
    print('Строка должна быть непустой, а число должно быть больше нуля')