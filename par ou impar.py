numero=int(input("Digite um número inteiro: ")) #criar uma variavel e pedir um número inteiro para poder dividi-lo por 2, usando % que vai mostrar o resto da divisão
resto = numero % 2

if resto == 0:  #se o resto for igual a 0 é par
  print("O número é par")

else:
  print("O número é impar")