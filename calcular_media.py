def calcular_media(notas):
    """
    Função para calcular a média das notas.
    
    Argumento:
    notas (list): Uma lista contendo as notas.
    
    Retorna:
    float: A média das notas.
    """
    # Verifica se a lista de notas não está vazia
    if notas:
        return sum(notas) / len(notas)
    else:
        return "Erro: lista de notas vazia"

# Solicita a entrada do usuário
num_notas = int(input("Digite o número de notas: "))
notas = []

# Solicita ao usuário que insira as notas
for i in range(num_notas):
    nota = float(input("Digite a nota {}: ".format(i + 1)))
    notas.append(nota)

# Chama a função para calcular a média das notas
media = calcular_media(notas)

# Exibe o resultado
print("A média das notas é:", media)
