#Quiz09
#Problema3
def superpower(x,y):
	c=0
	while(c!=y):
		a=pow(x,y)
		c=c+1
	return a

x=int(input("Dame un numero: "))
y=int(input("Dame su exponencial: "))
p=superpower(x,y)
print(p)
