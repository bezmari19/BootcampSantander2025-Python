nome = input('Digite seu nome completo:\n')
idade = input('Digite sua idade:\n')
cidade = input('Digite a cidade onde você mora:\n')

print(f'Olá {nome}, você tem {idade} anos e mora em {cidade}')

# Exemplo para input e output simples com quebra de linha

nome = input('Digite seu primeiro nome:')
saldo_disponível = 2000.00
valor_compra = float(input('Digite o valor da compra:'))

print(f'Olá {nome}, o valor da compra é de R$ {valor_compra:.2f} e seu saldo disponível é de R$ {saldo_disponível:.2f}')

# Exemplo para input e output com formatação de string e cálculo de ponto flutuante

nome = input('Digite seu nome completo:')
sobrenome = input('Digite seu sobrenome:')

print(nome, sobrenome, sep='#', end='...\n')

