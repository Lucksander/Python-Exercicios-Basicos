# Solicita ao usuário a primeira nota e converte para inteiro
nota1 = int(input("Digite a primeira nota: "))

# Solicita ao usuário a segunda nota
nota2 = int(input("Digite a Segunda nota: "))

# Solicita ao usuário a terceira nota
nota3 = int(input("Digite a Terceira nota: "))

# Soma as 3 notas, divide por 3 para calcular a média
# e verifica se a média é maior ou igual a 7
if (nota1 + nota2 + nota3) / 3 >= 7:
    
    # Se a média for 7 ou mais, o aluno está aprovado
    print("Aprovado")

else:
    
    # Caso contrário, o aluno está reprovado
    print("Reprovado")