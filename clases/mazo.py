from carta import carta
from random import randint

class mazo:
    def __init__(self):
        self.cartas = []
    def __init__(self, order : bool):
        self.cartas = []
        for i in range(4):
            for j in range(1, 14):
                self.cartas.append(carta(i, j))
        if not order:
            self.mezclar()
    
    def mezclar(self):
        cartas1 = self.cartas
        cartas2 = []
        while len(cartas1) > 0:
            i = randint(0, len(cartas1)-1)
            cartas2.append(cartas1[i])
            cartas1.pop(i)
        self.cartas = cartas2