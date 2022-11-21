#calculadora simples, só faz soma, o type mostra qual o tipo da variavel
n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número:'))
s = n1 + n2
print(f'O número {n1} somado ao {n2} é igual a: {s}')
print(type(n1))

#dissecador de variavel, mostra o que a varíavel é
n = (input('Digite algo'))
print(f'{n} é apenas númerico?', n.isnumeric())
print(f'{n} é apenas alfábético?', n.isalpha())
print(f'{n} é número e alfábético?', n.isalnum())
print(f'{n} está em MAÍSCULO?', n.isupper())
print(f'{n} está em minúsculo?', n.islower())
print(f'{n} é um espaço?', n.isspace())
print(f'{n} está capitalizada?', n.istitle())
print(f'{n} transformado em caps:', n.capitalize())
