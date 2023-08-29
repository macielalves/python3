num = input('Insira um valor entre 1000 e 9999: ').strip()
num_control = 4
n = num_control
def inversor(num):
	num = int(num)
	a = num // 1 % 10
	b = num // 10 % 10
	c = num // 100 % 10
	d = num // 1000 % 10
	return a, b, c, d
invert = ''.join(reversed(num))
n1, n2, n3, n4 = inversor(num)

print(f'{num} na ordem inversa é {invert[:n]}')#contem mais opções
print(f'{num} na ordem inversa é {n1}{n2}{n3}{n4}')#meio mais analógico