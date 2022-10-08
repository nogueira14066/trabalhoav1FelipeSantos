idade=0      #criar as variaveis
ano_atual=2022  #ano atual para cálculo
abono=0


ano_nascimento=int(input("Digite o ano de nascimento: "))   #input para pedir ano, sexo e salário
sexo=str(input("Digite o sexo: "))
salario_bruto=float(input("Digite o seu salário bruto: "))

idade = ano_atual - ano_nascimento   #cálculo da idade
print(f"Sua idade é: {idade}")  #format e print da idade

salario_bruto = salario_bruto + abono  #cálculo sálario bruto


if idade>=40:    #usar a condição if e else para dizer o abono de acordo com a idade
   abono=15/100 * salario_bruto
else:
  idade<40
  abono=25/100 * salario_bruto
  
print(f"Seu salário bruto é: {salario_bruto}") #printar salario bruto sem abono
print(f"Seu abono é: {abono}" ) #mostrar abono
print(f"Seu salário bruto acrescido do abono é: {salario_bruto + abono}") #salario bruto acrescido do abono


