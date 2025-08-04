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



