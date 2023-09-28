value = 1

while value < 10:
    print(value)
    value += 1

print('')

value2 = 1

while value2 < 10:
    print(value2)

    if value2 == 5:
        break
    value2 += 1

print('')

value3 = 1

while value3 < 10:
    value3 += 1

    if value3 == 5: #no 5
        continue
    print(value3)

print('')

for x in 'HIROKO':
    print(x)

for x in range(0, 5): #5 not inclusive
    print(x)


for x in range (0, 100, 10):
    print(x)
else:
    print('100!')
