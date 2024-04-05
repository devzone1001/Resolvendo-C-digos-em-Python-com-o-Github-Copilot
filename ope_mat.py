def soma(a, b):
    """
    Função para calcular a soma de dois números.
    """
    return a + b

def subtracao(a, b):
    """
    Função para calcular a subtração de dois números.
    """
    return a - b

def multiplicacao(a, b):
    """
    Função para calcular a multiplicação de dois números.
    """
    return a * b

def divisao(a, b):
    """
    Função para calcular a divisão de dois números.
    """
    # Verifica se b é diferente de zero para evitar divisão por zero
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

# Solicita a entrada do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Realiza operações entre os números
resultado_soma = soma(numero1, numero2)
resultado_subtracao = subtracao(numero1, numero2)
resultado_multiplicacao = multiplicacao(numero1, numero2)
resultado_divisao = divisao(numero1, numero2)

# Exibe os resultados
print("Soma:", resultado_soma)
print("Subtração:", resultado_subtracao)
print("Multiplicação:", resultado_multiplicacao)
print("Divisão:", resultado_divisao)
