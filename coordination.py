import replit,random
Xr=Yr=Zr=0
P=[Xr,Yr,Zr]
replit.clear()
def location():
  global all
  for i in range(1000):
    a=random.randint(0,2)
    P[a]+=1
  xa = random.randint (1,360)
  ya = random.randint (1,360)
  za = random.randint (1,360)
  X = random.randint (0,P[0])
  Y = random.randint (0,P[1])
  Z = random.randint (0,P[2])
  finalx = (xa/360)*(2*(22/7)*(X/2))
  finaly = (ya/360)*(2*(22/7)*(Y/2))
  finalz = (za/360)*(2*(22/7)*(Z/2))
  print(finalx)
  print(finaly)
  print(finalz)
location()