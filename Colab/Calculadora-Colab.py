!pip install ipywidgets matplotlib
import ipywidgets as widgets
from IPython.display import display, clear_output
import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import statistics
import cmath
import json
from IPython.display import HTML

# Estilo CSS personalizado aprimorado
style = """
<style>
.widget-label {
    font-weight: bold !important;
    color: #2c3e50 !important;
    min-width: 120px !important;
}
.widget-button {
    background-color: #3498db !important;
    color: white !important;
    font-weight: bold !important;
    border: none !important;
    margin: 10px 0 !important;
}
.widget-button:hover {
    background-color: #2980b9 !important;
}
.widget-dropdown {
    border: 1px solid #3498db !important;
}
.widget-output {
    border: 1px solid #ddd !important;
    padding: 15px !important;
    margin-top: 15px !important;
    border-radius: 5px !important;
    background-color: #f9f9f9 !important;
}
.calculator-title {
    color: #2c3e50;
    text-align: center;
    margin-bottom: 20px;
    font-size: 24px;
    font-weight: bold;
}
.instructions {
    background-color: #e8f4fc;
    padding: 12px;
    border-radius: 5px;
    margin: 10px 0;
    border-left: 4px solid #3498db;
}
.section-title {
    color: #3498db;
    font-weight: bold;
    margin: 15px 0 5px 0;
}
.input-group {
    margin-bottom: 10px;
}
.complex-section {
    margin: 15px 0;
    padding: 10px;
    background-color: #f5f5f5;
    border-radius: 5px;
    border: 1px solid #ddd;
}
.hidden {
    display: none !important;
}
</style>
"""

# Aplicar o estilo
display(HTML(style))

# Widgets
menu = widgets.Dropdown(
    options=['Adição', 'Subtração', 'Multiplicação', 'Divisão', 'Potenciação',
             'Radiciação', 'Fatorial', 'Trigonometria', 'Teorema de Pitágoras',
             'Equação 1º grau', 'Equação 2º grau', 'Logaritmo', 'Derivada', 'Integral',
             'Gráfico de função', 'Estatística', 'Regra de três', 'Conversão de temperatura',
             'Números complexos'],
    description='Selecione a função:',
    style={'description_width': 'initial'},
    layout={'width': '90%'}
)

# Área de instruções dinâmica
instructions = widgets.HTML(
    value="<div class='instructions'>Selecione uma função acima para ver as instruções e os campos necessários.</div>",
    layout={'margin': '10px 0'}
)

# Campos de entrada numéricos
entrada1 = widgets.FloatText(description='Valor 1:', style={'description_width': 'initial'}, layout={'width': '90%'})
entrada2 = widgets.FloatText(description='Valor 2:', style={'description_width': 'initial'}, layout={'width': '90%'})
entrada3 = widgets.FloatText(description='Valor 3:', style={'description_width': 'initial'}, layout={'width': '90%'})

# Opções para regra de três e temperatura
tipo_box = widgets.ToggleButtons(
    options=['Diretamente proporcional', 'Inversamente proporcional'], 
    description='Tipo de proporção:',
    style={'description_width': 'initial'},
    layout={'width': '90%'}
)
tipo_temp = widgets.ToggleButtons(
    options=['Celsius → Fahrenheit', 'Fahrenheit → Celsius'], 
    description='Conversão:',
    style={'description_width': 'initial'},
    layout={'width': '90%'}
)

# Campos para expressões e listas
expr_input = widgets.Text(
    description='Expressão matemática:', 
    placeholder='Ex: x**2 + 3*x ou sin(x)',
    style={'description_width': 'initial'},
    layout={'width': '90%'}
)
valores_lista = widgets.Text(
    description='Lista de valores:', 
    placeholder='Ex: 1, 2, 2, 3, 4 (separados por vírgula)',
    style={'description_width': 'initial'},
    layout={'width': '90%'}
)

# Campos para números complexos (agora em containers separados)
complex_container = widgets.VBox([
    widgets.HTML(value="<div class='section-title'>Números Complexos</div>"),
    widgets.VBox([
        widgets.HTML(value="<div style='font-weight:bold;'>Número Complexo z₁:</div>"),
        widgets.FloatText(description='Parte real:', style={'description_width': 'initial'}, layout={'width': '90%'}),
        widgets.FloatText(description='Parte imaginária:', style={'description_width': 'initial'}, layout={'width': '90%'})
    ]),
    widgets.VBox([
        widgets.HTML(value="<div style='font-weight:bold;'>Número Complexo z₂:</div>"),
        widgets.FloatText(description='Parte real:', style={'description_width': 'initial'}, layout={'width': '90%'}),
        widgets.FloatText(description='Parte imaginária:', style={'description_width': 'initial'}, layout={'width': '90%'})
    ])
], layout={'margin': '10px 0'}, style={'description_width': 'initial'})

# Acessar os widgets dentro do container
z1_real = complex_container.children[1].children[1]
z1_imag = complex_container.children[1].children[2]
z2_real = complex_container.children[2].children[1]
z2_imag = complex_container.children[2].children[2]

# Botão de cálculo com estilo
botao = widgets.Button(
    description='Calcular', 
    button_style='primary',
    layout={'width': '200px', 'margin': '10px 0'}
)

# Área de saída com estilo
saida = widgets.Output(layout={'border': '1px solid #ddd', 'padding': '15px', 'margin_top': '15px'})

# Dicionário de instruções para cada função
instrucoes = {
    'Adição': 'Digite dois números para somar (Valor 1 + Valor 2).',
    'Subtração': 'Digite dois números para subtrair (Valor 1 - Valor 2).',
    'Multiplicação': 'Digite dois números para multiplicar (Valor 1 × Valor 2).',
    'Divisão': 'Digite dois números para dividir (Valor 1 ÷ Valor 2).',
    'Potenciação': 'Digite a base (Valor 1) e o expoente (Valor 2) para calcular a potência.',
    'Radiciação': 'Digite o radicando (Valor 1) e o índice (Valor 2) para calcular a raiz.',
    'Fatorial': 'Digite um número inteiro (Valor 1) para calcular seu fatorial.',
    'Trigonometria': 'Digite um ângulo em graus (Valor 1) para calcular seno, cosseno e tangente.',
    'Teorema de Pitágoras': 'Digite os dois catetos (Valor 1 e Valor 2) para calcular a hipotenusa.',
    'Equação 1º grau': 'Digite os coeficientes a (Valor 1) e b (Valor 2) da equação ax + b = 0.',
    'Equação 2º grau': 'Digite os coeficientes a (Valor 1), b (Valor 2) e c (Valor 3) da equação ax² + bx + c = 0.',
    'Logaritmo': 'Digite o logaritmando (Valor 1) e a base (Valor 2) para calcular o logaritmo.',
    'Derivada': 'Digite uma expressão matemática em termos de x (como "x**2 + 3*x") para calcular sua derivada.',
    'Integral': 'Digite uma expressão matemática em termos de x (como "x**2 + 3*x") para calcular sua integral indefinida.',
    'Gráfico de função': 'Digite uma expressão matemática em termos de x (como "sin(x)") para plotar seu gráfico.',
    'Estatística': 'Digite uma lista de valores separados por vírgula (como "1, 2, 2, 3, 4") para calcular média, mediana, moda e desvio padrão.',
    'Regra de três': 'Digite os três valores conhecidos e selecione o tipo de proporção (direta ou inversa).',
    'Conversão de temperatura': 'Digite a temperatura e selecione o tipo de conversão desejada.',
    'Números complexos': 'Digite as partes real e imaginária de dois números complexos para realizar operações entre eles.'
}

# Função para atualizar instruções e visibilidade dos campos
def atualizar_interface(change=None):
    op = menu.value
    
    # Esconder todos os campos primeiro
    entrada1.layout.display = 'none'
    entrada2.layout.display = 'none'
    entrada3.layout.display = 'none'
    tipo_box.layout.display = 'none'
    tipo_temp.layout.display = 'none'
    expr_input.layout.display = 'none'
    valores_lista.layout.display = 'none'
    complex_container.layout.display = 'none'
    
    # Atualizar instruções
    instructions.value = f"<div class='instructions'><strong>{op}:</strong> {instrucoes[op]}</div>"
    
    # Mostrar campos relevantes
    if op in ['Adição', 'Subtração', 'Multiplicação', 'Divisão', 'Potenciação', 'Radiciação']:
        entrada1.layout.display = 'block'
        entrada2.layout.display = 'block'
    elif op in ['Fatorial', 'Trigonometria']:
        entrada1.layout.display = 'block'
    elif op == 'Teorema de Pitágoras':
        entrada1.layout.display = 'block'
        entrada2.layout.display = 'block'
    elif op == 'Equação 1º grau':
        entrada1.layout.display = 'block'
        entrada2.layout.display = 'block'
    elif op == 'Equação 2º grau':
        entrada1.layout.display = 'block'
        entrada2.layout.display = 'block'
        entrada3.layout.display = 'block'
    elif op == 'Logaritmo':
        entrada1.layout.display = 'block'
        entrada2.layout.display = 'block'
    elif op in ['Derivada', 'Integral', 'Gráfico de função']:
        expr_input.layout.display = 'block'
    elif op == 'Estatística':
        valores_lista.layout.display = 'block'
    elif op == 'Regra de três':
        entrada1.layout.display = 'block'
        entrada2.layout.display = 'block'
        entrada3.layout.display = 'block'
        tipo_box.layout.display = 'block'
    elif op == 'Conversão de temperatura':
        entrada1.layout.display = 'block'
        tipo_temp.layout.display = 'block'
    elif op == 'Números complexos':
        complex_container.layout.display = 'block'

# Função de cálculo (mantida como antes)
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
                print(f'sin({a}°) = {math.sin(math.radians(a)):.4f}')
                print(f'cos({a}°) = {math.cos(math.radians(a)):.4f}')
                print(f'tan({a}°) = {math.tan(math.radians(a)):.4f}')
            elif op == 'Teorema de Pitágoras':
                print(f'Hipotenusa: {math.hypot(a, b_val):.4f}')
            elif op == 'Equação 1º grau':
                if a != 0:
                    print(f'Solução: x = {-b_val/a:.4f}')
                else:
                    print('Coeficiente "a" não pode ser zero.')
            elif op == 'Equação 2º grau':
                delta = b_val**2 - 4*a*c
                if delta < 0:
                    print('Sem raízes reais')
                elif delta == 0:
                    print(f'Raiz única: {-b_val / (2*a):.4f}')
                else:
                    x1 = (-b_val + math.sqrt(delta)) / (2*a)
                    x2 = (-b_val - math.sqrt(delta)) / (2*a)
                    print(f'Raízes: x₁ = {x1:.4f}, x₂ = {x2:.4f}')
            elif op == 'Logaritmo':
                print(f'log_{b_val}({a}) = {math.log(a, b_val):.4f}')
            elif op == 'Derivada':
                x = sp.symbols('x')
                f = sp.sympify(expr)
                derivada = sp.diff(f, x)
                print(f'Derivada de {expr}:')
                sp.pprint(derivada)
            elif op == 'Integral':
                x = sp.symbols('x')
                f = sp.sympify(expr)
                integral = sp.integrate(f, x)
                print(f'Integral de {expr}:')
                sp.pprint(integral)
            elif op == 'Gráfico de função':
                x_vals = np.linspace(-10, 10, 400)
                x = sp.symbols('x')
                f = sp.lambdify(x, sp.sympify(expr), 'numpy')
                y_vals = f(x_vals)
                plt.figure(figsize=(10, 6))
                plt.plot(x_vals, y_vals, label=f'f(x) = {expr}', color='blue')
                plt.title(f'Gráfico de f(x) = {expr}')
                plt.xlabel('x')
                plt.ylabel('f(x)')
                plt.grid(True)
                plt.legend()
                plt.show()
            elif op == 'Estatística':
                print(f'Média: {statistics.mean(lista):.4f}')
                print(f'Mediana: {statistics.median(lista):.4f}')
                try:
                    print(f'Moda: {statistics.mode(lista):.4f}')
                except:
                    print('Moda: não há moda única')
                print(f'Desvio padrão: {statistics.stdev(lista):.4f}')
            elif op == 'Regra de três':
                if tipo == "Diretamente proporcional":
                    print(f'Resultado: {(b_val * c) / a:.4f}')
                else:
                    print(f'Resultado: {(a * b_val) / c:.4f}')
            elif op == 'Conversão de temperatura':
                if temp_tipo == 'Celsius → Fahrenheit':
                    print(f'{a}°C = {a * 9/5 + 32:.2f}°F')
                else:
                    print(f'{a}°F = {(a - 32) * 5/9:.2f}°C')
            elif op == 'Números complexos':
                z1 = complex(z1_real.value, z1_imag.value)
                z2 = complex(z2_real.value, z2_imag.value)
                print(f'z₁ = {z1}')
                print(f'z₂ = {z2}')
                print(f'\nz₁ + z₂ = {z1 + z2}')
                print(f'z₁ - z₂ = {z1 - z2}')
                print(f'z₁ × z₂ = {z1 * z2}')
                if z2 != 0:
                    print(f'z₁ ÷ z₂ = {z1 / z2}')
                print(f'\nMódulo de z₁: {abs(z1):.4f}')
                print(f'Conjugado de z₁: {z1.conjugate()}')
                print(f'Forma polar de z₁: ({abs(z1):.4f}, {cmath.phase(z1):.4f} rad)')
                print(f'\nz₁² = {z1**2}')
                print(f'√z₁ = {cmath.sqrt(z1)}')
        except Exception as e:
            print(f"Erro: {str(e)}")

botao.on_click(calcular_operacao)

# Observador do menu
menu.observe(atualizar_interface, names='value')

# Organizar os widgets em seções
input_section = widgets.VBox([
    widgets.HTML(value="<div class='section-title'>Configuração do Cálculo</div>"),
    menu,
    instructions,
    widgets.HTML(value="<div class='section-title'>Parâmetros de Entrada</div>"),
    entrada1,
    entrada2,
    entrada3,
    tipo_box,
    tipo_temp,
    expr_input,
    valores_lista,
    complex_container
], layout={'margin': '10px 0'})

# Criar o layout principal
main_layout = widgets.VBox([
    widgets.HTML(value="<h1 class='calculator-title'>Calculadora Científica Avançada</h1>"),
    widgets.HTML(value="<div style='text-align:center;margin-bottom:20px;'>Selecione a função desejada e preencha os campos necessários</div>"),
    input_section,
    botao,
    widgets.HTML(value="<div class='section-title'>Resultados</div>"),
    saida
], layout={
    'width': '80%', 
    'margin': '0 auto', 
    'padding': '20px', 
    'border': '1px solid #eee', 
    'border_radius': '5px',
    'max_width': '800px'
})

# Inicializar a interface
atualizar_interface()

# Exibir a calculadora
display(main_layout)

# Tentar carregar histórico (opcional)
try:
    with open('historico_calc.json') as f:
        historico = json.load(f)
    with saida:
        print("\nHistórico de cálculos:")
        for item in historico[-5:]:  # Mostrar apenas os últimos 5 cálculos
            print(f"- {item}")
except FileNotFoundError:
    pass
except Exception as e:
    with saida:
        print(f"\nErro ao carregar histórico: {e}")
