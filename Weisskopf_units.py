# Weisskopf Estimate Calculator/Unit Conversion
# C. Casarella 2015

import math

def BwE(A,L):
  """
  Weisskopf estimate for an electric-type transition of multipolarity L, for a nucleus of atomic number A
  """
  return 0.12**(2*L)/(4*math.pi)*(3/(L+3))**2*A**(2*L/3)/100**L

def BwM(A,L):
  """
  Weisskopf estimate for a magnetic-type transition of multipolarity L, for a nucleus of atomic number A
  """
  return BwE(A,L-1)*40*((L+2)/(L+3))**2

A_in=int(input("A=? ",))

print("For an E1 in A="+str(A_in)+", 1 mW.u. = "+str(1000*BwE(A_in,1)),"e$^2$b")
print("For an E2 in A="+str(A_in)+", 1 W.u. = " +str( BwE(A_in,2)    ),"e$^2$b$^2$")
print("For an E3 in A="+str(A_in)+", 1 W.u. = " +str( BwE(A_in,3)    ),"e$^2$b$^3$")
print("For an M1 in A="+str(A_in)+", 1 W.u. = " +str( BwM(A_in,1)    ),"$\mu_N^2$")