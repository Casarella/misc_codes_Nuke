# Recoil Velocity calculator for v1pgm (F(tau) calculation)
# Clark Casarella Mar 8, 2016
# Calculates recoil velocity of particle in units of c (s.o.l.)

import math

def recoil_beta(An,Aa,En):
  """
  Input parameters: 
  An -> nuclear weight of bombarding particle (1 for neutrons), 
  Aa -> total nuclear weight of target molecule  (Dy_2 O_3 = 162*2+16*3), 
  En -> (bombarding neutron energy in MeV)

  """
  return 0.04635*An/(An+Aa)*(En/An)**0.5

An=int(input("Bombarding particle A=? (1 for neutrons) ",))
Aa=int(input("Molecular Target mass number? (total weight) ",))
En=float(input("Bombarding particle Energy? (in MeV) ",))

#print(recoil_beta(1,162*2+16*3,1.6))
#print(recoil_beta(1,162*2+16*3,2.2))
#print(recoil_beta(1,162*2+16*3,3.1))

print('beta=',recoil_beta(An,Aa,En))