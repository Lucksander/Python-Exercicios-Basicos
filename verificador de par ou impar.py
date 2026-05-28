# Solicita ao usuário que digite um número inteiro
numero = int(input("digite um numero inteiro: "))

# Verifica se o número é par ou ímpar usando o operador módulo (%)
# Se o resto da divisão por 2 for igual a 0, o número é par
if numero % 2 == 0:
    print("o numero é par")
else:
    print("o numero é impar")