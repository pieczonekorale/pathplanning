import numpy as np
import matplotlib.pyplot as plt
import math

class Vehicle:
  center_x = 0 #x srodka grawitacji
  center_y = 0 #y srodka grawitacji
  size_w = 0 #szerokosc
  size_h = 0 #dlugosc
  Psi = 0  # kat odchylenia od osi
  v = 1  # pkt na jednostke czasu
  R = 1  # PROMIEN KRZYWIZNY ???
  w = 0  # predkosc katowa init
  at = 0  # przyspieszenie liniowe
  ar = 0 #przyspieszenie katowe
  corners = [] #wierzcholki pojazdu
  u = [] #wektor polozenia
  q = [] #wektor kontroli


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
    current = self.corners
    return current

  def get_center(self):
    center = [self.center_x, self.center_y]
    return center

  def corners_update(self, new_center_x, new_center_y):
    self.center_x=new_center_x
    self.center_y=new_center_y
    self.corners = [[self.center_x - self.size_w, self.center_y - self.size_h],
                    [self.center_x + self.size_w, self.center_y - self.size_h],
                    [self.center_x + self.size_w, self.center_y + self.size_h],
                    [self.center_x - self.size_w, self.center_y + self.size_h]]  # wspolrzedne wierzcholkow samochodu




  def rotate (self, alfa):
    alfa_sin=(math.sin(math.radians(alfa)))
    alfa_cos=(math.cos(math.radians(alfa)))
    #angle check
    if alfa == 90:
      alfa_cos =0
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






v2=Vehicle(4,2)
v2.plot_corners()
v2.corners_update(4,4)
v2.plot_corners()
v2.rotate(30)