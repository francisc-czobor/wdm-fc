def func():
    print('miau')


def func2():
    return 'bau'


func()
print(func2())


def func3(ceva='altceva'):
    print(ceva)


func3('la multi ani')
func3()


def func4(param1, param2='def', param3='def3'):
    print(param1, param2, param3)


func4('miau', 'bau', param3='ceva')


def add(num1, num2):
    if type(num1) == type(num2) == type(10):
        print(num1 + num2)
    else:
        print('invalid params')


add(1, 2)
add('1', 2)
print()


def outer():
    print('inainte')

    def inner():
        print('inauntru')
        # outer()  dont do that

    print('dupa')
    inner()


outer()


x = 25
print(x)


# def functie(y):
#     print(x, y)
#
#
# functie(100)
# print(x)


def functie_cu_global():
    global x
    x = 100
    print(x)


functie_cu_global()
print(x)


lst = [1, 456, 8, 5, 2, -4]
print(list(filter(lambda num: num < 5, lst)))
print(list(map(lambda num: num ** 2, lst)))
