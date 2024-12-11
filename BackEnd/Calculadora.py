while True:
  num1 = input("Digite o primeiro número: ")
  num2 = input("Digite outro número: ")
  operador = input("Digite a operação que deseja fazer (+, -, *, /): ")

  try:
    float_num1 = float(num1)
    float_num2 = float(num2)
    break
  except:
    print("Um ou todos os números digitados não são aceitos")
    continue

while True:
    if operador in ['+', '-', '*', '/']:
        break  # Exit the loop if the operator is valid
    else:
        print("Digite um operador válido (+, -, *, /).")
        operador = input("Digite a operação que deseja fazer (+, -, *, /): ")

print("Efetuando o cálculo. Aguarde ")
if operador == '+':
  print(f"{float_num1} + {float_num2} =", float_num1+float_num2)
if operador == '-':
  print(f"{float_num1} - {float_num2} =", float_num1-float_num2)
if operador == '*':
  print(f"{float_num1} * {float_num2} =", float_num1*float_num2)
if operador == '/':
  print(f"{float_num1} / {float_num2} =", float_num1/float_num2)
