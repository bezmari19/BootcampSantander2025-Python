saldo = 1500
saque = 300
limite_diario = 250
conta_especial = True #True se a conta é especial, false se não for especial

saldo >= saque and saque <= limite_diario or conta_especial and saldo >= saque
#Verifica se o saldo é maior ou igual ao saque e se o saque é menor ou igual ao limite diário, ou se a conta é especial e o saldo é maior ou igual ao saque.
#leitura dificil do código, pois não está claro onde começa e termina cada condição.

(saldo >= saque and saque <= limite_diario) or (conta_especial and saldo >= saque)
#Verifica se o saldo é maior ou igual ao saque e se o saque é menor ou igual ao limite diário, ou se a conta é especial e o saldo é maior ou igual ao saque. 
#Os parênteses são usados para agrupar as condições e garantir a precedência correta das operações lógicas.

#exemplos de operadores lógicos de forma simplificada
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False

#Linhas lógicas muito grandes podem não ser uma boa prática em programação, pois dificulta a leitura e entendimento do código.
#É recomendável quebrar as linhas lógicas em partes menores e usar parênteses para agrupar as condições, tornando o código mais legível.
