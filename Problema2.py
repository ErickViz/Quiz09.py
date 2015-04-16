#Quiz09
#Problema2
def triangulo(x):
	c=0
	c2=1
	while(c!=x):
		a="T"
		m=a*c2
		print(m)
		c2=c2+1
		c=c+1
	if(c==x):
		c2=c2-2
		d=0
	for d in range(x):
			r=a*c2
			print(r)
			c2=c2-1
			d=d+1
	return m
x=int(input("Dame un numero"))
a=triangulo(x)
