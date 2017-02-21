# delta_correction.py 
# C. Casarella 2016
# converts multipole mixing fraction (delta) into a much more intuitive
# measure of multipolarity strength

import math

def percent_E2(delta):
  """
  Definition of E2 strength in terms of the multipole mixing fraction
  """
  return round(delta**2/(1+delta**2)*100,2)

def bounds_up_correction(delta,deltaup):
  return round(deltaup-delta,3)
def bounds_down_correction(delta,deltadown):
  return round(delta-deltadown,3)
def percent_E2_max(deltaup):
  return round(deltaup**2/(1+deltaup**2)*100,2)
def percent_E2_min(deltadown):
  return round(deltadown**2/(1+deltadown**2)*100,2)

delta_input=float(input('delta:'))
deltaup_input=float(input('delta_up:'))
deltadown_input=float(input('delta_down:'))

print(percent_E2(delta_input),'%','E2')
print(delta_input)
print(bounds_up_correction(delta_input,deltaup_input))
print(bounds_down_correction(delta_input,deltadown_input))
print('range:',percent_E2_max(deltaup_input),'-',percent_E2_min(deltadown_input),'%','E2')