def hello():
    print('hello there')
    return 'hello'

hello()

value = hello()

print(value)

def multiple(*args):
    print (args)

multiple('andres', 1, {'hey': 'hello'}) #return a tuple

def mult_named(**kwargs):
    print(kwargs)

mult_named(first='Andres', last='Henriquez') #return a dictionary
