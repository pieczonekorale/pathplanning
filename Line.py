import math

class Line:
    a = 0;
    b = 0;

    def __init__(self, def_a, def_b):
        self.a = def_a
        self.b = def_b

    def coeff_set(self, new_a, new_b):
        self.a = new_a
        self.b = new_b

    def coeff_get(self):
        coeff = [self.a, self.b]
        return coeff

    def angle_check(self):
        pass

    #ODLEGLOSC PUNKTU OD DANEJ LINII - DO OBLICZANIA CERR
    def distance(self, x, y):
        dist = (-1*self.a*x + y -self.b) / math.sqrt((self.a*self.a)+1)
        return dist

