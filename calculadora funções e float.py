# Função para pedir um número ao usuário
def pedir_numero(mensagem):
    while True:
        try:
            # Tenta converter o valor digitado para float
            numero = float(input(mensagem))
            return numero
        except ValueError:
            # Executa caso o usuário digite algo inválido
            print("Digite apenas números.")


# Solicita os números ao usuário
num1 = pedir_numero("Digite o primeiro número: ")
num2 = pedir_numero("Digite o segundo número: ")

# Operações matemáticas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Exibe os resultados
print("\n===== RESULTADOS =====")
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)

# Verifica se o segundo número é diferente de zero
if num2 != 0:
    divisao = num1 / num2
    print("Divisão:", divisao)
else:
    print("Não é possível dividir por zero.")