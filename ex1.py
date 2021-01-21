def mcd(a, b):
	res = 0
	while(b > 0):
		res = b
		b = a % b
		a = res
	return a
 
# solicitamos los dos números
num1 = int(input("introdueix el primer número: "))
num2 = int(input("introdueix el segundo número: "))
 
print("El máximo común divisor de ", num1," y ", num2," es ", mcd(num1, num2))