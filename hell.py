def fatorial(n):
	if n == 0:
		return 1
	else:
		return n * fatorial(n-1)
		
number = 5
result = fatorial(number)
print(f"O fatorial de {number} is {result}.") 
