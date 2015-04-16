#Quiz09
#Problema4
def fibonacci(x):
	if(x==0) or (x==1):
		return(x)
	if(x>1):
		return fibonacci(x-1)+ fibonacci(x-2)
x=int(input("Dame una posición: "))
a=fibonacci(x)
print(a)
