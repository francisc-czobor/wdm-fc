print(type(1))
print(type(1.1))
print(type(True))
print(type('ceva'))
print(type([1, 2, 3]))
print(type({1: 'da', 2: 'nu'}))
print(type((1, 2)))

print('ceva'.upper())
print((1).real)
print((1).imag)
print(1.1.as_integer_ratio())
print((-.25).as_integer_ratio())


class Dulău:
    echipa_favorita = 'Dinamo'

    def __init__(self, nume, rasa, varsta):
        self.nume = nume
        self.rasa = rasa
        self.varsta = varsta
        self.nr_trofee = 0

    # object method
    def get_medie_trofee_per_an(self):
        return self.nr_trofee / self.varsta

    # class method
    @classmethod  # decorator
    def inhaitare(cls):
        print(cls.echipa_favorita)
        print('ma vad cu ultrasii asa putin asa asa putin nu mult caine-miu')

    # static method
    @staticmethod
    def scandeaza():
        print('Hai cainii rosii!')

    def __str__(self):
        # return '{nume}: {rasa}'.format(nume=self.nume, rasa=self.rasa)
        return ''.join([self.nume, ': ', self.rasa])
        # return self.nume + ': ' + self.rasa neoptimizata pls don't

    def __len__(self):
        return self.nr_trofee


rares = Dulău(nume='Rareș Costin Pârlea', rasa='Labador', varsta=17)
rares.tigari_fumate = 1000000
# rares = {
#     'rasa': 'Labador',
#     'varsta': 17,
#     'nr_trofee': 0,
#     'tigari_fumate': 1000000,
# }
print(type(rares))
print(rares)
print(str(rares))
print(rares.__init__)


def fumeaza():
    return 'IA UITE-L UNDE FUMEAZAAAA!'


rares.fumeaza = fumeaza
print(rares.fumeaza)
print(rares.fumeaza())

print(rares.__dict__)

rares.__dict__.pop('rasa')

print(rares.__dict__)
print(type(rares))
print(rares.__class__)

print(rares.echipa_favorita)
print(Dulău.__dict__)

rares.get_medie_trofee_per_an()
Dulău.get_medie_trofee_per_an(self=rares)

print(len(rares))

rares.inhaitare()
Dulău.inhaitare()
