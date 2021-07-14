import numpy as np
import sympy
import matplotlib.pyplot as plt
import math

class Vehicle:
  center_x = 0 #x srodka grawitacji
  center_y = 0 #y srodka grawitacji
  size_w = 0 #szerokosc
  size_h = 0 #dlugosc
  psi = 0  # kat odchylenia od osi
  v = 1  # pkt na jednostke czasu
  R = 1  # PROMIEN KRZYWIZNY ???
  w = 0  # predkosc katowa init
  at = 0  # przyspieszenie liniowe
  ar = 0 #przyspieszenie katowe
  corners = [] #wierzcholki pojazdu
  u = [] #wektor polozenia
  q = [] #wektor kontroli
  movement = []

  def __init__(self, size_x, size_y):
    self.size_w= size_x/2 #promien szerokosci samochodu
    self.size_h= size_y/2 #promien wysokosci samochodu

    self.corners = [[self.center_x-self.size_w, self.center_y-self.size_h],
                    [self.center_x+self.size_w, self.center_y-self.size_h],
                    [self.center_x+self.size_w, self.center_y+self.size_h],
                    [self.center_x-self.size_w, self.center_y+self.size_h]] #wspolrzedne wierzcholkow samochodu
    self.ar = self.v*self.v/self.R #przyspieszenie katowe INIT

    #self.u = [self.center_x, self.center_y, self.Psi] #wektor polozenia
    #self.q = [self.v, self.w] #wektor kontroli predkosci

  def get_corners(self):
    return self.corners

  def get_center(self):
    center = [self.center_x, self.center_y]
    return center

  def get_velocity(self):
    return self.v

  def corners_update(self, new_center_x, new_center_y):
    self.center_x=new_center_x
    self.center_y=new_center_y
    self.corners = [[self.center_x - self.size_w, self.center_y - self.size_h],
                    [self.center_x + self.size_w, self.center_y - self.size_h],
                    [self.center_x + self.size_w, self.center_y + self.size_h],
                    [self.center_x - self.size_w, self.center_y + self.size_h]]  # wspolrzedne wierzcholkow samochodu


  def angle_update(self, angle):
    self.psi = angle

  def rotate (self, alfa):
    self.angle_update(alfa)
    alfa_sin=(math.sin(math.radians(alfa)))
    alfa_cos=(math.cos(math.radians(alfa)))
    #angle check
    if alfa == 90:
      alfa_cos = 0
    if alfa == 0:
      alfa_sin = 0

    ax_x=0 #środek ukł współrzędnych
    ax_y=0
    curr_center=self.get_center()
    dist_x=curr_center[0]-ax_x #przesuniecie punktu srodkowego do centrum ukladu wspolrzednych
    dist_y=curr_center[1]-ax_y
    curr_corners=self.get_corners()
    updated_corners=[]
    #(math.sin(math.radians(alfa)))
    for i in curr_corners:
      curr_x = i[0]
      curr_y = i[1]
      moved_x = curr_x-dist_x
      moved_y = curr_y-dist_y #przesuniecie do poczatku ukladu wspolrzednych
      rot_x = moved_x * alfa_cos - moved_y * alfa_sin #transformacja wzgl poczatku ukladu wspolrzednych
      rot_y = moved_x * alfa_sin + moved_y * alfa_cos
      rot_x = rot_x+dist_x #powrot do poczatku ukladu wspolrzednych
      rot_y = rot_y+dist_y
      updated_corners.append([rot_x,rot_y])
    print(updated_corners)
    x_results = []
    y_results = []
    for j in updated_corners:
      x_results.append(j[0])
      y_results.append(j[1])
    x_results.append(x_results[0])
    y_results.append(y_results[0])
    plt.axis([-8, 8, -8, 8])

    plt.gca().set_aspect("equal")
    plt.plot(x_results, y_results)
    plt.grid(True)
    plt.show()


  def check_angle(self):
    corners = self.get_corners()
    center = self.get_center()
    reference = corners[1]
    len = self.w/2
    #do dokonczenia jesli bedzie potrzebna



  def move(self, refpath):
    #sprawdz gdzie jestes
    current_center = self.get_center()
    current_corners = self.get_corners()
    current_angle = self.psi
    ycerr = 2137
    ycerr_cross=[]
    #liczenie bledu YCERR - odleglosc xcyc od sciezki referencyjnej
    #BARDZO UPROSZCZONE tylko dla linii prostych pod kątem 0 lub 90


    if current_center[1] > refpath[0][1]:
      if current_center [1] < refpath[1][1]:
        ycerr_cross = [refpath[0][0], current_center[1]]
    else:
      ycerr_cross = [current_center[0], refpath[0][1]]

    ycerr = math.dist(current_center, ycerr_cross)
    #print(ycerr)

    #policzenie skladowych wektora predkosci
    psi_sin=(math.sin(math.radians(current_angle)))
    psi_cos=(math.cos(math.radians(current_angle)))
    if current_angle == 90:
      psi_cos = 0
    if current_angle == 0:
      psi_sin = 0
    current_velocity = self.get_velocity()
    vx = current_velocity * psi_cos
    vy = current_velocity * psi_sin

    #polozenie krok do przodu
    sim_x = current_center[0] + vx
    sim_y = current_center[1] + vy
    #print(sim_x, sim_y)


    #POLICZENIE BLEDU YERR
    if sim_y > refpath[0][1]:
      if sim_y < refpath[1][1]:
        yerr_cross = [refpath[0][0], sim_y]
    else:
      yerr_cross = [sim_x, refpath[0][1]]

    yerr = math.dist([sim_x, sim_y], yerr_cross)
    #print(yerr)

    #POLICZENIE BŁĘDU ODCHYLENIA
    err_helper = math.dist([sim_x, sim_y], current_center)
    err_angle = 0 #zalozenie dla konkretnego przypadku w celu testu
    #tutaj nalezy policzyc tanens miedzy styczna do sciezki, a odcinkiem err_helper, aby wyznaczyc blad odchylenia

    #POLICZENIE PID - teoria
    #w_controller = self.kp * yerr + self.kd * (d yerr / dt) + self.ki integral (yerr dt)

    #jedziemy do przodu
    #zebrane dane i ich wpływ - do przepracowania
    if ycerr == 0 and err_angle == 0:
      self.corners_update(sim_x, sim_y)




  def plot_corners(self):
    curr = self.get_corners()
    x_results = []
    y_results = []
    for i in curr:
      x_results.append(i[0])
      y_results.append(i[1])
    x_results.append(x_results[0])
    y_results.append(y_results[0])
    plt.gca().set_aspect("equal") #ustawienie rzędu wielkości danych na wykresie
    plt.axis([-8, 8, -8, 8])
    plt.plot(x_results, y_results)
    plt.grid(True)
    plt.show()





'''
v2=Vehicle(4,2)
v2.plot_corners()
v2.corners_update(4,4)
v2.plot_corners()
v2.rotate(30)
'''
path1 = [[0,0], [6,0]]
path2 = [[6,0], [6,6]]
v1 = Vehicle(2,2)
v1.plot_corners()

#path plotter
plot_xc = []
plot_yc = []

for i in range(6):
  v1.move(path1)
  center = v1.get_center()
  print(center)
  plot_xc.append(center[0])
  plot_yc.append(center[1])


plt.gca().set_aspect("equal")
plt.axis([-8, 8, -8, 8])
plt.plot(plot_xc, plot_yc, 'o', color='black');
plt.grid(True)
plt.show()