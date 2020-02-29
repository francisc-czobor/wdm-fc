# COMMON METHODS #

# LISTS #

[1, 2, 3].pop()             # [1, 2] and it returns 3
[1, 2, 3].append(4)         # [1, 2, 3, 4]
[1, 2, 3].remove(2)         # [1, 3]
[1, 2, 3].index(3)          # 2
[1, 2, 3].extend([4, 5])    # [1, 2, 3, 4, 5]
[1, 2, 3].clear()           # []
[1, 3, 3].count(3)          # 2
[1, 2, 3].insert(1, 5)      # [1, 5, 2, 3]
[1, 2, 3].reverse()         # [3, 2, 1]
[3, 1, 2].sort()            # [1, 2, 3]

# TUPLES #

(1, 3, 3).count(3)          # 2
(1, 2, 3).index(2)          # 1

# SETS #

{1, 2, 3}.clear()           # {}
{1, 2, 3}.remove(2)         # {1, 3}
{1, 2, 3}.discard(2)        # {1, 3} dar nu dă eroare dacă elementul nu există în mulțime
{1, 2, 3}.pop()             # {2, 3} ? (șterge și întoarce un element arbitrar)
{1, 2, 3}.add(4)            # {1, 2, 3, 4} și nu are niciun efect dacă elementul există deja

# cu set-urile mai poți face toate operațiile pentru mulțimi: reuniune, intersecție etc.

# DICTS #

d = {
    1: 'ceva',
    'cheie': 'altceva',
    ('tuplu', 'unic'): -123,
}

d.pop(1)                    # scoate cheia 1
d.clear()                   # golește dicționarul
d.values()                  # ['ceva', 'altceva', -123]
d.keys()                    # [1, 'cheie', ('tuplu', 'unic')]
d.get('cheie')              # 'altceva'
d.items()                   # [(1, 'ceva'), ('cheie', 'altceva'), (('tuplu', 'unic'), -123)] adică lista de tupluri

# STRINGS #

''.join(['da', 'nu'])       # e mai complicat, caută documentația. funcție folosită foarte des
'da nu'.split(' ')          # ['da', 'nu']
'abc'.upper()               # 'ABC'
'ABC'.lower()               # 'abc'
'0 {} {}'.format('1', '2')  # '0 1 2'
'bau bau bau'.capitalize()  # 'Bau bau bau'

# și multe multe altele. citește lista de metode când ai nevoie de ceva anume că poate există
