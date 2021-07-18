import numpy as np
from Line import Line
import math

#PUNKT PRZECIECIA 2 PROSTYCH
def cross(line1, line2):
    coeff1 = line1.coeff_get()
    coeff2 = line2.coeff_get()

    a2 = np.array([[-1*coeff1[0], 1], [-1*coeff2[0], 1]])
    b2 = np.array([coeff1[1], coeff2[1]])
    result = np.linalg.solve(a2, b2)
    return result

#WZOR PROSTEJ PRZECHODZACEJ PRZEZ 2 PUNKTY
def formula(x1, y1, x2, y2):
    new_a = (y1 - y2) / (x1 - x2)
    new_b = y1 - new_a * x1
    result = Line(new_a, new_b)
    return result

#ODCHYLENIE OD OSI X FRAGMENTU SCIEZKI
def angle_check(starter, finish):
    if starter[0]==finish[0]:
        return 90
    else:
        if starter[1]==finish[1]:
            return 0
        else:
            new_finish = [finish[0]-starter[0], finish[1]-starter[1]] #przesuniecie startera do punktu 00 i drugiego punktu odpowiednio wg. wspolrzednych startera
            a = new_finish[1] #przyprostokatna pionowa
            b = new_finish[0] #przyprostokatna pozioma
            angle = math.degrees(math.atan(a/b))
            return angle




