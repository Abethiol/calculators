while True:
    # Solicitar os dois números
    try:
        num1 = float(input('Por favor, digite um número: '))
        num2 = float(input('Por favor, digite outro número: '))
    except ValueError:
        print("Entrada inválida. Por favor, digite números.")
        continue

    # Solicitar a operação a ser feita
    print('Escolha a operação desejada:')
    print('1- somar')
    print('2- subtrair')
    print('3 - multiplicar')
    print('4 - dividir')
    conta = input('Digite a operação desejada (1/2/3/4): ')

    # Realizar operação e fornecer o resultado
    if conta == '1':
        print(f'O resultado da soma de {num1} e {num2} é {num1+num2}')
    elif conta == '2':
        print(f'O resultado da subtração de {num1} e {num2} é {num1-num2}')
    elif conta == '3':
        print (f'O resultado da multiplicação de {num1} e {num2} é {num1*num2}')
    elif conta == '4':
        if num2 == 0:
            print('Não é possível dividir por zero')
        else:
            print(f'O resultado da divisão de {num1} e {num2} é {num1/num2}')

    # Perguntar se deseja continuar
    print('Deseja realizar outra operação: ')
    continuar = input('Digite S para continuar ou N para sair: ')

    if continuar.upper() == 'N':
        print('Obrigado por usar a calculadora!')
        break
