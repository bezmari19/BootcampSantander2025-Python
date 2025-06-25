#código exemplificando o uso estrtura while em código python
#while executa toda vez que a tela é atendida

opcao = -1 #variável que garante o funcionamento e a condição da inicialização do loop

while opcao != 0: #enquanto a opção for diferente de 0 o código continuara rodando as opções
    opcao = int(input('Digite:\n [1] Sacar\n [2] Extrato\n [0] Sair:\n')) #váriável de entrada para o usuário indicando as opções 

    if opcao == 1: #se for igual a 1
        print('Sacando o valor, aguarde um instante!') #mostra que está sacando 
    elif opcao == 2: #se não outro, esse opção 2
        print('Exibindo extrato')
    #pode ser usado apenas até esse elif ou:
#else que não não é muito usado para quando o usuário desejar apertar 0 e sair
else:
    print('Obrigada por usar nosso sistema! Volte sempre.') #mensagem a ser exibida para o usuário

#uso de break em estrturas de repetição:

while True: #sequência infinita
    numero = int(input('Informe um número:\n')) #entrada do usuário

    if numero == 30: #se o número for igual a 30 
        break #o código para e...

print(numero) #mostra ao usuário 

#break corta o laço de repetição 
#continue pula 