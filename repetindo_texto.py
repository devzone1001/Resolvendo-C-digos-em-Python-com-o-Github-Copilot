def repetir_string_com_espacos(string, vezes):
    """
    Função para repetir uma string com espaços entre as letras um número especificado de vezes.
    
    Argumentos:
    string (str): A string a ser repetida.
    vezes (int): O número de vezes que a string deve ser repetida.
    
    Retorna:
    str: A string repetida com espaços entre as letras.
    """
    # Adiciona espaços entre cada caractere da string repetida
    string_com_espacos = ' '.join(string)
    # Repete a string com espaços o número de vezes especificado
    return (string_com_espacos + ' ') * vezes

# Solicita a entrada do usuário
entrada_string = input("Digite uma string: ")
entrada_numero = int(input("Digite um número: "))

# Chama a função para repetir a string com espaços
resultado = repetir_string_com_espacos(entrada_string, entrada_numero)

# Exibe o resultado
print("O resultado da repetição com espaços é:", resultado)
