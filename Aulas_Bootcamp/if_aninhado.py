#Código unica e exclusivamente para fins de estudo:

CONTA_ESTÁGIO = 1 #Constante que determina o número correspondente - que o usuário visualizará na máquina - da conta que ele deseja escolher
CONTA_UNIVERSITÁRIA = 2 #Constante que determina o número correspondente - que o usuário visualizará na máquina - da conta que ele deseja escolher
SALDO_CONTA1 = 2500 #Saldo contido na conta estágio
SALDO_CONTA2 = 1500 #Saldo contido na conta universitária
LIMITE_SAQUE1 = 1500 #Limite de saque da conta estágio
LIMITE_SAQUE2 = 500 #Limite de saque da conta universitária
TETO_SALDO_CONTAS = 10000 #teto estipulado das contas, mas também para fins de exemplificação de onde o else (condição falsa comparativamente as estipuladas pelo programa)

nome_cliente = input('Digite seu nome inteiro abaixo:\n')
cpf_conta_titular = input('Digite o número do seu CPF para verificar a conta:\n(Não é obrigatório uso de caracteres especiais.)\n')
saque_conta = int(input('Digite o quanto você quer sacar:\n(Digite APENAS os números.)\n'))
tipo_conta = int(input(f'Digite {CONTA_ESTÁGIO} se sua conta for de estágio e digite {CONTA_UNIVERSITÁRIA} se sua conta for universitária:\n(Digite APENAS o número)\n'))

if tipo_conta == CONTA_ESTÁGIO: #se o tipo de conta escolhida for '1'
  if saque_conta < LIMITE_SAQUE1: #se o saque for menor que o limite estipulado na constante LIMITE_SAQUE1
    print('Seu valor foi aceito. Aguarde, a máquina está contando as notas.')
  elif saque_conta == LIMITE_SAQUE1: #se o saque for igual ao valor estipulado no LIMITE_SANGUE1
    print(f'O valor foi aceito. O saque requerido é igual ao limite {LIMITE_SAQUE1}. Aguarde, a máquina está contando as notas.')
  elif saque_conta < SALDO_CONTA1 and saque_conta > LIMITE_SAQUE1: #se o saque for menor que o saldo contido na conta, porém maior que o limite estipulado
    print(f'Seu valor foi aceito e corresponde ao limite de saque {LIMITE_SAQUE1}. Aguarde, a máquina está contando as notas')
    print('Você só pode fazer essa operação 1 vez.') 
  elif saque_conta == SALDO_CONTA1: #se o saque for igual ao saldo da conta estágio, ou seja, saque do valor cheio. 
    print(f'Você está sacando todo o valor contido na conta, tem certeza se deseja continuar com a operação? O valor é: {SALDO_CONTA1}')
    #Após esse aviso, é possível implementar algo que faça com que o usuário responda se sim ou não ( uma função, por exemplo )
    #Se a resposta for sim, segue a operação
    #se a resposta for não, ele é jogado de volta ao menu do banco ou menu de saque da máquina. Retomando ao início da operação
  elif saque_conta > SALDO_CONTA1 and saque_conta < TETO_SALDO_CONTAS: #se o valor do saque for maior que o saldo contido na conta do usuário e menor que o teto estipulado
    print(f'Você não pode realizar está operação. O valor do saldo é: {SALDO_CONTA1}') #O programa avisa caso o valor ultrapasse
    print('Clique no botão sai a baixo, para retornar ao início da operação...') #E da mesma forma que condição anterior de a opção de sim ou não aqui ele:
    #Apenas pede que o usuário retorne ao início já que o valor do saque ultrapassa o valor do saldo contido na conta
if tipo_conta == CONTA_UNIVERSITÁRIA: #Mesmos paremêtros, mas para uma conta diferente com valor estipulados diferentes.
  #apenas muda o quanto de dinheiro está conta recebe e pode retirar
  if saque_conta < LIMITE_SAQUE2:
    print('Seu valor foi aceito. Aguarde, a máquina está contando as notas.')
  elif saque_conta == LIMITE_SAQUE2:
    print(f'O valor foi aceito. O saque requerido é igual ao limite {LIMITE_SAQUE2}. Aguarde, a máquina está contando as notas.')
  elif saque_conta < SALDO_CONTA2 and saque_conta > LIMITE_SAQUE2:
    print(f'Seu valor foi aceito e corresponde ao limite de saque {LIMITE_SAQUE2}. Aguarde, a máquina está contando as notas.\n')
    print('Você só pode fazer essa operação 1 vez.')
  elif saque_conta == SALDO_CONTA2:
    print(f'Você está sacando todo o valor contido na conta, tem certeza se deseja continuar com a operação? O valor é: {SALDO_CONTA2}')
  elif saque_conta > SALDO_CONTA2 and saque_conta < TETO_SALDO_CONTAS:
    print(f'Você pode realizar está operação. O valor do saldo é: {SALDO_CONTA2}')
else:
  print('Ops, algo deu errado e você não pode fazer essa operação! Tente novamente voltando ao menu.') #Else dos dois ifs aninhados, ou seja:
  #Se nenhuma das operações acima forem verdadeiras, o usuário cairá nessa mensagem.
  #Por exemplo, valores maiores que o teto estipulado da conta