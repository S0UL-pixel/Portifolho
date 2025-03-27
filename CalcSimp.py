def resultado(operacao, n1, n2):
    match operacao:
        case '+':
            return n1 + n2
        case '-':
            return n1 - n2
        case '*':
            return n1 * n2
        case '/':
            return n1 / n2
        case '**':
            return n1 ** n2


operacao = str(input('Qual operação desejará vazer?(+, -, *, /, **)'))
n1 = int(input('Qual o primeiro numero?'))
n2 = int(input('Qual o segundo numero?'))
print(f'O resultado da operação desejada é de {resultado(operacao, n1, n2)}')