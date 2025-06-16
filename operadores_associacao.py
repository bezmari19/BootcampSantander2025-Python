#Operadores de associação 
#Serven para verificar se um objeto está dentro de alguma lista (por exemplo)

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso
#### True

"Maçã" not in frutas
#### True

200 in saques 
#### False

#exemplo mais extenso de operador de associação
frutas = ["laranja", "abacaxi", "laranja", "maçã"]
print("laranja" in frutas) #True
print("uva" not in frutas) #True
print("abacaxi" not in frutas) #False
print("abacaxi" in frutas) #True