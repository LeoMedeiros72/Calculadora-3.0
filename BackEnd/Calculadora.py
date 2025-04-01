import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, integrate, Eq, solve
from scipy import stats

def menu():
    print("\nCalculadora Educacional")
    print("1. Operações Básicas (Adição, Subtração, Multiplicação, Divisão)")
    print("2. Potenciação")
    print("3. Radiciação")
    print("4. Fatorial")
    print("5. Teorema de Pitágoras")
    print("6. Equações do 1º e 2º grau")
    print("7. Trigonometria (Seno, Cosseno, Tangente)")
    print("8. Logaritmos")
    print("9. Derivada de uma Função")
    print("10. Integral de uma Função")
    print("11. Gráfico de Função")
    print("12. Cálculo Estatístico (Média, Mediana, Moda, Variância, Desvio Padrão)")
    print("13. Regra de três (diretamente ou inversamente proporcional)")
    print("14. Conversão de Temperatura (Celsius para Fahrenheit ou Fahrenheit para Celsius)")
    print("15. Sair")


def operacoes_basicas():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(f"Soma: {num1 + num2}")
    print(f"Subtração: {num1 - num2}")
    print(f"Multiplicação: {num1 * num2}")
    print(f"Divisão: {num1 / num2 if num2 != 0 else 'Erro: Divisão por zero'}")

def potenciação():
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    print(f"Resultado: {base ** expoente}")

def radiciacao():
    numero = float(input("Digite o número: "))
    indice = float(input("Digite o índice da raiz (exemplo, para a raiz quadrada, digite 2): "))
    print(f"Resultado: {numero ** (1 / indice)}")

def fatorial():
    numero = int(input("Digite o número para calcular o fatorial: "))
    print(f"Fatorial de {numero}: {np.math.factorial(numero)}")

def pitagoras():
    a = float(input("Digite o valor do cateto a: "))
    b = float(input("Digite o valor do cateto b: "))
    c = np.sqrt(a**2 + b**2)
    print(f"A hipotenusa é: {c}")

def equacoes():
    tipo = input("Digite 1 para equação do 1º grau ou 2 para equação do 2º grau: ")
    if tipo == '1':
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        if a != 0:
            x = -b / a
            print(f"A solução da equação é: x = {x}")
        else:
            print("Não é uma equação do 1º grau.")
    elif tipo == '2':
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        delta = b**2 - 4*a*c
        if delta >= 0:
            x1 = (-b + np.sqrt(delta)) / (2*a)
            x2 = (-b - np.sqrt(delta)) / (2*a)
            print(f"As soluções da equação são: x1 = {x1} e x2 = {x2}")
        else:
            print("Não existem soluções reais.")
    else:
        print("Opção inválida.")

def trigonometria():
    angulo = float(input("Digite o ângulo em graus: "))
    angulo_rad = np.radians(angulo)
    print(f"Seno: {np.sin(angulo_rad)}")
    print(f"Cosseno: {np.cos(angulo_rad)}")
    print(f"Tangente: {np.tan(angulo_rad)}")

def logaritmos():
    numero = float(input("Digite o número: "))
    base = float(input("Digite a base do logaritmo: "))
    if numero > 0 and base > 0 and base != 1:
        print(f"Logaritmo de {numero} na base {base}: {np.log(numero) / np.log(base)}")
    else:
        print("Entradas inválidas para o cálculo de logaritmo.")

def derivada():
    x = symbols('x')
    funcao_str = input("Digite a função em termos de x (ex: x**2 + 3*x - 4): ")
    funcao = eval('lambda x: ' + funcao_str)
    derivada = diff(funcao_str, x)
    print(f"A derivada da função é: {derivada}")

def integral():
    x = symbols('x')
    funcao_str = input("Digite a função em termos de x (ex: x**2 + 3*x - 4): ")
    funcao = eval('lambda x: ' + funcao_str)
    integral = integrate(funcao_str, x)
    print(f"A integral da função é: {integral}")

def grafico():
    funcao_str = input("Digite a função para o gráfico (ex: x**2 + 3*x - 4): ")
    funcao = lambda x: eval(funcao_str)
    x_vals = np.linspace(-10, 10, 400)
    y_vals = funcao(x_vals)
    plt.plot(x_vals, y_vals)
    plt.title(f"Gráfico da função: {funcao_str}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

def estatisticas():
    dados = list(map(float, input("Digite os dados separados por espaço: ").split()))
    print(f"Média: {np.mean(dados)}")
    print(f"Mediana: {np.median(dados)}")

    moda_resultado = stats.mode(dados)
    if isinstance(moda_resultado.mode, np.ndarray):  # Verifica se é um array
        modas = moda_resultado.mode
        if len(modas) > 1:
            print(f"Modas: {', '.join(map(str, modas))}")
        else:
            print(f"Moda: {modas[0]}")
    else:
        print(f"Moda: {moda_resultado.mode}")

    print(f"Variância: {np.var(dados)}")
    print(f"Desvio padrão: {np.std(dados)}")

def regra_tres():
    print("1. Diretamente Proporcional")
    print("2. Inversamente Proporcional")
    tipo = input("Escolha o tipo: ")
    a = float(input("Valor de a: "))
    b = float(input("Valor de b: "))
    c = float(input("Valor de c: "))
    if tipo == '1':
        d = (b * c) / a
    else:
        d = (a * b) / c
    print(f"O valor de d é: {d}")

def conversao_temperatura():
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    opcao = input("Escolha a conversão: ")
    temp = float(input("Digite a temperatura: "))
    if opcao == '1':
        print(f"{temp}°C = {(temp * 9/5) + 32}°F")
    else:
        print(f"{temp}°F = {(temp - 32) * 5/9}°C")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            operacoes_basicas()
        elif escolha == '2':
            potenciação()
        elif escolha == '3':
            radiciacao()
        elif escolha == '4':
            fatorial()
        elif escolha == '5':
            pitagoras()
        elif escolha == '6':
            equacoes()
        elif escolha == '7':
            trigonometria()
        elif escolha == '8':
            logaritmos()
        elif escolha == '9':
            derivada()
        elif escolha == '10':
            integral()
        elif escolha == '11':
            grafico()
        elif escolha == '12':
            estatisticas()
        elif escolha == '13':
            regra_tres()
        elif escolha == '14':
            conversao_temperatura()
        elif escolha == '15':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
