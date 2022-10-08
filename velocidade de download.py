tempo_download=0  #variavel para fazer o cálculo após tamanho e velocidade de internet serem informados

tamanho_arquivo=float(input("Digite o tamanho do arquivo em MB: ")) # float é melhor do que int nesse caso
velocidade_internet=float(input("Digite a velocidade da internet em Mbps: "))


tempo_download =(tamanho_arquivo * 8 / velocidade_internet) / 60 #cálculo

print ("O tempo de download é de %.2f minutos" %tempo_download) #resposta... O %2.f é para formatar o resultado em duas casas decimais apenas, e é necessário colocar % no lugar da virgula...