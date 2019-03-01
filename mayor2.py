x=0
y=0
z=0
for i in range (0,11):
	i=int(input("inserte numero"))
	if i>0:
		x+=1
	elif i<0:
		y+=1
	elif i==0:
		z+=1
	print("numeros negativos",y,"numeros positivos",x,"iguales a cero",z)

