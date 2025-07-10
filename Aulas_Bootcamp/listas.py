#tipos de lista em python
frutas = ['abacaxi', 'uva', 'maça', 'banana']
frutas1 = []
letras = list('frutas')
print(frutas)
numero = list(range(10))
print(numero)
carros = ['Ferrari', 'FB', 420000, 2020, 2900, 'São Paulo', True ]
print(carros)

#como acessar as listas:
#acesso direto - a partir de um indice iniciado em 0
frutas[0]
print(frutas[0])
frutas[2]
print(frutas[2])
frutas[-1]
print(frutas[-1])

#listas aninhadas:
#podem armazenar outras listas criando, por exemplo, a matriz bidimensional (com colunas e linhas)
matriz = [
    [1,'a',2],
    ['b',3,4],
    [6,5,'c']
]
print(matriz)
matriz[0] #[1,'a',2]
print(matriz[0])
matriz[0][0] #1
print(matriz[0][0])
matriz[0][-1] #2
print(matriz[0][-1])
matriz[-1][-1] #'c'
print(matriz[-1][-1])

#fatiamento de listas
lista = ['p','y','t','h','o','n']
lista[2:]
print(lista[2:])
lista[:2]
print(lista[:2])
lista[1:3]
print(lista[1:3])
lista[0:3:2]
print(lista[0:3:2])
lista[::]
print(lista[::])
lista[::-1]
print(lista[::-1])

#iterar listas: normalmente é usado o laço de repetição for
for carro in carros:
    print(carros)

#função enumerate: muitas vezes usada dentro do laço for para saber o indice do objeto dentro do laço de repetição
for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

#compreensão de listas: usada principalmente quando quer criar uma lista nova com base em uma lista existente
#de uma forma melhor usando um filtro ou gerar uma nova lista aplicando uma modificação
numeros_lista = [1, 30, 21, 2, 9, 65, 34]
#quadrado = [numero ** 2 for numero in numeros_lista]
#pares = [numero for numero in numeros_lista if numero % 2 == 0]
#for numero in numeros_lista:
    #if numero % 2 == 0:
        #pares.append(numero)





