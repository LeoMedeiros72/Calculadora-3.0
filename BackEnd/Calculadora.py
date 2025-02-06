import math

# Funções matemáticas
def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

def potenciacao(x, y):
    return x ** y

def fatorial(x):
    return math.factorial(int(x))

def pitagoras(cat1, cat2, hip):
    """Calcula o valor desconhecido (cateto ou hipotenusa) usando o Teorema de Pitágoras."""
    if hip == 'x':
        return (cat1 ** 2 + cat2 ** 2) ** 0.5
    elif cat1 == 'x':
        return (hip ** 2 - cat2 ** 2) ** 0.5
    elif cat2 == 'x':
        return (hip ** 2 - cat1 ** 2) ** 0.5

def equacao_primeiro_grau(a, b):
    """Resolve a equação do primeiro grau ax + b = 0."""
    if a == 0:
        return "Erro: Coeficiente 'a' não pode ser zero."
    x = -b / a
    return x

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
        print("7. Teorema de Pitágoras")
        print("8. Equação do primeiro grau")
        print("9. Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5/6/7/8/9): ")

        # Sair do programa
        if escolha == '9':
            print("Saindo da calculadora...")
            break

        # Operações com dois números
        if escolha in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida! Por favor, digite números.")
                continue

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

        # Fatorial
        elif escolha == '6':
            try:
                num = int(input("Digite o número para calcular o fatorial: "))
                if num < 0:
                    print("Erro: Fatorial não é definido para números negativos.")
                    continue
                print(f"Resultado: {fatorial(num)}")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número inteiro.")

        # Teorema de Pitágoras
        elif escolha == '7':
            try:
                print("Atribua os valores da hipotenusa e catetos. Coloque 'x' para o valor desconhecido.")
                hip = input("Digite a hipotenusa: ")
                cat1 = input("Digite o cateto 1: ")
                cat2 = input("Digite o cateto 2: ")

                hip = float(hip) if hip != 'x' else 'x'
                cat1 = float(cat1) if cat1 != 'x' else 'x'
                cat2 = float(cat2) if cat2 != 'x' else 'x'

                desconhecidos = [val for val in [hip, cat1, cat2] if val == 'x']
                if len(desconhecidos) != 1:
                    print("Erro: Deve haver exatamente um valor desconhecido (x).")
                    continue

                resultado = pitagoras(cat1, cat2, hip)
                print(f"O outro valor é: {resultado}")
            except ValueError:
                print("Entrada inválida! Por favor, digite números ou 'x' para o valor desconhecido.")

        # Equação do primeiro grau
        elif escolha == '8':
            try:
                print("Atribua os valores da equação na forma Ax + B = 0")
                a = float(input("Digite o valor de A: "))
                b = float(input("Digite o valor de B: "))
                resultado = equacao_primeiro_grau(a, b)
                print(f"O valor de x é: {resultado}")
            except ValueError:
                print("Entrada inválida! Por favor, digite números.")

        else:
            print("Opção inválida! Tente novamente.")


# Executar a calculadora
if __name__ == "__main__":
    calculadora()
