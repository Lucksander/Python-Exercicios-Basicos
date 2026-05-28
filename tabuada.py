# Solicita um número inteiro ao usuário
numero = int(input("Digite um numero Inteiro: "))

# O laço for vai repetir 10 vezes
# range(1,11) começa no 1 e vai até o 10
for i in range(1,11):

    # Mostra a soma do número digitado com o valor atual de i
    print(f"{numero} + {i} = {numero + i}", end="  ")

    # Mostra a subtração
    print(f"{numero} - {i} = {numero - i}", end="  ")

    # Mostra a multiplicação
    print(f"{numero} * {i} = {numero * i}", end="  ")

    # Mostra a divisão com 2 casas decimais
    print(f"{numero} / {i} = {numero / i:.2f}")