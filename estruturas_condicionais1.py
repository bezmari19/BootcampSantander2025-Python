#Exemplo de verificação usando if/elif/else de forma básica

#Primeiro exemplo: verificar a idade ao comprar bebida alcoolica no super mercado

IDADE_PERMITIDA = 18 #constante que verifica idade consentida nacionalmente para uso de bebida
LIMITE_IDADE = 100 #constante que verifica o limite de idade para consumo de bebida;
#(pseudo limite, serve apenas para verificar os caracteres no else caso seja um número inteiro)
BEBIDA_NACOMPRA = 'SIM' #constante que verifica a resposta do usuário para se houver bebida na compra
BEBIDA_FORACOMPRA = 'NÃO' #constante que verifica a resposta do usuário se não houver bebida na compra

nome_cliente = input('Digite seu nome abaixo, por favor:\n') #váriavel de entrada do nome do usuário
idade_cliente = int(input('Digite sua idade abaixo, por favor:\n')) #váriavel de entrada da idade do usuário
tem_bebida = input('Digite SIM para bebidade na compra e NÃO para não tem na compra:\n') #variável de entrada que verifica conforme as opções se:
#há bebida na compra 'SIM' e 'NÃO' caso não tenha

if idade_cliente < IDADE_PERMITIDA and tem_bebida == BEBIDA_NACOMPRA: #condição que verifica se o usuário é menor de idade e se tem bebida na compra dele
  print(f'Você não pode comprar essa mercadoria. A idade permitida para uso de bebidas alcoolicas é {IDADE_PERMITIDA}') #ele retorna ao usuário que não pode já que ele é menor de idade e há bebida na mercadoria

elif idade_cliente >= IDADE_PERMITIDA and idade_cliente <= LIMITE_IDADE and tem_bebida == BEBIDA_NACOMPRA: #condição segundaria que verifica caso a idade digitada seja igual ou maior a idade consentida, se está dentro do limite de caracteres e se há bebida
  #retorna ao usuário que ele pode já que cumpre os requisitos e que pode prosseguir com a compra
  print('Você está dentro do consentimento para fazer uso da bebida acoolica.\n') 
  print('Por favor, escolha sua forma de pagamento a seguir.\n')

elif idade_cliente < IDADE_PERMITIDA and tem_bebida == BEBIDA_FORACOMPRA: #condição, caso as duas primeiras não sejam validas, verifica se NÃO há bebida na compra e se o usuário é menor de idade
  #retorna ao cliente que pode prosseguir com a compra 
  print('Ok, agora escolha sua forma de pagamento!')

elif idade_cliente >= IDADE_PERMITIDA and idade_cliente <= LIMITE_IDADE and tem_bebida == BEBIDA_FORACOMPRA: #condição que verifica se não há bebida alcoolica na compra do maior de idade e se está dentro do limite de caracteres
  #retorna ao cliente que pode prosseguir com a compra
  print('Ok, agora escolha sua forma de pagamento!')

else: #caso nenhuma das condições anteriores estejam dentro das condições estabelicidas para compra
  print('Ops, acho que deu algo de errado com a sua compra. Tente novamente voltando ao menu!') 
