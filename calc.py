# Calc em python.
#Uso o int para falar que eu quero um número inteiro se eu não usar o int o computador vai ler como se fosse uma string usamos o input para que o usuario coloque qualquer coisa de preferencia um número 
print('''[========Calculadora feita por GuiR.==========]
Essa calculadora é feita em python, Ela ainda não está pronto mais dá para usar, você pode somar, multiplicar , divir, fazer a raiz quadrada, subtração e ver o resto do calculo 
Espero que goste <3
''')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = n1 + n2 
n4 = n1 * n2
n5 = n1 / n2
n6 = n1 - n2
n7 = n1 ** n2
n8 = n1 % n2
if n1 + n2: #Usamos o if para ele fazer uma função se for verdadeira
    print('A soma entre eles são: {}'.format(n3))
if n1 * n2:
    print('{} vezes {} é igual a: {}'.format(n1,n2,n4))
if n1 / n2:
    print('O {} divido por {} e igual a: {}'.format(n1,n2,n5))
if n1 - n2:
    print('{} menos {} dá: {}'.format(n1,n2,n6))
if n1 ** n2:
    print('A raiz quadrade de {} e {} e igual a: {}'.format(n1,n2,n7))
if n1 % n2:
    print('O resto de {} e {} são: {}'.format(n1,n2,n8))
else:
    print('Esse número é invalido')
print('''O programa acaba por aqui espero que gostem 
 by GuiR''')

