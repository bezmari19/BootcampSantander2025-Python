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
  if saque_conta < LIMITE_SAQUE1:
    print('Seu valor foi aceito. Aguarde, a máquina está contando as notas.')
  elif saque_conta < LIMITE_SAQUE1 and saque_conta == LIMITE_SAQUE1:
    print(f'O valor foi aceito. O saque requerido é igual ao limite {LIMITE_SAQUE1}. Aguarde, a máquina está contando as notas.')
  elif saque_conta < SALDO_CONTA1 and saque_conta >= LIMITE_SAQUE1:
    print(f'Seu valor foi aceito e corresponde ao limite de saque {LIMITE_SAQUE1}. Aguarde, a máquina está contando as notas')
  elif saque_conta == SALDO_CONTA1:
    print(f'Você está sacando todo o valor contido na conta, tem certeza se deseja continuar com a operação? O valor é: {SALDO_CONTA1}')
  elif saque_conta > SALDO_CONTA1:
    print(f'Você pode realizar está operação. O valor do saldo é: {SALDO_CONTA1}')
  else: 
    print('Ops, algo deu errado e você não pode realizar está operação! Volte ao menu.')