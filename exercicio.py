valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
par = 0

if valor2 < valor1:
    primeiro = valor2
    segundo = valor1

else:
    primeiro = valor1
    segundo = valor2

while primeiro <= segundo:
    if primeiro % 2 == 0:
        par += 1
    primeiro += 1

print(f'Entre os números escolhidos existem {par} números pares.')