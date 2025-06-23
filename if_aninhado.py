CONTA_ESTÁGIO = 1
CONTA_UNIVERSITÁRIA = 2
SALDO_CONTA1 = 2.500
SALDO_CONTA2 = 2.000
LIMITE_SAQUE1 = 1.500
LIMITE_SAQUE2 = 1.000

nome_cliente = input('Digite seu nome abaixo:\n')
cpf_conta_titular = input('Digite o número do seu CPF para verificar a conta:\n')
saque_conta = int(input('Digite o quanto você quer sacar:\n'))
tipo_conta = int(input(f'Digite {CONTA_ESTÁGIO} se sua conta for de estágio e digite {CONTA_UNIVERSITÁRIA} se sua conta for universitária:\n'))

if tipo_conta == '1':
  if saque_conta < LIMITE_SAQUE1 and saque_conta < SALDO_CONTA1:
    print('O valor do saque requerido foi aceito, espere a máquina contar as notas!')
  elif saque_conta >= LIMITE_SAQUE1 and saque_conta < SALDO_CONTA1:
    print('Você tem certeza? O limite de saque irá esceder e não poderá mais sacar por hoje. Verifique o valor disponível na conta antes de realizar a operação')
  elif saque_conta == SALDO_CONTA1:
    print('Você irá retirar todo dinheiro da conta, tem certeza que quer fazer essa operação?')

elif tipo_conta == '2':
  if saque_conta < LIMITE_SAQUE2 and saque_conta < SALDO_CONTA2:
    print('O valor do saque requerido foi aceito, espere a máquina contar as notas!')
  elif saque_conta >= LIMITE_SAQUE2 and saque_conta < SALDO_CONTA2:
     print('Você tem certeza? O limite de saque irá esceder e não poderá mais sacar por hoje. Verifique o valor disponível na conta antes de realizar a operação')
  elif saque_conta == SALDO_CONTA2:
    print('Você irá retirar todo dinheiro da conta, tem certeza que quer fazer essa operação?')

else:
  print('Algo deu errado, tente novamente.')