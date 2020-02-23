class Animal:
    def __init__(self, name, weight, colour):
        self.name = name
        self.weight = weight
        self.colour = colour

    def eat(self):
        print('munch')

    def say(self):
        print('generic animal noise...')


class Fotbalist(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('sanatos')


class Caine(Animal, Fotbalist):

    def __init__(self, name, weight, rasa, colour):
        Animal.__init__(self, 'bau', weight, colour)
        Fotbalist.__init__(self, name)
        self.rasa = rasa

    def say(self):
        print('ham ham')
        super(Caine, self).say()

    def scandeaza(self):
        print('hai Dinamo!')


class Pisica(Animal):

    def say(self):
        print('miau')


a = Animal('Marius', 68, 'alb')
a.eat()
a.say()
d = Caine('Clifford', 80, 'labrador', 'rosu')
d.eat()
d.say()
print(d.__dict__)
print(d.name)

d.scandeaza()
# a.scandeaza()  nu merge
