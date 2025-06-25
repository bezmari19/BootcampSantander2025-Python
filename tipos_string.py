nome = 'Marina' #variável com o nome

print(nome.upper()) #deixa todas as letras em maiúscula
print(nome.lower()) #deixa todas as letras em minúscula
print(nome.title()) #deixa apenas a primeira letra maiúscula
print(nome.strip()) #coloca espaço na esquerda e na direita 
print(nome.lstrip()) #coloca espaço apenas na esquerda
print(nome.rstrip()) #coloca espaço apenas na direita
print(nome.center(15, '!')) #centrliza a variável: o primeira argumento é o tamnanho do espaço
#o segundo argumento não é obrigatório e coloca o caracter escolhido preenchendo os espaços
print('.'.join(nome)) #junta ao argumento o caracter passado no comando

#juntando os comandos de formas diferentes:

print(nome.center(10,'.').upper()) #centraliza a variável e coloca pontos nos lugares e deixa a variável em letra maiuscula
print(nome.title().center(10,'#')) #deixa a várivel com a primeira letra maiuscula, centraliza e preenche com hashtag nos luagres com espaço
print('.'.join(nome).center(15,'*')) #coloca na varável o . entre as letras e centraliza preenchendo com asterisco o local com espago
print('-'.join(nome).upper().rstrip()) #coloca - entre as letras da váriavel, em letra maiuscula e coloca espaço do lado direito da várivavel
