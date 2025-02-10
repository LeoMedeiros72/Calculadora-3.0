import math

# Funções matemáticas
def adicionar(x, y):
    """Calcula a soma de dois números"""
    return x + y

def subtrair(x, y):
    """Calcula a subtração de dois números"""
    return x - y

def multiplicar(x, y):
    """Calcula a multiplicação de dois números"""
    return x * y

def dividir(x, y):
    """Calcula a divisão de dois números"""
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

def potenciacao(x, y):
    """Calcula a potenciação de dois números"""
    return x ** y

def fatorial(x):
    """Calcula o fatorial de um número"""
    return math.factorial(int(x))

def logaritmo(x, base=None):
    """Calcula o logaritmo de x na base especificada. Se a base não for fornecida, retorna o logaritmo natural."""
    if base is None:
        return math.log(x)  
    else:
        if base <= 0 or base == 1:
            return "Erro: A base deve ser positiva e diferente de 1."
        return math.log(x, base)  

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

def equacao_segundo_grau(a, b, c):
    """Resolve uma equação do segundo grau do tipo ax² + bx + c = 0."""
    if a == 0:
        return "Erro: Coeficiente 'a' não pode ser zero."

    delta = b ** 2 - 4 * a * c
    print(f"Discriminante (Delta): {delta}")

    if delta < 0:
        print("A função não possui raízes reais.")
        x1 = x2 = None
    elif delta == 0:
        x1 = x2 = -b / (2 * a)
        print(f"A função possui uma raiz real dupla: x1 = x2 = {x1:.2f}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"A função possui duas raízes reais diferentes: x1 = {x1:.2f} e x2 = {x2:.2f}")

    xv = -b / (2 * a)
    yv = -delta / (4 * a)
    print(f"O vértice da parábola é: ({xv:.2f}, {yv:.2f})")

    return {
        "Delta": delta,
        "raízes": (x1, x2),
        "vértice": (xv, yv),
    }

# Ajustar lógica de saída
def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potenciação")
        print("6. Fatorial")
        print("7. Logaritmo")
        print("8. Teorema de Pitágoras")
        print("9. Equação do primeiro grau")
        print("10. Equação do segundo grau")
        print("11. Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5/6/7/8/9/10/11): ")

        # Sair do programa
        if escolha == '11':
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

        # Logaritmo
        elif escolha == '7':
            try:
                x = float(input("Digite o valor de x (logaritmando): "))
                base = input("Digite o valor da base (deixe em branco para logaritmo natural): ")
                if base == '':
                    resultado = logaritmo(x)
                else:
                    base = float(base)
                    resultado = logaritmo(x, base)
                print(f"Resultado: {resultado}")
            except ValueError:
                print("Entrada inválida! Por favor, digite números.")

        # Teorema de Pitágoras
        elif escolha == '8':
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
        elif escolha == '9':
            try:
                print("Atribua os valores da equação na forma Ax + B = 0")
                a = float(input("Digite o valor de A: "))
                b = float(input("Digite o valor de B: "))
                resultado = equacao_primeiro_grau(a, b)
                print(f"O valor de x é: {resultado}")
            except ValueError:
                print("Entrada inválida! Por favor, digite números.")

        # Equação do segundo grau
        elif escolha == '10':
            try:
                print("Atribua os valores da equação na forma Ax² + Bx + C = 0")
                a = float(input("Digite o valor de A: "))
                b = float(input("Digite o valor de B: "))
                c = float(input("Digite o valor de C: "))
                resultado = equacao_segundo_grau(a, b, c)
                print(f"Os valores da função são: {resultado}")
            except ValueError:
                print("Entrada inválida! Por favor, digite números.")

        else:
            print("Opção inválida! Tente novamente.")

# Executar a calculadora
if __name__ == "__main__":
    calculadora()
