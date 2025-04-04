import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, integrate, Eq, solve, sympify, lambdify
from scipy import stats
from datetime import datetime
import logging
import math
import json

class CalculadoraCientifica:
    def __init__(self):
        self.historico = []
        try:
            with open('historico.json', 'r') as f:
                self.historico = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.historico = []

    def salvar_historico(self):
        with open('historico.json', 'w') as f:
            json.dump(self.historico, f)

    def menu_principal(self):
        """Exibe o menu principal"""
        print("\n" + "="*40)
        print(" CALCULADORA CIENTÍFICA ".center(40, '#'))
        print("="*40)
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
        print("12. Cálculo Estatístico")
        print("13. Regra de três")
        print("14. Conversão de Temperatura")
        print("15. Números Complexos")
        print("16. Ver Histórico")
        print("17. Sair")
        print("="*40)

    def operacoes_basicas(self):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"Soma: {num1 + num2}")
        print(f"Subtração: {num1 - num2}")
        print(f"Multiplicação: {num1 * num2}")
        print(f"Divisão: {num1 / num2 if num2 != 0 else 'Erro: Divisão por zero'}")
        self.adicionar_ao_historico("Operações Básicas", f"{num1} e {num2}")

    def potenciação(self):
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))
        resultado = base ** expoente
        print(f"Resultado: {resultado}")
        self.adicionar_ao_historico("Potenciação", f"{base}^{expoente} = {resultado}")

    def radiciacao(self):
        numero = float(input("Digite o número: "))
        indice = float(input("Digite o índice da raiz (exemplo, para a raiz quadrada, digite 2): "))
        resultado = numero ** (1 / indice)
        print(f"Resultado: {resultado}")
        self.adicionar_ao_historico("Radiciação", f"raiz {indice} de {numero} = {resultado}")

    def fatorial(self):
        try:
            numero = int(input("Digite o número para calcular o fatorial: "))
            if numero < 0:
                raise ValueError("O fatorial só está definido para números não negativos.")
            resultado = math.factorial(numero)
            print(f"Fatorial de {numero}: {resultado}")
            self.adicionar_ao_historico("Fatorial", f"{numero}! = {resultado}") 
        except ValueError as e:
            print(f"Erro: {e}")

    def pitagoras(self):
        a = float(input("Digite o valor do cateto a: "))
        b = float(input("Digite o valor do cateto b: "))
        c = np.sqrt(a**2 + b**2)
        print(f"A hipotenusa é: {c}")
        self.adicionar_ao_historico("Teorema de Pitágoras", f"Catetos {a} e {b} → Hipotenusa {c}")

    def equacoes(self):
        tipo = input("Digite 1 para equação do 1º grau ou 2 para equação do 2º grau: ")
        if tipo == '1':
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            if a != 0:
                x = -b / a
                print(f"A solução da equação é: x = {x}")
                self.adicionar_ao_historico("Equação 1º grau", f"{a}x + {b} = 0 → x = {x}")
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
                self.adicionar_ao_historico("Equação 2º grau", f"{a}x² + {b}x + {c} = 0 → x1={x1}, x2={x2}")
            else:
                print("Não existem soluções reais.")
        else:
            print("Opção inválida.")

    def trigonometria(self):
        angulo = float(input("Digite o ângulo em graus: "))
        angulo_rad = np.radians(angulo)
        seno = np.sin(angulo_rad)
        cosseno = np.cos(angulo_rad)
        tangente = np.tan(angulo_rad)
        print(f"Seno: {seno}")
        print(f"Cosseno: {cosseno}")
        print(f"Tangente: {tangente}")
        self.adicionar_ao_historico("Trigonometria", f"Ângulo {angulo}° → sen={seno:.4f}, cos={cosseno:.4f}, tan={tangente:.4f}")

    def logaritmos(self):
        numero = float(input("Digite o número: "))
        base = float(input("Digite a base do logaritmo: "))
        if numero > 0 and base > 0 and base != 1:
            resultado = np.log(numero) / np.log(base)
            print(f"Logaritmo de {numero} na base {base}: {resultado}")
            self.adicionar_ao_historico("Logaritmo", f"log{base}({numero}) = {resultado:.4f}")
        else:
            print("Entradas inválidas para o cálculo de logaritmo")

    def derivada(self):
        x = symbols('x')
        funcao_str = input("Digite a função em termos de x (ex: x**2 + 3*x - 4): ")
        derivada = diff(funcao_str, x)
        print(f"A derivada da função é: {derivada}")
        self.adicionar_ao_historico("Derivada", f"d/dx({funcao_str}) = {derivada}")

    def integral(self):
        x = symbols('x')
        funcao_str = input("Digite a função em termos de x (ex: x**2 + 3*x - 4): ")
        integral = integrate(funcao_str, x)
        print(f"A integral da função é: {integral}")
        self.adicionar_ao_historico("Integral", f"∫({funcao_str})dx = {integral}")

    def grafico(self):
        funcao_str = input("Digite a função para o gráfico (ex: x**2 + 3*x - 4): ")
        try:
            x = symbols('x')
            expr = sympify(funcao_str)  
            funcao = lambdify(x, expr, modules=['numpy'])  
            x_vals = np.linspace(-10, 10, 400)
            y_vals = funcao(x_vals)
            plt.plot(x_vals, y_vals)
            plt.title(f"Gráfico da função: {funcao_str}")
            plt.grid(True)
            plt.show()
            self.adicionar_ao_historico("Gráfico", f"Função: {funcao_str}")
        except Exception as e:
            print(f"Erro ao processar a função: {e}")

    def estatisticas(self):
        dados = list(map(float, input("Digite os dados separados por espaço: ").split()))
        media = np.mean(dados)
        mediana = np.median(dados)
        variancia = np.var(dados)
        desvio_padrao = np.std(dados)

        moda_resultado = stats.mode(dados)
        if isinstance(moda_resultado.mode, np.ndarray):
            modas = moda_resultado.mode
            moda_str = ', '.join(map(str, modas)) if len(modas) > 1 else str(modas[0])
        else:
            moda_str = str(moda_resultado.mode)

        print(f"Média: {media}")
        print(f"Mediana: {mediana}")
        print(f"Moda: {moda_str}")
        print(f"Variância: {variancia}")
        print(f"Desvio padrão: {desvio_padrao}")
        self.adicionar_ao_historico("Estatísticas", f"Dados: {len(dados)} valores → Média={media:.2f}")

    def regra_tres(self):
        print("1. Diretamente Proporcional")
        print("2. Inversamente Proporcional")
        tipo = input("Escolha o tipo: ")
        a = float(input("Valor de a: "))
        b = float(input("Valor de b: "))
        c = float(input("Valor de c: "))

        if tipo == '1':
            d = (b * c) / a
            operacao = f"{a}/{b} = {c}/x → x = {d:.2f}"
        else:
            d = (a * b) / c
            operacao = f"{a}*{b} = {c}*x → x = {d:.2f}"

        print(f"O valor de d é: {d}")
        self.adicionar_ao_historico("Regra de Três", operacao)

    def conversao_temperatura(self):
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        opcao = input("Escolha a conversão: ")
        temp = float(input("Digite a temperatura: "))

        if opcao == '1':
            resultado = (temp * 9/5) + 32
            print(f"{temp}°C = {resultado}°F")
            self.adicionar_ao_historico("Conversão", f"{temp}°C → {resultado}°F")
        else:
            resultado = (temp - 32) * 5/9
            print(f"{temp}°F = {resultado}°C")
            self.adicionar_ao_historico("Conversão", f"{temp}°F → {resultado}°C")

    def numeros_complexos(self):
        print("\nOperações com Números Complexos")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Conjugado")
        print("6. Módulo")
        print("7. Forma Polar")
        print("8. Potenciação")
        print("9. Raízes")
        op = input("Escolha a operação (1-9): ")

        try:
            if op in ['1', '2', '3', '4']:
                print("\nDigite os números no formato a+bj (ex: 3+4j)")
                a = complex(input("Primeiro número complexo: "))
                b = complex(input("Segundo número complexo: "))

                if op == '1':
                    resultado = a + b
                    print(f"\n{a} + {b} = {resultado}")
                    self.adicionar_ao_historico("Complexos - Soma", f"{a} + {b} = {resultado}")
                elif op == '2':
                    resultado = a - b
                    print(f"\n{a} - {b} = {resultado}")
                    self.adicionar_ao_historico("Complexos - Subtração", f"{a} - {b} = {resultado}")
                elif op == '3':
                    resultado = a * b
                    print(f"\n{a} * {b} = {resultado}")
                    self.adicionar_ao_historico("Complexos - Multiplicação", f"{a} * {b} = {resultado}")
                elif op == '4':
                    resultado = a / b
                    print(f"\n{a} / {b} = {resultado}")
                    self.adicionar_ao_historico("Complexos - Divisão", f"{a} / {b} = {resultado}")

            elif op == '5':
                num = complex(input("\nDigite o número complexo (formato a+bj): "))
                conjugado = num.real - num.imag*1j
                print(f"\nConjugado de {num} = {conjugado}")
                self.adicionar_ao_historico("Complexos - Conjugado", f"{num} → {conjugado}")

            elif op == '6':
                num = complex(input("\nDigite o número complexo (formato a+bj): "))
                modulo = abs(num)
                print(f"\nMódulo de {num} = {modulo}")
                self.adicionar_ao_historico("Complexos - Módulo", f"{num} → {modulo:.2f}")

            elif op == '7':
                num = complex(input("\nDigite o número complexo (formato a+bj): "))
                r = abs(num)
                theta = np.angle(num, deg=True)
                print(f"\nForma polar de {num}:")
                print(f"Módulo: {r:.2f}")
                print(f"Ângulo: {theta:.2f}°")
                self.adicionar_ao_historico("Complexos - Polar", f"{num} → {r:.2f}∠{theta:.2f}°")

            elif op == '8':
                num = complex(input("\nDigite o número complexo (formato a+bj): "))
                exp = int(input("Digite o expoente inteiro: "))
                resultado = num**exp
                print(f"\n{num}^{exp} = {resultado}")
                self.adicionar_ao_historico("Complexos - Potenciação", f"{num}^{exp} = {resultado}")

            elif op == '9':
                num = complex(input("\nDigite o número complexo (formato a+bj): "))
                n = int(input("Digite a ordem da raiz (ex: 2 para raiz quadrada): "))
                r = abs(num)**(1/n)
                theta = np.angle(num)

                print(f"\nRaízes {n}ésimas de {num}:")
                for k in range(n):
                    root = r * (np.cos((theta + 2*np.pi*k)/n) + 1j*np.sin((theta + 2*np.pi*k)/n))
                    print(f"Raiz {k+1}: {root:.4f}")
                self.adicionar_ao_historico("Complexos - Raízes", f"{n}√{num}")

            else:
                print("Opção inválida!")

        except ValueError:
            print("Formato inválido! Use o formato a+bj (ex: 3+4j)")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def adicionar_ao_historico(self, operacao: str, resultado: str):
        """Registra uma operação no histórico"""
        entrada = {
            'data': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'operacao': operacao,
            'resultado': resultado
        }
        self.historico.append(entrada)
        logging.info(f"Operação registrada: {operacao}")

    def mostrar_historico(self):
        """Exibe o histórico de operações"""
        print("\n" + "="*40)
        print(" HISTÓRICO ".center(40))
        print("="*40)
        if not self.historico:
            print("Nenhuma operação registrada.")
        else:
            for i, item in enumerate(self.historico, 1):
                print(f"{i}. [{item['data']}] {item['operacao']} → {item['resultado']}")
        print("="*40)

    def executar(self):
        """Método principal para executar a calculadora"""
        while True:
            self.menu_principal()
            escolha = input("\nEscolha uma opção (1-17): ")
            if not escolha.isdigit() or int(escolha) not in range(1, 18):
                print("Opção inválida! Digite um número entre 1 e 17.")
                continue

            try:
                if escolha == '1':
                    self.operacoes_basicas()
                elif escolha == '2':
                    self.potenciação()
                elif escolha == '3':
                    self.radiciacao()
                elif escolha == '4':
                    self.fatorial()
                elif escolha == '5':
                    self.pitagoras()
                elif escolha == '6':
                    self.equacoes()
                elif escolha == '7':
                    self.trigonometria()
                elif escolha == '8':
                    self.logaritmos()
                elif escolha == '9':
                    self.derivada()
                elif escolha == '10':
                    self.integral()
                elif escolha == '11':
                    self.grafico()
                elif escolha == '12':
                    self.estatisticas()
                elif escolha == '13':
                    self.regra_tres()
                elif escolha == '14':
                    self.conversao_temperatura()
                elif escolha == '15':
                    self.numeros_complexos()
                elif escolha == '16':
                    self.mostrar_historico()
                elif escolha == '17':
                    self.salvar_historico()  
                    print("\nObrigado por usar a Calculadora Científica!")
                    break
                else:
                    print("\nOpção inválida! Tente novamente.")

                input("\nPressione Enter para continuar...")

            except KeyboardInterrupt:
                print("\nOperação cancelada pelo usuário")
                break
            except Exception as e:
                print(f"\nErro inesperado: {e}")
                logging.error(f"Erro não tratado: {e}")

if __name__ == "__main__":
    calculadora = CalculadoraCientifica()
    calculadora.executar()
