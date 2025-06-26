#Exemplo uso de if ternário

saldo_conta = 1500 #saldo da conta no momento da compra
pagamento_valor = int(input('Digite o valor da compra aqui\n')) #valor do pagamento referente a compra feita 

valor_retirado = saldo_conta - pagamento_valor #várivel que faz a conta do pagamento, ou seja que retira o valor

compra = 'Compra finalizada' if valor_retirado < saldo_conta else 'Algo deu errado' #if tenaário que verifica de forma simplificada se:
#A conta está ok ou não.
print(f'{compra} ao realizar o pagamento!\n') #Retorna ao usuário se deu certo ou se não com base na condição estipulada no programa
print(f'Seu saldo agora é: {valor_retirado}') #Retorna também ao usuário qual o saldo atual após a realização da compra