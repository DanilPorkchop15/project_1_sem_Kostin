# Вариант 12
# Дана строка-предложение на русском языке. Вывести самое короткое слово в
# предложении. Если таких слов несколько, то вывести последнее из них. Словом
# считать набор символов, не содержащий пробелов, знаков препинания и
# ограниченный пробелами, знаками препинания или началом/концом строки.
s = 'Всем привет! Меня зовут Данил Костин!!'
print(s)
marks = '''\@"()_+-/=.,'[]{};:%#<>~`*|№?!'''
for i in marks:
    s = s.replace(i, ' ')
try:
    print('Самое короткое слово в введенном предложении: ', min(s.split()[::-1], key=len))
except ValueError:
    print('Строка должна быть непустой')