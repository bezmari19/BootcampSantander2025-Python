#estrutura sem repetições
a = int(input('Digite um número abaixo:\n')) #número escolhido pelo usuário
print(a) #printa o número escolhido

a += 1 
print(a) #printa o número escolhido, depois mais a conta (resposta) 5 + 1
a += 1
print(a) #printa o resultado da anterior + 1
#E assim por diante 

#Exemplo a escolhido pelo usuário e b com número pré definido
a = int(input('Digite o primeiro:\n'))
b = 2 #vai adicionando +2 ao número escolhido
print(f'Esse foi o número escolhido: {a}') #mostra o número escolhido ao usuário

a += b #5+2=7
print(a) #printa a soma
a += b #pega o resultado da primeira soma e adiciona +2
print(a) #7+2=9

#Agora com 2 números pré estabelecidos
a = 5
b = 3

a += b #5+3=8
print(a) #8
a += b #8+3=11
print(a) #11
a += b #11+3=14
print(a) #14 
