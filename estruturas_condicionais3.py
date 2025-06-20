#exemplo usando condicional if/else

IDADE_DIRIGIR = 18 #constante que verifica a idade permitida por lei nacionalmente 

idade_usuário = int(input('Coloque sua idade abaixo para verificação:\n')) #variável de entrada para a idade do usuário

if idade_usuário >= IDADE_DIRIGIR: #condicional que verifica se o usuário é maior de idade
    #retorna ao usuário que ele pode já que a condicional é verdadeira
    print('Parabéns, você está apto a tirar sua CNH! Faça agora sua inscrição.')

else: #qualquer entrada que não seja verdadeira seguindo a condição if
    print(f'Você ainda não pode dirigir, a idade válida consentida por lei é {IDADE_DIRIGIR} ou maior de 18 anos')