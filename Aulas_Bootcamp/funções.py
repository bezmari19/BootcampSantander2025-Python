#função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros
#esses parâmetros, podem ou não ter valores padrões. Usar funções torna o código mais legível
#possibilita o reaproveitamento de código.
#Programar baseado em funções, é o mesmo que dizer que estamos programando de maneira estrturada

#exemplo:
#def identifica o nome da função, a função tem seus parâmetros
def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem2(nome):
    print(f"Seja bem-vindo(a) {nome}!")

def exibir_mensagem3(nome="Anônimo"):
    print(f"Seja bem-vindo(a) {nome}!")

#forma como executa a função chamando-a
exibir_mensagem()
exibir_mensagem2(nome="Marina")
exibir_mensagem3()
exibir_mensagem3(nome="Chappie")

#para retornar um valor, utilizamos a palavra return. Toda função Python retorna None por padrão.
#diferente de outras linguagens de programação, em python uma função pode retornar mais de um valor

#exemplo:
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(calcular_total([10,20,34]))
print(retorna_antecessor_e_sucessor(10))

#argumentos nomeados: funções também podem ser chamadas usando argumentos nomeados da forma chave=valor
#exemplo:
def salvar_carros(marca,modelo,ano,placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carros("Fiat", "Palio", 1999, "BC-1234")
#salvar_carros(**("marca":"Fiat", "modelo":"Palio", "ano":1999, "placa":"ABC-1234"))

#conceito de Args e Kwargs:
#Pode combinar parâmetros obrigatórios com args e kwargs, quando são definidos (*args e **kwargs),
#recebe os valores como tupla e dicionário respectivamente
#exemplo:
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Quinta-feira, 06 de Agosto de 2025", "Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)







