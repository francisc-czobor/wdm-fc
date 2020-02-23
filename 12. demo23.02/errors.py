try:
    print('da')
    # print(asdas)
    print(1/0)
    print('nu')
except ZeroDivisionError:
    print('asta se intampla daca am impartit la 0')
except NameError:
    print('asta se intampla daca folosim variabile nedeclarate')
else:
    print('asta se intampla daca nu e nicio eroare')
finally:
    print('asta se intampla mereu')

# else-ul necesita macar un except, dar finally merge singurel

print('asdasdas')


class SmthError(BaseException):
    pass


try:
    raise SmthError
except SmthError:
    print('tzeapa')
except:  # niciodata nu scrieti asa ceva
    print('altceva')
