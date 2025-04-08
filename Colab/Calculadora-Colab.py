!pip install ipywidgets matplotlib
import ipywidgets as widgets
from IPython.display import display, clear_output

import ipywidgets as widgets
from IPython.display import display, clear_output
import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import statistics
import cmath

# Widgets
menu = widgets.Dropdown(
    options=['Adição', 'Subtração', 'Multiplicação', 'Divisão', 'Potenciação',
             'Radiciação', 'Fatorial', 'Trigonometria', 'Teorema de Pitágoras',
             'Equação 1º grau', 'Equação 2º grau', 'Logaritmo', 'Derivada', 'Integral',
             'Gráfico de função', 'Estatística', 'Regra de três', 'Conversão de temperatura',
             'Números complexos'],
    description='Função:'
)

entrada1 = widgets.FloatText(description='Valor 1:')
entrada2 = widgets.FloatText(description='Valor 2:')
entrada3 = widgets.FloatText(description='Valor 3:')
tipo_box = widgets.ToggleButtons(options=['Diretamente proporcional', 'Inversamente proporcional'], description='Tipo:')
tipo_temp = widgets.ToggleButtons(options=['C→F', 'F→C'], description='Tipo:')
expr_input = widgets.Text(description='Expressão:', placeholder='Ex: x**2 + 3*x')
valores_lista = widgets.Text(description='Valores:', placeholder='Ex: 1,2,2,3,4')
# Campos extras para número complexo
z1_real = widgets.FloatText(description='z1 real:')
z1_imag = widgets.FloatText(description='z1 imag:')
z2_real = widgets.FloatText(description='z2 real:')
z2_imag = widgets.FloatText(description='z2 imag:')

botao = widgets.Button(description='Calcular')
saida = widgets.Output()

def calcular_operacao(b):
    with saida:
        clear_output()
        try:
            op = menu.value
            a = entrada1.value
            b_val = entrada2.value
            c = entrada3.value
            tipo = tipo_box.value
            temp_tipo = tipo_temp.value
            expr = expr_input.value
            lista = []

            if op == 'Estatística':
                if not valores_lista.value.strip():
                    print("Insira os valores separados por vírgula, exemplo: 1,2,2,3")
                    return
                lista = list(map(float, valores_lista.value.replace(' ', '').split(',')))

            if op == 'Adição':
                print(f'Resultado: {a + b_val}')
            elif op == 'Subtração':
                print(f'Resultado: {a - b_val}')
            elif op == 'Multiplicação':
                print(f'Resultado: {a * b_val}')
            elif op == 'Divisão':
                print(f'Resultado: {a / b_val}')
            elif op == 'Potenciação':
                print(f'Resultado: {a ** b_val}')
            elif op == 'Radiciação':
                print(f'Resultado: {a ** (1/b_val)}')
            elif op == 'Fatorial':
                print(f'Resultado: {math.factorial(int(a))}')
            elif op == 'Trigonometria':
                print(f'sin({a}) = {math.sin(math.radians(a))}')
                print(f'cos({a}) = {math.cos(math.radians(a))}')
                print(f'tan({a}) = {math.tan(math.radians(a))}')
            elif op == 'Teorema de Pitágoras':
                print(f'Hipotenusa: {math.hypot(a, b_val)}')
            elif op == 'Equação 1º grau':
                if a != 0:
                    print(f'Solução: x = {-b_val/a}')
                else:
                    print('Coeficiente "a" não pode ser zero.')
            elif op == 'Equação 2º grau':
                delta = b_val**2 - 4*a*c
                if delta < 0:
                    print('Sem raízes reais')
                elif delta == 0:
                    print(f'Raiz única: {-b_val / (2*a)}')
                else:
                    x1 = (-b_val + math.sqrt(delta)) / (2*a)
                    x2 = (-b_val - math.sqrt(delta)) / (2*a)
                    print(f'Raízes: x1 = {x1}, x2 = {x2}')
            elif op == 'Logaritmo':
                print(f'Log base {b_val} de {a}: {math.log(a, b_val)}')
            elif op == 'Derivada':
                x = sp.symbols('x')
                f = sp.sympify(expr)
                derivada = sp.diff(f, x)
                print(f'Derivada: {derivada}')
            elif op == 'Integral':
                x = sp.symbols('x')
                f = sp.sympify(expr)
                integral = sp.integrate(f, x)
                print(f'Integral: {integral}')
            elif op == 'Gráfico de função':
                x_vals = np.linspace(-10, 10, 400)
                x = sp.symbols('x')
                f = sp.lambdify(x, sp.sympify(expr), 'numpy')
                y_vals = f(x_vals)
                plt.plot(x_vals, y_vals)
                plt.title(f'Gráfico de {expr}')
                plt.grid(True)
                plt.show()
            elif op == 'Estatística':
                print(f'Média: {statistics.mean(lista)}')
                print(f'Mediana: {statistics.median(lista)}')
                print(f'Moda: {statistics.mode(lista)}')
                print(f'Desvio padrão: {statistics.stdev(lista)}')
            elif op == 'Regra de três':
                if tipo == "Diretamente proporcional":
                    print(f'Resultado: {(b_val * c) / a}')
                else:
                    print(f'Resultado: {(a * b_val) / c}')
            elif op == 'Conversão de temperatura':
                if temp_tipo == 'C→F':
                    print(f'{a}°C = {a * 9/5 + 32}°F')
                else:
                    print(f'{a}°F = {(a - 32) * 5/9}°C')
            elif op == 'Números complexos':
                z1 = complex(z1_real.value, z1_imag.value)
                z2 = complex(z2_real.value, z2_imag.value)
                print(f'z1 = {z1}, z2 = {z2}')
                print(f'z1 + z2 = {z1 + z2}')
                print(f'z1 - z2 = {z1 - z2}')
                print(f'z1 * z2 = {z1 * z2}')
                if z2 != 0:
                    print(f'z1 / z2 = {z1 / z2}')
                print(f'Módulo de z1: {abs(z1)}')
                print(f'Conjugado de z1: {z1.conjugate()}')
                print(f'Forma polar de z1: ({abs(z1)}, {cmath.phase(z1)} rad)')
                print(f'z1² = {z1**2}')
                print(f'Raiz quadrada de z1: {cmath.sqrt(z1)}')
        except Exception as e:
            print(f"Erro: {e}")

botao.on_click(calcular_operacao)

def atualizar_visibilidade_campos(change=None):
    op = menu.value
    entrada1.layout.display = entrada2.layout.display = entrada3.layout.display = 'none'
    tipo_box.layout.display = tipo_temp.layout.display = expr_input.layout.display = valores_lista.layout.display = 'none'
    z1_real.layout.display = z1_imag.layout.display = z2_real.layout.display = z2_imag.layout.display = 'none'

    if op in ['Adição', 'Subtração', 'Multiplicação', 'Divisão', 'Potenciação', 'Radiciação']:
        entrada1.layout.display = 'block'
        entrada2.layout.display = 'block'
    elif op in ['Fatorial', 'Trigonometria']:
        entrada1.layout.display = 'block'
    elif op == 'Teorema de Pitágoras':
        entrada1.layout.display = entrada2.layout.display = 'block'
    elif op == 'Equação 1º grau':
        entrada1.layout.display = entrada2.layout.display = 'block'
    elif op == 'Equação 2º grau':
        entrada1.layout.display = entrada2.layout.display = entrada3.layout.display = 'block'
    elif op == 'Logaritmo':
        entrada1.layout.display = entrada2.layout.display = 'block'
    elif op in ['Derivada', 'Integral', 'Gráfico de função']:
        expr_input.layout.display = 'block'
    elif op == 'Estatística':
        valores_lista.layout.display = 'block'
    elif op == 'Regra de três':
        entrada1.layout.display = entrada2.layout.display = entrada3.layout.display = 'block'
        tipo_box.layout.display = 'block'
    elif op == 'Conversão de temperatura':
        entrada1.layout.display = 'block'
        tipo_temp.layout.display = 'block'
    elif op == 'Números complexos':
        z1_real.layout.display = z1_imag.layout.display = z2_real.layout.display = z2_imag.layout.display = 'block'

menu.observe(atualizar_visibilidade_campos, names='value')
atualizar_visibilidade_campos()

display(menu, entrada1, entrada2, entrada3, tipo_box, tipo_temp, expr_input,
        valores_lista, z1_real, z1_imag, z2_real, z2_imag, botao, saida)


with open('historico_calc.json') as f:
    historico = json.load(f)
for item in historico:
    print(item)
