# numbers
a = 2.4
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
print(l)

# tuples
t = (1, 2, 3, 4, 5, 6, 7)
print(t)

# sets
s = {1, 2, 3, 4, 5, 6, 7}
print(s)

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

# dicts
lista_multe_randuri = [
    'primul',
    'al doilea',
    'al treilea'
]
print(lista_multe_randuri)
