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

    #ODLEGLOSC PUNKTU OD DANEJ LINII - DO OBLICZANIA CERR
    def distance(self, x, y):
        coeff = self.coeff_get()
        dist = (-1*coeff[0]*x + y -coeff[1]) / math.sqrt((coeff[0]*coeff[0])+1)
        return abs(dist)

