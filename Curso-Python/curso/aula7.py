#calculadora super pica sem usar varíavel e com operadores diferentes
n1 = int(input('Digite um número:'))
op = (input('Qual operador você quer usar?'))
n2 = int(input('Digite mais um número:'))

if op == '+':
    print(f'O número {n1} somado ao {n2} é igual a: {n1+n2}')
    print(type(n1+n2))
elif op == '-':
    print(f'O número {n1} subtraido ao {n2} é igual a: {n1-n2}')
    print(type(n1-n2))
elif op == '*':
    print(f'O número {n1} multiplicado por {n2} é igual a: {n1*n2}')
    print(type(n1*n2))
elif op == '/':
    print(f'O número {n1} dividido por {n2} é igual a: {n1/n2:.5f}')
    print(type(n1/n2))
else:
    print('Burro!!! Use os operadores: +, -, *, e /.')
