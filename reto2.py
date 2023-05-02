dist, velc, tiemp=input().split()
dist = float(dist)
velc = float(velc)
tiemp = float(tiemp)                     
velmax = (dist/1000) / (tiemp/3600) 
if (dist < 0 or velc < 0 or tiemp < 0):
   print("ERROR")
elif (velmax <= velc):
   print("OK")
elif (velmax > velc and velmax < velc *1.2):
   print("MULTA")
else:
   print("CURSO SENSIBILIZACION")
