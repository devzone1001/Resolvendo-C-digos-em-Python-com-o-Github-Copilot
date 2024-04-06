def verificar_par_impar(numero):
    """
    Função para verificar se um número é par ou ímpar.
    
    Argumento:
    numero (int): O número a ser verificado.
    
    Retorna:
    str: "par" se o número for par, "ímpar" se o número for ímpar.
    """
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Solicita a entrada do usuário
entrada_numero = int(input("Digite um número: "))

# Chama a função para verificar se o número é par ou ímpar
resultado = verificar_par_impar(entrada_numero)

# Exibe o resultado
print("O número", entrada_numero, "é", resultado)
