import numpy as np
import Line

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
    new_a = y1 - y2 / x1 - x2
    new_b = y1 - new_a * x1
    result = Line(new_a, new_b)
    return result

line1 = Line(-2, 5)
line2 = Line(-1, 1)
print(cross(line1, line2))


