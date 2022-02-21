print("Informe a quantidade de elétrons")
layer_value = int(input(">> "))
if(layer_value > 0):
    layer_letter = "K"
    layer_number = 1
elif(layer_value > 4 and layer_value <= 12):
    layer_letter = "L"
    layer_number = 2
elif(layer_value > 12 and layer_value <= 20):
    layer_letter = "M"
    layer_number = 3
elif(layer_value > 20 and layer_value <= 38):
    layer_letter = "N"
    layer_number = 4
elif(layer_value > 38 and layer_value <= 56):
    layer_letter = "O"
    layer_number = 5
elif(layer_value > 56 and layer_value <= 88):
    layer_letter = "P"
    layer_number = 6
elif(layer_value > 88):
    layer_letter = "Q"
    layer_number = 7
print(f"Camada {layer_number}, correspondente a letra {layer_letter}")
