import numpy as np
import sympy
import matplotlib.pyplot as plt
import math
from Line import Line
from path_helper import *

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

  def center_update(self, new_center_x, new_center_y): #jesli jest modyfikowany kat odchylenia, ta funkcja aktualizuje centrum, a funkcja rotate zajmuje sie wierzcholkami
    self.center_x = new_center_x
    self.center_y = new_center_y

  def corners_update(self, new_center_x, new_center_y): #uzywany jesli chcemy przesunac samochod bez modyfikacji kata
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

    ax_x=0 #??rodek uk?? wsp????rz??dnych
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
    #print(updated_corners)

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
    #liczenie bledu YCERR - odleglosc centrum od sciezki referencyjnej
    if refpath[0][0] == refpath [1][0]: #przypadek ze odcinek nie jest funkcja
      ycerr = abs(current_center[0]-refpath[0][0])
    else:
      refline = formula(refpath[0][0], refpath[0][1], refpath[1][0], refpath[1][1])
      ycerr = refline.distance(current_center[0], current_center[1])
      print(ycerr)

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

    yerr_cross = []
    #POLICZENIE BLEDU YERR
    if refpath[0][0] == refpath [1][0]: #przypadek ze odcinek nie jest funkcja
      yerr = abs(sim_x-refpath[0][0])
    else:
      sim_refline = formula(refpath[0][0], refpath[0][1], refpath[1][0], refpath[1][1])
      yerr = sim_refline.distance(sim_x, sim_y)
      #print(yerr)

    #POLICZENIE B????DU ODCHYLENIA
    err_helper = math.dist([sim_x, sim_y], current_center)
    err_angle = angle_check(refpath[0], refpath[1]) - self.psi


    #POLICZENIE PID - teoria
    #w_controller = self.kp * yerr + self.kd * (d yerr / dt) + self.ki integral (yerr dt)

    #jedziemy do przodu
    #zebrane dane i ich wp??yw - do przepracowania
    if err_angle == 0:
      self.corners_update(sim_x, sim_y)
    else:
      #self.center_update(sim_x, sim_y)
      self.rotate(err_angle)
      new_angle = self.psi
      new_sin = (math.sin(math.radians(new_angle)))
      new_cos = (math.cos(math.radians(new_angle)))
      if new_angle == 90:
        new_cos = 0
      if new_angle == 0:
        new_sin = 0
      new_vel = self.get_velocity()
      new_vx = new_vel * new_cos
      new_vy = new_vel * new_sin

      self.corners_update(current_center[0] + new_vx, current_center[1] + new_vy)


  def plot_corners(self):
    curr = self.get_corners()
    x_results = []
    y_results = []
    for i in curr:
      x_results.append(i[0])
      y_results.append(i[1])
    x_results.append(x_results[0])
    y_results.append(y_results[0])
    plt.gca().set_aspect("equal") #ustawienie rz??du wielko??ci danych na wykresie
    plt.axis([-8, 8, -8, 8])
    plt.plot(x_results, y_results)
    plt.grid(True)
    plt.show()




path1 = [[0,0], [3,0]]
path2 = [[3,0], [3,8]]
v1 = Vehicle(2,2)
v1.plot_corners()

#path plotter
plot_xc = []
plot_yc = []

for i in range(3):
  v1.move(path1)
  center = v1.get_center()
  print(center)
  plot_xc.append(center[0])
  plot_yc.append(center[1])

print(v1.get_center())

for i in range(8):
  v1.move(path2)
  center = v1.get_center()
  #print(center)
  plot_xc.append(center[0])
  plot_yc.append(center[1])


plt.gca().set_aspect("equal")
plt.axis([-8, 8, -8, 8])
plt.plot(plot_xc, plot_yc, 'o', color='black');
plt.grid(True)
plt.show()