def mcd(a, b):
	res = 0
	while(b > 0):
		res = b
		b = a % b
		a = res
	return a
 
# solicitamos los dos números
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
 
print("El máximo común divisor de ", num1," y ", num2," es ", mcd(num1, num2))
