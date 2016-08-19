a = open('taras.txt', encoding='utf-8')

def sortA_Z(a):
    c = []
    a = sorted(a, key=len, reverse=True)
    for line in a[:5]:
    	c.append(line)
    return c
            

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = []
b = ''
a1 = str(a.read())
for i in a1.lower():
    if i in {'б', 'ґ', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'}:
        count1 += 1

    if i in {'а', 'е', 'и', 'і', 'о', 'у', 'є', 'ю', 'я', 'ї'}:
        count2 += 1

    if i == " ":
        count3 += 1

    if i in (',', '.', ';', ':', '-', '!', '?', '(', ')', '[', ']'):
        count4 += 1
    if i not in (' ', ',', '.', ';', ':', '-', '!', '?', '(', ')', '[', ']', '/', '\n', '\ufeff'):
        b+=i

    else:
        count5.append(b)
        b = ''

print("Гласных букв: ", count1,
      "\nСогласных букв: ", count2,
      "\nКоличество пробелов: ", count3,
      "\nКоличество знаков препинания: ", count4,
      "\nТоп-5 длинных слов: ", sortA_Z(count5))

