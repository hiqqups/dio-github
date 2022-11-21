# perguntas de variavel com format
nome = input('Boa tarde meu confederado, qual teu nome?')
idade = input(f'{nome}, quantos anos tu tem meu parça?')
print(f'Então, seu nome é {nome}, e você tem {idade} anos, certin?')

#negocio idiota que eu fiz pra anny testando if e else
anny = input('QUAL SUA OPNIAO SOBRE A ANNY')
if anny == 'MALDITA':
    print('CONCORDOO')
else:
    print('wtf')

#tentando fazer calculadora sem ver o código (consegui sou foda)
print('CALCULADORA SUPER FODA!!!')
n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número'))
s = n1 + n2
print(f'O número {n1} somado ao número {n2} é igual a {s}')
print(type(s))

#calculadora com operador diferente usando varíavel (sem variavél na aula 7)
n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número:'))
op = (input('Qual operador você quer usar?'))
if op == '+':
    s = n1 + n2
    print(f'O número {n1} somado ao {n2} é igual a: {s}')
    print(type(s))
elif op == '-':
    m = n1 - n2
    print(f'O número {n1} subtraido ao {n2} é igual a: {m}')
    print(type(m))
elif op == '*':
    v = n1 * n2
    print(f'O número {n1} multiplicado por {n2} é igual a: {v}')
    print(type(v))
elif op == '/':
    d = n1 / n2
    print(f'O número {n1} dividido por {n2} é igual a: {d}')
    print(type(d))
else:
    print('Burro!!! Use os operadores: +, -, *, e /.')

