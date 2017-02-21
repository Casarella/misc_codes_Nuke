# SEMF - Semi-empirical mass formula calculator
#
# C. Casarella 2016
# Written for python3
#
# Input parameters, Z,A

def SEMF(Z,A):
  return aV*A-aS*A**(2/3)-aC*Z**2/A**(1/3)-aA*(A-2*Z)**2/A+delta


A=160
Z=66

Zm5=Z-5
Zm3=Z-3
Zm2=Z-2
Zm1=Z-1
Z0=Z
Z1=Z+1
Z3=Z+3
Z5=Z+5

Am5=A-5
Am3=A-3
Am2=A-2
Am1=A-1
A0=A
A1=A+1
A3=A+3
A5=A+5

aV=15.8
aS=18.3
aC=0.714
aA=23.2
aP=12

Pind=[[Zm5,Am5],[Zm3,Am3],[Zm2,Am2],[Zm1,Am1],[Z0,A0],[Z1,A1],[Z3,A3],[Z5,A5]]
Nind=[[Z,Am5],[Z,Am3],[Z,Am2],[Z,Am1],[Z,A0],[Z,A1],[Z,A3],[Z,A5]]
for ind in Pind :
  #print(ind)
  if ind[0]%2==0 and ind[1]%2==0:
    delta=aP/ind[1]**(1/2)
  elif ind[1]%2!=0:
    delta=0
  elif ind[0]%2!=0 and ind[1]%2==0:
    delta=-aP/ind[1]**(1/2)
  #print('delta =', delta)
  
print('Binding Energies for Proton Calculation')
#delta=11.18
for ind in Pind:
  print('For Z=', ind[0],'and A=', ind[1])
  print(round(SEMF(ind[0],ind[1]),3))
  

for indN in Nind:
  #print(indN)
  if indN[0]%2==0 and indN[1]%2==0:
    delta=aP/indN[1]**(1/2)
  elif indN[1]%2!=0:
    delta=0
  elif indN[0]%2!=0 and indN[1]%2==0:
    delta=-aP/indN[1]**(1/2)
 # print('delta =', delta)
print('Binding Energies for Neutron Calculation')
for indN in Nind:
  print('For Z=', indN[0],'and A=', indN[1])
  print(round(SEMF(indN[0],indN[1]),3))
  
print('Begin Proton/Neutron Pairing Gap')
#for jlist in Pind:
#  print(jlist)
#  for klist in jlist:
#    print(klist)
#    Zsemf[klist]=SEMF(klist,klist)

semfm3=round(SEMF(Pind[1][0],Pind[1][1]),3)+7
semfm1=round(SEMF(Pind[3][0],Pind[3][1]),3)+7
semf0= round(SEMF(Pind[4][0],Pind[4][1]),3)+7
semfp1=round(SEMF(Pind[5][0],Pind[5][1]),3)+7
semfp3=round(SEMF(Pind[6][0],Pind[6][1]),3)+7

print('M(Z-3)',semfm3)
print('M(Z-1)',semfm1)
print('M(Z)',semf0)
print('M(Z+3)',semfp1)
print('M(Z+3)',semfp3)
print('dummy')
print('', semf0)
print('',round(semf0+0.0625*semfm3,2))
print('',semf0+0.0625*semfm3-0.5625*semfm1)
print('',semf0+0.0625*semfm3-0.5625*semfm1-0.5625*semfp1)


print(semf0+0.0625*semfm3-0.5625*semfm1-0.5625*semfp1+0.0625*semfp3)


#print(-1000*2000*(SEMF(Pind[4][0],Pind[4][1])+0.0625*SEMF(Pind[1][0],Pind[1][1])-0.5625*SEMF(Pind[3][0],Pind[3][1])-0.5625*SEMF(Pind[5][0],Pind[5][1])+0.0625*SEMF(Pind[6][0],Pind[6][1])))


#deltaP=SEMF0-0.0625*SEMFm3-0.5625*SEMFm1-0.5625*SEMF1+0.00625*SEMF3
