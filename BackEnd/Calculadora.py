!pip install findiff

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
import findiff


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

def raiz(x, y):
    """
    Calcula a raiz de um número x com índice y.

    Parâmetros:
    x (float): O número do qual se deseja calcular a raiz.
    y (int): O índice da raiz.

    Retorna:
    float: O valor da raiz.
    """
    if y == 0:
        return "Erro: O índice da raiz não pode ser zero."
    if x < 0 and y % 2 == 0:
        return "Erro: Não é possível calcular a raiz par de um número negativo."
    return x ** (1 / y)


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

import math

def trigonometria(x, em_graus=True):
    """
    Calcula o seno, cosseno e tangente de um ângulo.

    Parâmetros:
    x (float): O valor do ângulo.
    em_graus (bool): Se True, o ângulo é considerado em graus. Se False, em radianos.

    Retorna:
    dict: Um dicionário contendo o seno, cosseno e tangente do ângulo.
    """
    if em_graus:
        x = math.radians(x)  # Converte graus para radianos

    seno = math.sin(x)
    cosseno = math.cos(x)
    tangente = math.tan(x)

    print(f"O seno de {x:.2f} radianos é {seno:.2f}, o cosseno é {cosseno:.2f} e a tangente é {tangente:.2f}")


def plotar_funcao_primeiro_grau(a, b):
    """
    Plota o gráfico da função do primeiro grau ax + b e mostra os pontos de corte com os eixos.

    Parâmetros:
    a (float): Coeficiente angular.
    b (float): Coeficiente linear.
    """
    # Define o intervalo de valores para x
    x = np.linspace(-10, 10, 400)  # Gera 400 pontos entre -10 e 10
    y = a * x + b  # Calcula os valores de y

    # Calcula os pontos de corte com os eixos
    corte_x = (-b / a, 0) if a != 0 else None  # Corte com o eixo x
    corte_y = (0, b)  # Corte com o eixo y

    # Configura o gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"y = {a}x + {b}", color="blue")

    # Destaca os pontos de corte
    if corte_x:
        plt.scatter(*corte_x, color="red", label=f"Corte com eixo x: ({corte_x[0]:.2f}, 0)")
    plt.scatter(*corte_y, color="green", label=f"Corte com eixo y: (0, {corte_y[1]:.2f})")

    # Linhas de referência (eixos x e y)
    plt.axhline(0, color="black", linewidth=0.5)  # Linha horizontal no y=0
    plt.axvline(0, color="black", linewidth=0.5)  # Linha vertical no x=0

    # Título e legendas
    plt.title(f"Gráfico da Função do Primeiro Grau: y = {a}x + {b}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Exibe as coordenadas no terminal
    print("\nCoordenadas de Corte:")
    if corte_x:
        print(f"Corte com o eixo x: ({corte_x[0]:.2f}, 0)")
    else:
        print("A função não corta o eixo x (reta horizontal).")
    print(f"Corte com o eixo y: (0, {corte_y[1]:.2f})")


def plotar_funcao_segundo_grau(a, b, c):
    """
    Plota o gráfico da função do segundo grau ax² + bx + c e mostra o vértice e os pontos de corte com os eixos.

    Parâmetros:
    a (float): Coeficiente quadrático.
    b (float): Coeficiente linear.
    c (float): Coeficiente constante.
    """
    if a == 0:
        print("Erro: O coeficiente 'a' não pode ser zero para uma função do segundo grau.")
        return

    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c

    xv = -b / (2 * a)
    yv = a * xv**2 + b * xv + c

    corte_y = (0, c)

    delta = b**2 - 4 * a * c
    if delta < 0:
        print("A função não corta o eixo x (não há raízes reais).")
        cortes_x = None
    elif delta == 0:
        x1 = -b / (2 * a)
        cortes_x = [(x1, 0)]
        print(f"A função toca o eixo x em: ({x1:.2f}, 0)")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        cortes_x = [(x1, 0), (x2, 0)]
        print(f"A função corta o eixo x em: ({x1:.2f}, 0) e ({x2:.2f}, 0)")

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"y = {a}x² + {b}x + {c}", color="blue")

    plt.scatter(xv, yv, color="red", label=f"Vértice: ({xv:.2f}, {yv:.2f})")

    if cortes_x:
        for corte in cortes_x:
            plt.scatter(*corte, color="green", label=f"Corte com eixo x: ({corte[0]:.2f}, 0)")

    plt.scatter(*corte_y, color="purple", label=f"Corte com eixo y: (0, {corte_y[1]:.2f})")

    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)

    plt.title(f"Gráfico da Função do Segundo Grau: y = {a}x² + {b}x + {c}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

    print("\nCoordenadas:")
    print(f"Vértice: ({xv:.2f}, {yv:.2f})")
    if cortes_x:
        for corte in cortes_x:
            print(f"Corte com o eixo x: ({corte[0]:.2f}, 0)")
    else:
        print("A função não corta o eixo x.")
    print(f"Corte com o eixo y: (0, {corte_y[1]:.2f})")



def integral(funcao_str, a, b):
    """
    Calcula a integral definida de uma função matemática.

    Parâmetros:
    funcao_str (str): A função matemática como uma string (ex: "x**2 + 3*x + 2").
    a (float): Limite inferior de integração.
    b (float): Limite superior de integração.

    Retorna:
    float: O valor da integral definida.
    """
    try:
        # Define a função a partir da string fornecida
        funcao = lambda x: eval(funcao_str, {"x": x, "math": math, "np": np})

        # Calcula a integral definida
        resultado, _ = quad(funcao, a, b)
        return resultado
    except Exception as e:
        return f"Erro: {e}"


def calcular_derivada(funcao_str, x0, dx=1e-6):
    """
    Calcula a derivada de uma função em um ponto específico usando diferenças finitas.

    Parâmetros:
    funcao_str (str): A função como uma string (ex: "x**2 + 3*x + 2").
    x0 (float): O ponto onde a derivada será calculada.
    dx (float): O passo para o cálculo numérico (opcional, padrão é 1e-6).

    Retorna:
    float: O valor da derivada no ponto x0.
    """
    try:
        # Verifica se o x0 é numérico
        x0 = float(x0)

        # Verifica se a função é uma string válida
        if not isinstance(funcao_str, str):
            raise ValueError("A função precisa ser fornecida como uma string.")

        # Define a função a partir da string fornecida
        funcao = lambda x: eval(funcao_str, {"x": x, "math": math, "np": np})

        # Aproximação da derivada usando a fórmula de diferenças finitas centrais
        derivada = (funcao(x0 + dx) - funcao(x0 - dx)) / (2 * dx)
        
        return derivada
    except ValueError as e:
        return f"Erro de valor: {e}"
    except Exception as e:
        return f"Erro: {e}"



# Ajustar o menu da calculadora
def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potenciação")
        print("6. Radiciação")
        print("7. Fatorial")
        print("8. Logaritmo")
        print("9. Teorema de Pitágoras")
        print("10. Equação do primeiro grau")
        print("11. Equação do segundo grau")
        print("12. Seno, Cosseno e Tangente")
        print("13. Função do primeiro grau (gráfico)")
        print("14. Função do segundo grau (gráfico)")
        print("15. Integral definida")
        print("16. Derivada")
        print("17. Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17): ")

        # Sair do programa
        if escolha == '17':
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
        elif escolha == '7':
            try:
                num = int(input("Digite o número para calcular o fatorial: "))
                if num < 0:
                    print("Erro: Fatorial não é definido para números negativos.")
                    continue
                print(f"Resultado: {fatorial(num)}")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número inteiro.")

        # Logaritmo
        elif escolha == '8':
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
        elif escolha == '9':
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
        elif escolha == '10':
            try:
                print("Atribua os valores da equação na forma Ax + B = 0")
                a = float(input("Digite o valor de A: "))
                b = float(input("Digite o valor de B: "))
                resultado = equacao_primeiro_grau(a, b)
                print(f"O valor de x é: {resultado}")
            except ValueError:
                print("Entrada inválida! Por favor, digite números.")

        # Equação do segundo grau
        elif escolha == '11':
            try:
                print("Atribua os valores da equação na forma Ax² + Bx + C = 0")
                a = float(input("Digite o valor de A: "))
                b = float(input("Digite o valor de B: "))
                c = float(input("Digite o valor de C: "))
                resultado = equacao_segundo_grau(a, b, c)
                print(f"Os valores da função são: {resultado}")
            except ValueError:
                print("Entrada inválida! Por favor, digite números.")

        # Trigonometria
        elif escolha == '12':
            try:
                print("Atribua o valor do ângulo: ")
                x = float(input("Digite o valor do ângulo: "))
                em_graus = input("O ângulo está em graus? (s/n): ").strip().lower() == 's'
                resultado = trigonometria(x, em_graus)
            except ValueError:
                print("Entrada inválida! Por favor, digite um número.")

        # Gráfico de Função do Primeiro Grau
        elif escolha == '13':
            try:
                print("Atribua os valores da função na forma y = Ax + B")
                a = float(input("Digite o valor de A (coeficiente angular): "))
                b = float(input("Digite o valor de B (coeficiente linear): "))
                plotar_funcao_primeiro_grau(a, b)
            except ValueError:
                print("Entrada inválida! Por favor, digite números.")

        # Gráfico de Função do Segundo Grau
        elif escolha == '14':
            try:
                print("Atribua os valores da função na forma y = Ax² + Bx + C")
                a = float(input("Digite o valor de A (coeficiente quadrático): "))
                b = float(input("Digite o valor de B (coeficiente linear): "))
                c = float(input("Digite o valor de C (coeficiente constante): "))
                plotar_funcao_segundo_grau(a, b, c)
            except ValueError:
                print("Entrada inválida! Por favor, digite números.")



        # Radiciação
        elif escolha == '6':
            try:
                print("Atribua os valores da raiz, sendo o primeiro número a BASE e o segundo o ÍNDICE.")
                x = float(input("Digite o valor da Base: "))
                y = int(input("Digite o valor do Índice: "))
                resultado = raiz(x, y)
                print(f"O resultado da {y}√{x} = {resultado:.2f}")
            except ValueError:
                print("Entrada inválida! Por favor, digite números.")


      # Integral definida
        elif escolha == '15':
            try:
                funcao_str = input("Digite a função (use 'x' como variável, ex: 'x**2 + 3*x + 2'): ")
                a = float(input("Digite o limite inferior de integração (a): "))
                b = float(input("Digite o limite superior de integração (b): "))
                resultado = integral(funcao_str, a, b)
                print(f"O valor da integral definida é: {resultado:.4f}")
            except ValueError:
                print("Entrada inválida! Por favor, digite números e uma função válida.")


      # Derivada
        elif escolha == '16': 
            try:
                funcao_str = input("Digite a função (use 'x' como variável, ex: 'x**2 + 3*x + 2'): ")
                x0 = float(input("Digite o ponto onde a derivada será calculada (x0): "))
                resultado = calcular_derivada(funcao_str, x0)
                print(f"O valor da derivada no ponto {x0} é: {resultado:.4f}")
            except ValueError:
                print("Entrada inválida! Por favor, digite números e uma função válida.")

        else:
                    print("Opção inválida! Tente novamente.")


# Executar a calculadora
if __name__ == "__main__":
    calculadora()
