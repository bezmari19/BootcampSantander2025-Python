#forma antiga de se interpolar string em python
#váriaveis que vão aparecer na interpolação
nome = 'Marina'
idade = 27
ocupacao = 'estudante'
linguagem = 'Python'

#esse tipo de formato serve para colocar e substiuir no texto
#após isso deve-se colocar a porcentagem e colocar o nome das variáveis em ordem para serem preenchidas na saída corretamente
print('Olá, me chamo %s. Eu tenho %d anos de idade, sou %s atualmente e estou matriculada no curdo de %s.' % (nome, idade, ocupacao, linguagem))
#%d usado para números inteiros e %s valores do tipo string
#%f usado para valores do tipo flutuante

#método format = formatar
#variáveis que serão usadas 
nome = 'Marina Bezerra'
idade = 27
ocupacao = 'estudante'
linguagem = 'Python'

#aqui o método .format() tem o mesmo princípio do método usando % porém, com uso de chaves e no fim:
#deve ser usado o format com os nomes da variáveis em forma de argumento e ainda da mesma forma que em %, todo em ordem a qual devem aparecer pro usuário
print('Olá, me chamo {}. Tenho {} anos de idade, sou {} no momento, e estou inscrita no curso de {}'.format(nome, idade, ocupacao, linguagem))
#ele também pode ser usado da seguinte forma:
print('Olá, me chamo {0}. Tenho {1} anos de idade, sou {2} no momento, e estou inscrita no curso de {3}'.format(linguagem, ocupacao, idade, nome))
#preenchendo com a posição da váriavel (exemplo embaralhado, ou seja, caso não esteja na ordem o format deve seguir da mesma maneira)
#colocar enumerado ajuda a distinguir quando uma variável aparece mais de uma vez

#usando o format de forma NOMEADAS
print('Olá, me chamo {nome}. Tenho {idade} anos de idade, sou {ocupacao} no momento e estou matriculada em um curso de {linguagem}.'.format(nome=nome, idade=idade, ocupacao=ocupacao, linguagem=linguagem)) #aqui as variaveis são passadas no formart

pessoa = {'nome': nome, 'idade': idade, 'ocupacao': ocupacao, 'linguagem': linguagem} #dicionário para facilitar o argumento usado no format ao imprimir o texto ao usuário
print('Olá, me chamo {nome}. Tenho {idade} anos de idade, sou {ocupacao} no momento e estou estudando linguagem de programação {linguagem}.'.format(**pessoa))
#nomeando as váriaveis conforme onde deve m ser preenchidas as informações contidas no texto, e no format usando o dicionário como argumento para localizar cada informação necessária
#o dicionário denomina cada váriavel ao idem correspondente

#usando f string na interpolação
#o código fica mais facil de entender e mais limpo e mais direto
nome = 'Marina Ferraz'
idade = 27
ocupacao = 'estudante'
linguagem = 'Python'

print(f'Olá, me chamo {nome}. Tenho {idade} anos de idade, atualmente sou {ocupacao} e estou inscrita no curso de linguagem de programação {linguagem}.')
#aqui é preciso colocar o f antes de declarar a string, e durante o texto apenas com chaves preencher as variaveis onde elas devem aparecer
#outro modo de formatação com números

PI = 3.14159 #valor de pi com 5 casas decimais (valor em float())
print(f'Valor de PI: {PI:.2f}') #retorna ao usuário o valor com apenas 2 casas decimais




