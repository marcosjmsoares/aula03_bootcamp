# Integre na solução anterior um fluxo de While 
# que repita o fluxo até que o usuário insira as 
# informações corretas

while True:
    try:
        premio = 1000
        nome = str(input("Digite o seu nome:"))

        salario = float(input("Digite o valor de salário:"))

        bonus = float(input("Digite a porcentagem do bônus:"))
        bonus_calculado = (salario / 100) * bonus
        calculo = salario + bonus_calculado + premio

        print("Olá " + nome + ", o seu bônus foi de " + str(calculo)) 
        break
    except:
        print("Valor informados errado. Tente novamente!")
 #fim

#  while True:
#     try:
#         valor1=int(input("Insira um numero: "))
#         valor2=int(input("Insira outro numero: "))
#         operador = input("Digite o operador (+, -, *, /): ")
#         if operador == '+':
#             resultado = valor1 + valor2
#         elif operador == '-':
#             resultado = valor1 - valor2
#         elif operador == '*':
#             resultado = valor1*valor2
#         elif operador == '/' and valor2 != 0:
#             resultado = valor1/valor2
#         else:
#             print("Operador invalido ou divisor por zero.")
#         print(f"Resultado: {resultado}")
#         break
#     except:
#         print("Valor informados errado. Tente novamente!")