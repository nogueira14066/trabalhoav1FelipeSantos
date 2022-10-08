notas_100, notas_50, notas_20, notas_10, notas_5, notas_1 = 0, 0, 0, 0, 0, 0  #criar as váriaveis para receber e fazer os cálculos

saque=int(input("Digite o valor, mínimo 10 e máximo 600: ")) #criar função input para o usuário entrar com um valor "INTEIRO"

if saque<10 or saque>600:   #USEI A FUNÇÃO IF, para caso o usuário colocar um valor abaixo de 10 ou maior que 600, mostrar valor inválido
  print("Valor inválido - Valor mínimo 10 e valor máximo 600")

notas_100, saque= divmod(saque, 100)   #usar esse cálculo "%" para mostrar o resto do saque com a nota disponível, div é a cédula e o mod é o resto das notas, que entrarão nas contas abaixo....

notas_50, saque= divmod(saque, 50)

notas_20, saque= divmod(saque, 20)

notas_10, saque= divmod(saque, 10)

notas_5, saque= divmod(saque, 5)

notas_1, saque= divmod(saque, 1)

if notas_100>0:         #se as notas de 100 forem maior que 0, printar o número de notas, que foram cálculdadas acima no divmod
  print(f"{notas_100} nota(s) de 100")

if notas_50>0:
  print(f"{notas_50} nota(s) de 50")

if notas_20>0:
  print(f"{notas_20} nota(s) de 20")

if notas_10>0:
  print(f"{notas_10} nota(s) de 10")

if notas_5>0:
  print(f"{notas_5} nota(s) de 5")

if notas_1>0:
  print(f"{notas_1} nota(s) de 1")


  #para a opção B, a única forma que encontrei foi excluir a nota de 20