# Importar bibliotecas necessárias
import math

# Funções matemáticas
def adicionar(x, y):
    """Retorna a soma de x e y."""
    return x + y

def subtrair(x, y):
    """Retorna a subtração de y de x."""
    return x - y

def multiplicar(x, y):
    """Retorna a multiplicação de x por y."""
    return x * y

def dividir(x, y):
    """Retorna a divisão de x por y, com tratamento para divisão por zero."""
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

def potenciacao(x, y):
    """Retorna x elevado à potência de y."""
    return x ** y

def fatorial(x):
    """Retorna x fatorial"""
    return math.factorial(int(x))

# Interface da calculadora
def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potenciação")
        print("6. Fatorial")
        print("7. Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5/6/7): ")

        # Sair do programa
        if escolha == '7':
            print("Saindo da calculadora...")
            break

        # Verificar se a escolha é válida
        if escolha in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida! Por favor, digite números.")
                continue

            # Executar a operação escolhida
            if escolha == '1':
                print(f"Resultado: {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif escolha == '4':
                print(f"Resultado: {dividir(num1, num2)}")
            elif escolha == '5':
                print(f"Resultado: {potenciacao(num1, num2)}")
        
        elif escolha == '6':
            try:
                num1 = int(input("Digite o número para calcular o fatorial: "))
                if num1 < 0:
                    print("Erro: Fatorial não é definido para números negativos.")
                    continue
            except ValueError:
                print("Entrada inválida! Por favor, digite um número inteiro.")
                continue
            print(f"Resultado: {fatorial(num1)}")
        
        else:
            print("Opção inválida! Tente novamente.")

# Executar a calculadora
if __name__ == "__main__":
    calculadora()
