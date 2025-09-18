# Importar biblioteca
import operator

# Dicionário que associa a escolha do usuário a uma função matemática
# Usamos o módulo operator para evitar vários if/elif
operacoes = {
    '1': ('somar', operator.add),
    '2': ('subtrair', operator.sub),
    '3': ('multiplicar', operator.mul),
    '4': ('dividir', operator.truediv)
}

# Solicita um número ao usuário até que ele digite algo válido (float).
# Se a entrada for inválida, avisa e repete.
def solicitar_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")

# Loop principal da calculadora: só termina quando o usuário digitar 'N'
while True:
    num1 = solicitar_numero('Por favor, digite um número: ')
    num2 = solicitar_numero('Por favor, digite outro número: ')

# Loop da escolha de operação: só sai quando o usuário digita uma opção válida
    while True:
        print('\nEscolha a operação desejada:')
        for chave, (nome, _) in operacoes.items():
           print(f'{chave} - {nome}')

        conta = input('Digite a operação desejada (1/2/3/4): ').strip()
        if conta in operacoes:
            nome, funcao = operacoes[conta]
            try:
                resultado = funcao(num1, num2)
                print(f'O resultado de {nome} entre {num1} e {num2} é {resultado}')
            except ZeroDivisionError:
                print("Não é possível dividir por zero.")
            break   # sai do loop de operação após uma escolha válida
        else:
            print("Operação inválida. Tente novamente.")

# Pergunta se o usuário deseja continuar.
# Só aceita 'S' ou 'N'. Rejeita qualquer outra entrada.
    while True:
        resposta = input('\nDeseja realizar outra operação? (S/N): ').strip().upper()
        if resposta in ('S', 'N'):
            break
        print("Entrada inválida. Digite apenas S para continuar ou N para sair.")

    if resposta == 'N':
        print('Obrigado por usar a calculadora!')
        break
