
class carta:
    def __init__(self, p, n):
        self.palo = p
        self.numero = n
    
    def strp(self, p):
        if p == 0:
            return "♠"
        elif p == 1:
            return "♥"
        elif p == 2:
            return "♣"
        elif p == 3:
            return "♦"
        else:
            return "-"
    def strp(self):
        return self.strp(self.palo)
    
    def strn(self, n):
        if n == 1:
            return "A"
        elif n == 11:
            return "J"
        elif n == 12:
            return "Q"
        elif n == 13:
            return "K"
        elif n > 0 and n < 14:
            return str(n)
        else:
            return "-"
    def strn(self):
        return self.strn(self.numero)
    
    def __str__(self, pretty):
        if pretty:
            text = self.strp()+" "+self.strn()
        else:
            text = str(self.palo)+" "+str(self.numero)
        return text