# def myName(name):
#     print(name)
#     print(lastName)
#     lastName = "Henriquez" #defined after usage -> error

# myName(nombre)

# nombre = 'Andres' #defined after usage -> error


count = 0

def counter():
    # count += 1 -> can't modify global variable in the scope of a function
    global count #the global keyword let you access de global variable scope
    count += 1
    print(count)

counter()

def colorfull():
    color = 'blue'

    def change():
        # color = 'red' -> this won't work because is in a different scope
        nonlocal color #this will bring the color variable to this function's scope
        color = 'red'
        print(color)
    change()
    return color

print(colorfull())
