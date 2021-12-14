import archive
elements = archive.tabela
layerf = archive.layer
sublayer = archive.sublayer
option_menu = 5

while option_menu > 0:
 print('''
  _______________MENU_______________
 | [1] - Pesquisar Elemento         |
 | [2] - Distribuição em níveis     |
 | [3] - Distribuição em subníveis  |
 | [0] - Sair                       |
 |__________________________________|
 ''')
 
 option_menu = int(input("Escolha: >>"))
 if(option_menu == 1):
     search_element = str(input("Informe a sigla do elemento: >>"))
     if search_element.isalpha():
         if search_element in elements:
             for key, value in elements.items():
                 if search_element == key:
                     note = value
                     print(f"O elemento {key} possui {note} elétrons na eletrosfera;")
                     print("Deseja continuar? \n 0 - Não \n 1 - Sim")
                     response = int(input(">>"))
                     if (response == 1):
                         option_menu = response
                     else:
                         option_menu = 0
         else:
             print("Não localizado")  
     else:
         print("Formatação inapropriada.")
 elif(option_menu == 2):
     print("Informe a quantidade de elétrons")
     layer_value = int(input(">> "))
     layerf(layer_value)
     print("Deseja continuar? \n 0 - Não \n 1 - Sim")
     response = int(input(">>"))
     if (response == 1):
         option_menu = response
     else:
         option_menu = 0
 elif(option_menu == 3):
     print("Informe a quantidade de elétrons")
     sublayer_value = int(input(">> "))
     sublayer(sublayer_value)
     print("Deseja continuar? \n 0 - Não \n 1 - Sim")
     response = int(input(">>"))
     if (response == 1):
         option_menu = response
     else:
         option_menu = 0
 elif(option_menu == 0):
     break
 else:
     print("Opção invalida")
     


      
