peso_ideal= 0  #criar uma variável de peso pra poder colocar o valor do cálculo
abaixo_peso=0

sexo=(input("Digite o sexo: ")) #pedir o sexo
altura=float(input("Digite a altura: ")) #pedir a altura

if(sexo=="Masculino"): #usar o if, se o sexo for igual a masculino então o peso ideal é a formula abaixo
  peso_ideal = (72.7 * altura) - 58
  print(f"peso ideal: \n{peso_ideal:.2f}")


elif(sexo=="Feminino"): #caso contrario se for feminino usar a formula abaixo e mostrar resultado
  peso_ideal = (62.1 * altura) - 44.7
  print(f"peso ideal: \n{peso_ideal:.2f}")
  

