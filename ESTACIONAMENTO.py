print("**SISTEMA DE ESTACIONAMENTO**")

# Colocar números inteiros ao invés de horas!! Por exemplo, se a hora for '12:30', colocar '12,50'!!

print("\n")

print("1 - CARRO - R$ 7,00/HORA")
print("2 - MOTO - 5 REAIS/HORA")
print("3 - CAMINHÃO - 9 REAIS/HORA")
print("\n")
n = 0
while n == 0:
  auto = int(input("DIGITE O NÚMERO DO TIPO DE VEÍCULO: "))
  if(auto == 1):
    print("CARRO")
    print("\n")
    placa = input("PLACA: ")
    modelo = input("MODELO: ")
    data = input("DATA: ")
    entrada = float(input("ENTRADA: "))
    saida = float(input("SAÍDA: "))
    print("\n")
    print('PLACA: ', placa)
    print("MODELO: ", modelo)
    print('DATA: ', data)
    print("ENTRADA: ", entrada)
    print("SAÍDA: ", saida)
    preco = (saida - entrada)*7
    print("\n")
    print("TOTAL A PAGAR: ", preco, "REAIS")
    
  elif(auto == 2):
    print("MOTO")
    print("\n")
    placa = input("PLACA: ")
    modelo = input("MODELO: ")
    data = input("DATA: ")
    entrada = float(input("ENTRADA: "))
    saida = float(input("SAÍDA: "))
    print("\n")
    print('PLACA: ', placa)
    print("MODELO: ", modelo)
    print('DATA: ', data)
    print("ENTRADA: ", entrada)
    print("SAÍDA: ", saida)
    preco = (saida - entrada)*5
    print("\n")
    print("TOTAL A PAGAR: ", preco, "REAIS")
  elif(auto == 3):
    print("CAMINHÃO")
    print("\n")
    placa = input("PLACA: ")
    modelo = input("MODELO: ")
    data = input("DATA: ")
    entrada = float(input("ENTRADA: "))
    saida = float(input("SAÍDA: "))
    print("\n")
    print('PLACA: ', placa)
    print("MODELO: ", modelo)
    print('DATA: ', data)
    print("ENTRADA: ", entrada)
    print("SAÍDA: ", saida)
    preco = (saida - entrada)*9
    print("\n")
    print("TOTAL A PAGAR: ", preco, "REAIS")
  else:
    print("Ops! Opção incorreta!! Tente novamente!")
    print("\n")