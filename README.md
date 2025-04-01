![Status](https://img.shields.io/badge/status-active-brightgreen)
![Licença](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.12-blue)

# Calculadora em Python

Este é um projeto educacional desenvolvido em Python, que consiste em uma calculadora capaz de realizar operações matemáticas variadas, incluindo adição, subtração, multiplicação, divisão, potenciação, radiciação, fatorial, além do cálculo do teorema de Pitágoras. Também abrange o estudo de funções e equações do 1º e 2º grau, permitindo a construção de gráficos e a determinação das coordenadas dos vértices. As funcionalidades incluem ainda cálculos trigonométricos (seno, cosseno e tangente), logaritmos naturais e de bases diversas, bem como integrais definidas e derivadas, regra de três simnples inversamente proporcional ou diretamente propocional. O projeto é flexível e pode ser expandido com novos recursos.

## Sobre o Projeto

Este projeto foi desenvolvido como uma calculadora multifuncional em Python, com o objetivo de auxiliar estudantes e entusiastas de matemática a realizar cálculos básicos e avançados de forma simples e intuitiva. Além das operações matemáticas tradicionais, a calculadora também inclui funcionalidades como gráficos de funções, resolução de equações e cálculos trigonométricos.

O projeto foi criado para fins educacionais, com o intuito de demonstrar a aplicação de conceitos de programação em Python, como funções, manipulação de bibliotecas (como `math` , `matplotlib`, `numpy`, `scipy` e `sympy`) e estruturas de controle.

## Contribuição

Contribuições são sempre bem-vindas! Se você quiser contribuir para este projeto, siga os passos abaixo:

1. Faça um **fork** do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`).
4. Faça um push para a branch (`git push origin feature/nova-feature`).
5. Abra um **Pull Request**.

Se você encontrar algum bug ou tiver uma sugestão, abra uma [issue](https://github.com/LeoMedeiros72/Calculadora-3.0/issues) no repositório.

## Funcionalidades

- **Adição**: Soma dois números.
- **Subtração**: Subtrai o segundo número do primeiro.
- **Multiplicação**: Multiplica dois números.
- **Divisão**: Divide o primeiro número pelo segundo (com tratamento de divisão por zero).
- **Potenciação**: Calcula a potência de um número elevado a outro.
- **Radiciação**: Calcula a raiz de acordo com o número escolhido como base e o número escolhido como índice.
- **Fatorial**: Calcula o fatorial de um número.
- **Logaritmo**: Calcula o logaritmo natural ou logaritmo de base específica.
- **Teorema de Pitágoras**: Calcula o valor de cateto ou hipotenusa a partir de dois valores digitados.
- **Equação do primeiro grau**: Calcula o valor de X na equação do primeiro grau.
- **Equação do segundo grau**: Calcula o valor das raízes, discriminante (delta) e vértices da parábola.
- **Trigonometria**: Calcula o valor do seno, cosseno e tangente do ângulo digitado.
- **Função do primeiro grau**: Faz o gráfico da função mostrando os pontos de interseção tanto no eixo X quanto no Y.
- **Função do segundo grau**: Faz o gráfico da função mostrando a parábola, o vértice e os pontos de interseção dos eixos X e Y (se existir).
- **Integral Definida**: Calcula o valor da Integral a partir da função escrita e dos limites superior e inferior.
- **Derivada**: Calcula o valor da derivada a partir da função escrita e do ponto de derivada.
- **Estatística**: Calcula média, mediana, moda, variância e desvio padrão de uma lista de números separados por vírgula.
- **Regra de Três**: A partir de 3 números digitados faz o cálculo do quarto número, podendo ser diretamente propocional ou inversamente propocional.
  
## Como Usar

### Para executar a calculadora, use o seguinte comando:

   ```bash
   python calculadora.py
```

###   Após isso selecione o número que está relacionado a operação que deseja efetuar:

**1. Operações Básicas (Adição, Subtração, Multiplicação, Divisão)**

**2. Potenciação**

**3. Radiciação**

**4. Fatorial**

**5. Teorema de Pitágoras**

**6. Equações do 1º e 2º grau**

**7. Trigonometria (Seno, Cosseno, Tangente)**

**8. Logaritmos**

**9. Derivada de uma Função**

**10. Integral de uma Função**

**11. Gráfico de Função**

**12. Cálculo Estatístico (Média, Mediana, Moda, Variância, Desvio Padrão)**

**13. Regra de Três (Diretamente ou Inversamente Proporcional)**

###   Para sair da calculadora digite o núemro abaixo:   

**14. Sair**

![image](https://github.com/user-attachments/assets/c4cbe31e-97ea-449f-bdb4-9a47afa8b1b1)

       
## 🚀 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/LeoMedeiros72/Calculadora-3.0.git
   cd Calculadora-3.0

## Tecnologias Utilizadas

- **Python 3.12**: Linguagem de programação principal.
- **Biblioteca Math**: Para cálculos matemáticos avançados.
- **Matplotlib**: Para geração de gráficos.
- **NumPy**: Para manipulação de arrays e cálculos numéricos.
- **Biblioteca quad do pacote cipy.integrate**: Para cálculo de integrais
- **Biblioteca findiff**: Para cálculo de derivadas
- **Biblioteca statistics**: Para cálculos estatísticos

## 📌 Exemplos de uso

### Adição
#### Entrada
Digite o primeiro número: 5

Digite o segundo número: 3
#### Saída
Resultado: 8

![image](https://github.com/user-attachments/assets/8457317d-a201-43f6-a6d2-095a1119d794)

### Fatorial
#### Entrada
Digite o número para calcular o fatorial: 5
#### Saída
Resultado: 120

![image](https://github.com/user-attachments/assets/bf730e36-12da-4eda-8a67-14bf7ddf392f)

### Equação do segundo grau
#### Entrada
Digite o valor de A: 1
Digite o valor de B: -3
Digite o valor de C: 2
#### Saída
Discriminante (Delta): 1.0
A função possui duas raízes reais diferentes: x1 = 2.00 e x2 = 1.00
O vértice da parábola é: (1.50, -0.25)

![image](https://github.com/user-attachments/assets/6c9cb919-7113-4076-a4e5-c78a24839752)

## Roadmap

- [x] Adicionar operações básicas (adição, subtração, multiplicação, divisão).
- [x] Implementar gráficos de funções do primeiro e segundo grau.
- [ ] Adicionar suporte para números complexos.
- [ ] Implementar uma interface gráfica (GUI) usando Tkinter.
- [x] Adicionar suporte para cálculos de derivadas e integrais.

## 📂 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor

- **Leonardo Medeiros**
  - GitHub: [LeoMedeiros72](https://github.com/LeoMedeiros72)
  - LinkedIn: [Leonardo Medeiros](https://www.linkedin.com/in/leonardo-medeiros-43556b211/)
  - E-mail: xorao.lsm@gmail.com
