#ex05 sucessor e antecessor
n = int(input('Digite um número:'))
print(f'O número que você escolheu é {n} \n seu antecessor é {n-1}\n seu sucessor é {n+1}.')

#ex06 dobro, triplo e raiz
n = int(input('Digite um número'))
print(f'O número que você escolheu é {n} \n o Dobro desse número é {n*2}\n o Triplo desse número é {n*3}\n e a Raiz Quadrada deste número é {n**(1/2)}')

#ex07 média
p = int(input('Digite a nota da prova do Aluno'))
t = int(input('Digite a nota do trabalho do Aluno'))
print(f'A média bimestral deste aluno foi {(p+t)/2}')

#ex08 comprimento
c = int(input('Digite o tamanho em metros'))
print(f'{c}M em centímetros: {c*100} e em milímetros: {c*1000}')

#ex09 tabuada
n = int(input('Digite um número para ver sua tabuada:'))
print(f'Você escolheu o número {n}.')
print(f' {n}x1 = {n*1}\n {n}x2 = {n*2}\n {n}x3 = {n*3}\n {n}x4 = {n*4}\n {n}x5 = {n*5}\n {n}x6 = {n*6}\n {n}x7 = {n*7}\n {n}x8 = {n*8}\n {n}x9 = {n*9}\n {n}x10 = {n*10}')

#ex10 dolar por 3 reais (triste situação)
m = int(input('Digite o valor dos seus dinheiros'))
print(f'Você tem {m} dinheiros, então você pode comprar {m//3.27} dólares, restando {m%3.27} reais.')

#ex11 area e tinta
l = int(input('Digite a largura da parede em metros'))
a = int(input('Digite a altura da parede em metros'))
x = l * a
print(f'A área desta parede é de {x} metros quadrados, o que significa que você precisa de {x/2} litros de tinta.')

#ex12
preço = int(input('Preço do produto'))
desconto = preço * 0.05
print(f'O novo preço do produto, com 5% de desconto será {preço-desconto}')

#ex13
sal = int(input('Digite seu salário:'))
aumento = sal * 0.15
print(f'Seu salário, com 15% de aumento, será: {sal + aumento}')
