#exemplo de condicionais simples apenas com um 'desvio'
MAIOR_IDADE = 18

idade = int(input('Digite abaixo a sua idade:\n')) #Variável de entrada do usuário

if idade >= MAIOR_IDADE: #condicional que verifica se o usuário tem 18 ou é maior de 18 anos
    #retorna que ele pode fazer consumo de bebida alccoolica devido a idade digitada
    print(f'Você pode beber, está dentro da idade consentida para isso: maior ou igual {MAIOR_IDADE}')

if idade < MAIOR_IDADE: #condicional que verifica se o usuario é menor de 18 anos
    #retorna o aviso com a idade permitida por lei 
    print(f'Ops, você não pode beber. A idade consentida para isso é {MAIOR_IDADE} ou maior que {MAIOR_IDADE}')