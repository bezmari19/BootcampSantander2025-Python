#um conjunto não ordenado de pares chave: valor, onde as chaves são únicas em uma dada instância do dicionário.
#Dicionários são delimitados por chaves {} e contém uma lista de pares chave: valor separado por virgula

pessoa = {"nome":"Marina", "idade":27}
pessoa = dict(nome="Marina", idade=27)
pessoa["telefone"] = "3333--1234"
print(pessoa)

#acesso aos dados do dicionário. Exemplos:
dados = {"nome":"Marina", "idade":27, "telefone":"3333--1234"}
dados["nome"] #Marina
dados["idade"] #27
dados["telefone"] #3333-1234

#adicionando dados ao dicionário substituindo informações
dados["idade"] = 25
dados["telefone"] = "8899-1011"
print(dados)

#dicionarios aninhados: podem armazenar qualquer tipo de objeto Python como valor,
#desde que a chave para esse valor seja um objeto imutável como (straings e números)
contatos = {"marina@gmail.com":{"nome":"Marina", "idade":27, "telefone":"3333--1234"},
            "julia@gmail.com":{"nome":"Julia", "idade":25, "telefone":"8899-1011"},
            "giovana@gmail.com":{"nome":"Giovana", "idade":23, "telefone":"1011-1213"},
            }
print(contatos["giovana@gmail.com"]["telefone"])

#iterar dicionarios
for chave in contatos:
    print(chave, contatos[chave])
#for chave, valor in contatos.items():
    #print(chave, valor)
#dicionarios não permitem que você repita chave


#metodos da classe dict:
#{}.clear = apaga todos os itens do dicionario
#{}.copy = ele tira uma cópia do dicionário, virando OUTRO dicionário
#o uso serve para quando não quer alterar o dicionario original
#{}.fromkeys = 1 - quando quer criar chaves no dicionario sem colocar valor. 2 quando quer criar chaves e colocar valores padrão pode ou não ser existente
#{}.get = uma segunda forma de acessar informações no dicionario caos não tenha certeza de há realmente aquela informação pela chave
#{}.items
#{}.keys = retorna só as chaves no dicionário
#{}.pop = remover chaves e retorna o valor que ele encontrou para remoção
#{}.popitem
#{}.setdefault = se o atributo não estiver ele adiciona o valor que foi colocado ou se existir ele retorna o valor existente e não altera ele
#{}.update = ele deixa atualizar o dicionário com outro dicionário
#{}.values = ele retorna apenas o valores que tem nas chaves do dicionário
# in = funciona também dentrod e uma lista/ verifica se há informações nas chaves do dicionario
# del = tira um valor do dicionário que você passar para ele, exemplo passar o valor que deve ser retirado








