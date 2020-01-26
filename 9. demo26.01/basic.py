# numbers
z = 2.4
x = 12
y = 5.1

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)
# print(x ** y)

# strings

s1 = 'ana are mere'
s2 = 'don\'t'
# niciodata ghilimele!

# string formating
var_ana = 'Ana'
var_mere = 'mere'
sf = '{x} {t} are {y}.'.format(x=var_ana, y=var_mere, t='Almajanu')
# print(sf)

# lists
# print([1, 2, 3])
# print([1, 2.3, 'bau', [1, 2, 4]])

l = [1, 2, 3, 4, 5, 6, 7]
# print(l)

# tuples
t = (1, 2, 3, 4, 5, 6, 7)
# print(t)

# sets
s = {1, 2, 3, 4, 5, 6, 7}
# print(s)

# indexing
# print('string', s1[0])
# print('list', l[1])
# print('tuplu', t[2])
# # print('set', s[0]) nu se poate pentru ca seturile nu au ordine
# print('invers', l[-1])  # e echivalent cu l[len(l) - 1]

# slicing
# print(s1[4:7])
# print(l[4:])
# print(t[:5])
# print(l[:])
# print(l[0:5:2])
# print(l[::2])
# print(l[5:0])  # atentie ca nu da eroare
# print(l[::-1])

# len - length (lungime / marime)
# print('len', len(s1))
# print('len', len(l))
# print('len', len(t))
# print('len', len(s))

# mutability = proprietatea cuiva de a putea fi modificat
# s1[0] = 'A' string-urile sunt imutabile
s1_modificat = s1.upper()
# print(s1, s1_modificat)

l[0] = -1  # listele sunt mutabile
# print(l)

# t[0] = -1  # tuplurile NU sunt mutabile
# print(t)

'Listele sunt multimi omogene, dar tuplurile sunt neomogene.'
nume = ['Claudia', 'Franci', 'Alex', 'Andrada', 'Dan', 'Eric']
locatie = (12.123455, 98.142342, 24)  # latitudine, longitudine si orientare

# unicitate
set_nou = {1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3}  # elementele set-urilor sunt unice
# print(set_nou)

# exemple de metode
l.append(4)
l.extend([1, 2, 3])
l.pop(5)
# print(l)

set_nou.discard(5)
# print(set_nou)

lista_naspa = [1, 2, 3, 2, 1, 4, 3, 2, 3, 1, 1, 1, 1, 2]
lista_misto = list(set(lista_naspa))
# print(lista_misto)

lista_multe_randuri = [
    'primul',
    'al doilea',
    'al treilea',
    'al patrulea',
]
# print(lista_multe_randuri)

# dicts
d = {  # cheile trebuie sa fie imutabile
    1: 'bau',
    2: 'miau',
    'cheia3': 123,
    'cheia4': 'string',
    4: 12,
    (1, 'unu'): [1, 2, 3],
    # [1, 'unu']: [1, 2, 3], listele/seturile nu pot fi chei in dictionare
}
# print(d)
# print(d[(1, 'unu')])

d.pop(1)
# d[0] referentierea directa da eroare
ceva = d.get(0, 'altceva')
# print(list(d.keys()))
# print(list(d.values()))
# print(ceva)

# del d[0]

# print(d)

a = 2
b = 3
# print(a < b)
# print(a <= b)
# print(a > b)
# print(a >= b)
# print(a == b)
# print(a != b)
#
# print(1 == '1')
# print(1 != '1')
# print(1 == int('1'))
# print(str(1) == '1')
# print(type(1), type('1'))
# print(type(1) == type(2))
# print(isinstance(1, int))  # int, str, list, tuple, set, dict, bool etc.

# print(True and False)
# print(True or False)
# print(0 in [1, 2, 3])  # False
# print(1 in [1, 2, 3])  # True
# print(2 in d)  # merge pe liste, tupluri, seturi si dictionare

# if a > b:
#     print('da')
# elif a < b:
#     print('nu')
# else:
#     print('poate')

if (
    a > b
    and x > y
):
    pass

i = 0
while i < 5:
    # print(i ** 2)
    i += 1

# for elem in [1, 2, 3]:
#     print(elem)
#     if elem == 2:
#         break
# else:
#     print('gata')

tuple_ex = [(12, 43, 23), (54, 23, 1), (456, 45, 0), (1, 4, 6)]

# for x1, _, x2 in tuple_ex:  # tuple unpacking
#     print('elem1:', x1)
#     print('elem2:', x2)

# print(range(1000000000))
# print(list(range(5)))
#
# for i in range(len(tuple_ex)):
#     print(i, tuple_ex[i])

list1 = [1, 2, 3, 4, 5, 6]
list2 = []
for elem in list1:
    list2.append(elem ** elem)

print(list2)

print([elem ** elem for elem in list1])  # list comprehension
# [operatie for var_de_nume_pentru_elem in numele_struncturii_ordonate]

print([el * el for el in [elem ** elem for elem in list1]])
