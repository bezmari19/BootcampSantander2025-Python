#parâmetros especiais:
#por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome
#Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados
#assim, um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por:
#posição, por posição e nome, ou por nome

#exemplo positional only:
def criar_carros(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carros("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #válido
criar_carros(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #inválido

#exemplo de keyword only:
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #valido
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #invalido

#exemplo keyword and positional only:
def criando_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criando_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #valido
criando_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0") #invalido

#objetos de primeira classe são as funções, podendo atribui-las a variaveis, passa-las como parametro para funções, usa-las como valores em estruturas de dados e como valor de retorno para uma função
def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(resultado)

exibir_resultado(10,10,somar)

#escopo local e escopo global:
#Em escopos globais as alterações ali feitas em objetos imutaveis serão perdidas quando o terminar de ser executado
#em escopos globais utilizamos a palavra-chave global, que informa ao interpretador que a variável que está sendo manipulada no escopo local é globa.
#Essa NÃO é uma boa pratica e deve ser evitada

#exemplo




