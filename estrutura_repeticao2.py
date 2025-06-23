#Usando FOR:

texto = input('Digite um texto em letras minúsculas qualquer abaixo:\n') #o usuário pode digitar o texto que quiser
sequencia = input('Digite qualquer sequência de número a baixo:\n') # o usuário pode digitar a sequência de números que quiser
CONSOANTES = 'bcdfghjklmnpqrstvwxyz' #constante que verifica quais consoantes estão presentes no texto
PARES = '02468' #constante que verifica quais números pares estão presentes na sequência do usuário

for letra in texto: #para cada letra no texto, se a letra estiver em consoante
    if letra in CONSOANTES:
        print(letra, end='\n') #ela mostra ao usuário as letras consoantes do texto

for numero in sequencia: #para cada numero na sequencia, se o numero estiver em par
    if numero in PARES:
        print(numero, end='\n') #ela mostra ao usuário os números pares da sequência

print() #adiciona uma quebra de linha ao output