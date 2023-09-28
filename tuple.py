myTuple = (1, 2, 2, 3)

print(myTuple)

newList = list(myTuple)
newList.append('four')
newTuple = tuple(newList)

(one, *two, three) = newTuple

print(one)
print(two)
print(three)
print(newTuple)
