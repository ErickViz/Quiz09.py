#Quiz09
#Problema3
def superpower(x,y):
	c=0
	a=1
	while(c!=y):
		a=x*a
		c=c+1
	return a

x=int(input("Dame un numero: "))
y=int(input("Dame su exponencial: "))
p=superpower(x,y)
print(p)

