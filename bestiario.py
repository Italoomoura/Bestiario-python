monstros = {}

def addMonstro(): 
  qtd = int(input("\nQuantidade de Monstros: "))
  i = 1
  while i <= qtd:
    nome = input("\nNome do monstro: ")
    vida = int(input("Vida do monstro: "))
    monstros[nome] = vida
    i += 1

while True:
  print("\n1. Todos Monstros \n2. Adicionar Monstros \n3. Selecionar Monstro\n")
  x = int(input("Digite o número: "))
  if x == 1:
    print("\n",monstros.keys())
  elif x == 2:
    addMonstro()
  elif x == 3:
    print("\nQual monstro deseja ver?")
    varM = input("Nome do Monstro: ")
    print("Esse Monstro tem",monstros[varM],"de vida")
  else:
    print("Opção Inválida!")
