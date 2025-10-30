
class Carta:
    def __init__(self, p, n):
        self.palo = p
        self.numero = n
    
    def strp(self, p): # String palo
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
    def strsp(self): # String self palo
        return self.strp(self.palo)
    
    def strn(self, n): # String numero
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
    def strsn(self): # String self  numero
        return self.strn(self.numero)
    
    def __str__(self):
        text = self.strsn()+self.strsp()
        return text

    def literal_str(self):
        text = str(self.numero)+" "+str(self.palo)
        return text