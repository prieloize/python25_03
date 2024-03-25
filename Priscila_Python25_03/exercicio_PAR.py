import time
numero = int(input("Digite um numero inteiro positivo:"))

while numero<= 0:
    numero= float(input("Digite um numero positivo: "))

if numero % 2 == 0:
    print('"P-A-R!!!"')
else:
    print('Tente outra vez!')

time.sleep(5)