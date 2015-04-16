# Quiz09
# Problema1
import math
def distancia(x1,y1,x2,y2):
	s= x2-x1
	z= y2-y1
	s1=s*s
	z1=z*z
	r= s1+z1
	r1= math.sqrt(r)
	print("La distancia entre x2 y x1 es: ",s)
	print("La distancia entre y2 y y1 es: ",z)
	return r1
x1=int(input("Dame el primer numero: "))
y1=int(input("Dame el segundo numero: "))
x2=int(input("Dame el tercer numero: "))
y2=int(input("Dame el cuarto numero: "))
d=distancia(x1,y1,x2,y2)
print("La hipotenusa de los puntos es: ", d)
