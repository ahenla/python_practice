custom_list = ["andres", "hiroko", "samuel", "romina"]

print("hiroko" in custom_list)

print(custom_list[0:3])

print(custom_list[1:])
print(custom_list[:2])
print(custom_list[:])

custom_list += ["Gato"]

custom_list += 'javiera'

print(custom_list)

custom_list.insert(0, "god")

print(custom_list)

custom_list[3:3] = ['kitty', 'puppy']

print(custom_list)

custom_list[3:5] = ['turtle', 'fish']

print(custom_list)

custom_list.remove('fish')
print(custom_list)

del custom_list[-7:]
print(custom_list)
