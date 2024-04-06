def verificar_palindromo(texto):
    """
    Função para verificar se uma palavra ou frase é um palíndromo.
    
    Argumento:
    texto (str): O texto a ser verificado.
    
    Retorna:
    bool: True se o texto for um palíndromo, False caso contrário.
    """
    # Remove espaços em branco e converte para minúsculas
    texto = texto.replace(" ", "").lower()
    # Compara o texto com seu inverso
    return texto == texto[::-1]

# Solicita a entrada do usuário
entrada_texto = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

# Chama a função para verificar se o texto é um palíndromo
resultado = verificar_palindromo(entrada_texto)

# Exibe o resultado
if resultado:
    print("O texto é um palíndromo!")
else:
    print("O texto não é um palíndromo.")
