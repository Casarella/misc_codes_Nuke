#
#
#
#
#
#
#
#
#nuclide="Dy"
#A=160
#Z=66
#N=A-Z
Arange1=187
Arange2=141
fulllist=[[162,66],[146,62],[148,62],[150,62],[152,62],[154,62],[152,64],[154,66],[156,66],[174,70],[176,70],[174,72],[180,72],[182,72]]
Arange=list(range(Arange2,Arange1))
Zrange=list(range(57,78))
rangeIndexA=list(range(len(Arange)))
rangeIndexZ=list(range(len(Zrange)))
w,h=3,187-141
#print('Arange=',Arange)
#print('Zrange=',Zrange)
#print('rangeindexA=',rangeIndexA)
#print('rangeindexZ=',rangeIndexZ)
Matrix=[[[0 for x in range(w)] for y in range(h)]for z in range(len(Zrange))] 
for indZ in rangeIndexZ:
  for indA in rangeIndexA:
    Matrix[indZ][indA][1]=Zrange[indZ]
    Matrix[indZ][indA][0]=Arange[indA]

#for indZ in rangeIndexZ:
#  print(Matrix[0][indZ])
#  print(Matrix[15][indZ])
#print(Matrix[0][0])
#print(Matrix[0][1])
#print(Matrix[0][2])

#print('Calculate the Binding Energies needed')
#print('for gap.f for',A,nuclide,":")
sethelp=[-5,-3,-2,-1,0,1,3,5]
for indlist in fulllist:
  A=indlist[0]
  Z=indlist[1]
  if Z==62:
    nuclideF='Sm'
  elif Z==64:
    nuclideF='Gd'
  elif Z==66:
    nuclideF='Dy'
  elif Z==68:
    nuclideF='Er'
  elif Z==70:
    nuclideF='Yb'
  elif Z==72:
    nuclideF='Hf'
  print(nuclideF, A, 'p')
#proton gap
  for ind in sethelp:
    Znew=Z+ind
    Anew=A+ind
    if Znew==77:
      nuclideNew="Ir"
    elif Znew==76:
      nuclideNew="Os" 
    elif Znew==75:
      nuclideNew="Re" 
    elif Znew==74:
      nuclideNew="W"  
    elif Znew==73:
      nuclideNew="Ta" 
    elif Znew==72:
      nuclideNew="Hf" 
    elif Znew==71:
      nuclideNew="Lu" 
    elif Znew==70:
      nuclideNew="Yb" 
    elif Znew==69:
      nuclideNew="Tm" 
    elif Znew==68:
      nuclideNew="Er" 
    elif Znew==67:
      nuclideNew="Ho" 
    elif Znew==66:
      nuclideNew="Dy" 
    elif Znew==65:
      nuclideNew="Tb" 
    elif Znew==64:
      nuclideNew="Gd" 
    elif Znew==63:
      nuclideNew="Eu" 
    elif Znew==62:
      nuclideNew="Sm" 
    elif Znew==61:
      nuclideNew="Pm" 
    elif Znew==60:
      nuclideNew="Nd" 
    elif Znew==59:
      nuclideNew="Pr" 
    elif Znew==58:
      nuclideNew="Ce" 
    elif Znew==57:
      nuclideNew="La"
    print(Anew,nuclideNew)
  print(nuclideF, A, 'n')
  
   #neutron gap
  for ind in sethelp:
    Anew=A+ind
    print(Anew,nuclideF)