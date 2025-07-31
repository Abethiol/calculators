#!/bin/bash
while true; do
    echo "Calculadora em Shell"

    # Pede o primeiro número
    echo "Por favor, digite o primeiro número:"
    read num1

    # Pede o segundo número
    echo "Por favor, digite o segundo número:"
    read num2

    # Pede a operação
    echo "Escolha a operação desejada:"
    echo "1 - Somar"
    echo "2 - Subtrair"
    echo "3 - Multiplicar"
    echo "4 - Dividir"
    echo "Digite o número da operação (1/2/3/4):"
    read conta

    # Faz a conta dependendo da escolha
    if [ "$conta" == "1" ]; then
        # Soma
        resultado=$(echo "scale=2; $num1 + $num2" | bc -l)
        echo "O resultado da soma de $num1 e $num2 é: $resultado"
    elif [ "$conta" == "2" ]; then
        # Subtração
        resultado=$(echo "scale=2; $num1 - $num2" | bc -l)
        echo "O resultado da subtração de $num1 e $num2 é: $resultado"
    elif [ "$conta" == "3" ]; then
        # Multiplicação
        resultado=$(echo "scale=2; $num1 * $num2" | bc -l)
        echo "O resultado da multiplicação de $num1 e $num2 é: $resultado"
    elif [ "$conta" == "4" ]; then
        # Divisão - verifica se o segundo número é zero antes
        if [ "$num2" == "0" ]; then
            echo "Não dá para dividir por zero!"
        else
            resultado=$(echo "scale=2; $num1 / $num2" | bc -l)
            echo "O resultado da divisão de $num1 e $num2 é: $resultado"
        fi
    else
        echo "Opção inválida. Por favor, escolha 1, 2, 3 ou 4."
    fi

    # Pergunta se quer fazer outra conta
    echo "Quer fazer outra operação?"
    echo "Digite S para SIM ou N para NÃO:"
    read continuar

    # Sai do programa se a pessoa digitar 'N'
    if [ "${continuar,,}" == "n" ]; then # O ',,' aqui transforma para minúscula antes de comparar
        echo "Obrigado por usar a calculadora!"
        break
    fi
done
