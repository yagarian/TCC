tabela = {
    "H": [1],
    "He": [ 2],
    "Li": [ 3 ],
    "Be": [4 ],
    "B": [5],
    "C": [ 6 ],
    "N": [ 7 ],
    "O": [ 8 ],
    "F": [ 9 ],
    "Ne": [ 10 ],
    "Na": [ 11 ],
    "Mg": [ 12 ],
    "Al": [ 13 ],
    "Si": [ 14 ],
    "P": [ 15 ],
    "S": [ 16 ],
    "Cl": [ 17 ],
    "Ar": [ 18 ],
    "Po": [ 19 ],
    "Ca": [ 20 ],
    "Sc": [ 21 ],
    "Ti": [ 22 ],
    "V": [ 23 ],
    "Cr": [ 24 ],
    "Mn": [ 25 ],
    "Fe": [ 26 ],
    "Co": [ 27 ],
    "Ni": [ 28 ],
    "Cu": [ 29 ],
    "Zn": [ 30 ],
    "Ga": [ 31 ],
    "Ge": [ 32 ],
    "As": [ 33 ],
    "Se": [ 34 ],
    "Br": [ 35 ],
    "Kr": [ 36 ],
    "Rb": [ 37 ],
    "Sr": [ 38 ],
    "Y": [ 39 ],
    "Zr": [ 40 ],
    "Nb": [ 41 ],
    "Mo": [ 42 ],
    "Tc": [ 43 ],
    "Ru": [ 44 ],
    "Rh": [ 45 ],
    "Pd": [ 46 ],
    "Ag": [ 47 ],
    "Cd": [ 48 ],
    "In": [ 49 ],
    "Sn": [ 50 ],
    "Sb": [ 51 ],
    "Te": [ 52 ],
    "I": [ 53 ],
    "Xe": [ 54 ],
    "Cs": [ 55 ],
    "Ba": [ 56 ],
    "La": [ 57 ],
    "Ce": [ 58 ],
    "Pr": [ 59 ],
    "Nd": [ 60 ],
    "Pm": [ 61 ],
    "Sm": [ 62 ],
    "Eu": [ 63 ],
    "Gd": [ 64 ],
    "Tb": [ 65 ],
    "Dy": [ 66 ],
    "Ho": [ 67 ],
    "Er": [ 68 ],
    "Tm": [ 69 ],
    "Yb": [ 70 ],
    "Lu": [ 71 ],
    "Hf": [ 72 ],
    "Ta": [ 73 ],
    "W": [ 74 ],
    "R": [ 75 ],
    "Os": [ 76 ],
    "Ir": [ 77 ],
    "Pt": [ 78 ],
    "Au": [ 79 ],
    "Hg": [ 80 ],
    "Tl": [ 81 ],
    "Pb": [ 82 ],
    "Bi": [ 83 ],
    "Po": [ 84 ],
    "At": [ 85 ],
    "Rn": [ 86 ],
    "Fr": [ 87 ],
    "Ra": [ 88 ],
    "Ac": [ 89 ],
    "Th": [ 90 ],
    "Pa": [ 91 ],
    "U": [ 92 ],
    "Np": [ 93 ],
    "Pu": [ 94 ],
    "Am": [ 95 ],
    "Cm": [ 96 ],
    "Bk": [ 97 ],
    "Cf": [ 98 ],
    "Es": [ 99 ],
    "Fm": [ 100 ],
    "Md": [ 101 ],
    "No": [ 102 ],
    "Lr": [ 103 ],
    "Rf": [ 104 ],
    "Db": [ 105 ],
    "Sg": [ 106 ],
    "Bh": [ 107 ],
    "Hs": [ 108 ],
    "Mt": [ 109 ],
    "Ds": [ 110 ],
    "Rg": [ 111 ],
    "Cn": [ 112 ],
    "Nh": [ 113 ],
    "Fl": [ 114 ],
    "Mc": [ 115 ],
    "Lv": [ 116 ],
    "Ts": [ 117 ],
    "Og": [ 118 ],
}
 
def layer(layer_value):
 global layer_letter
 global layer_number
 if(layer_value <= 2):
     layer_letter = "K"
     layer_number = 1
 elif(layer_value > 2 and layer_value <= 8):
     layer_letter = "L"
     layer_number = 2
 elif(layer_value > 8 and layer_value <= 18):
     layer_letter = "M"
     layer_number = 3
 elif(layer_value > 18 and layer_value <= 32):
     layer_letter = "N"
     layer_number = 4
 elif(layer_value > 32 and layer_value <= 64):
     layer_letter = "O"
     layer_number = 5
 elif(layer_value > 64 and layer_value < 72):
     layer_letter = "P"
     layer_number = 6
 elif(layer_value > 72 and layer_value < 80):
     layer_letter = "Q"
     layer_number = 7
 print(f"Camada {layer_number}, correspondente a letra {layer_letter}")

def sublayer(number):
    if number <= 2:
        config = f"1s{number}"
    elif number > 2 and number <=4:
        rest = 2-(number - 2) 
        config = f"1s2, 2s{rest}"
    elif number > 4 and number <=12:
         prob = number - 4
         rest1 = (number - 4)
         if rest1 < 0:
            rest1 = 0
         if rest1 > 6:
             rest1 = 6
         rest2 = (prob - rest1)
         config = f"1s2, 2s2, 2p{rest1}, 3s{rest2} "
    elif number > 12 and number <=20:
         prob = number - 12
         rest1 = (number - 12)-2
         if rest1 < 0:
            rest1 = 0
         if rest1 > 6:
             rest1 = 6
         rest2 = (prob - rest1)
         config = f"1s2, 2s2, 2p6, 3s2, 3p{rest1}, 4s{rest2} "
    elif number > 20 and number <=38:
         prob = number - 20
         rest1 = (number - 20)
         if rest1 < 0:
            rest1 = 0
         if rest1 > 10:
             rest1 = 10
         rest2 = (prob - rest1)
         if rest2 < 0:
            rest2 = 0
         if rest2 > 6:
             rest1 = 6
         rest3 = (prob - rest1)- rest2
         config = f"1s2, 2s2, 2p6, 3s2, 3p6, 4s2, 3d{rest1}, 4p{rest2}, 5s{rest3} "
    elif number > 38 and number <=56:
         prob = number - 38
         rest1 = (number - 38)
         if rest1 < 0:
            rest1 = 0
         if rest1 > 10:
             rest1 = 10
         rest2 = (prob - rest1)
         if rest2 < 0:
            rest2 = 0
         if rest2 > 6:
             rest1 = 6
         rest3 = ((prob - rest1)- rest2)
         config = f"1s2, 2s2, 2p6, 3s2, 3p6, 4s2, 3d10, 4p6, 5s2, 4d{rest1}, 5p{rest2}, 6s{rest3} "
    elif number > 56 and number <=88:
         prob = number - 56
         rest0 = (number - 56) 
         if rest0 < 0:
            rest0 = 0
         if rest0 > 14:
            rest0 = 14
         rest1 = (number - 56) 
         if rest1 < 0:
            rest1 = 0
         if rest1 > 10:
            rest1 = 10
         rest2 = (prob - rest1)
         if rest2 < 0:
            rest2 = 0
         if rest2 > 6:
            rest1 = 6
         rest3 = ((prob - rest1 - rest0)- rest2)
         config = f"1s2, 2s2, 2p6, 3s2, 3p6, 4s2, 3d10, 4p6, 5s2, 4d10, 5p6, 6s2, 4f{rest0}, 5d{rest1}, 6p{rest2}, 7s{rest3} "
    elif number > 88 and number <=118:
         prob = number - 88
         rest1 = (number - 88) 
         if rest1 < 0:
            rest1 = 0
         if rest1 > 14:
            rest1 = 14
         rest2 = (number - 88) 
         if rest2 < 0:
            rest2 = 0
         if rest1 > 10:
            rest1 = 10
         rest3 = (prob - rest1)
         if rest3 < 0:
            rest3 = 0
         if rest3 > 6:
            rest3 = 6
         config = f"1s2, 2s2, 2p6, 3s2, 3p6, 4s2, 3d10, 4p6, 5s2, 4d10, 5p6, 6s2, 4f14, 5d10, 6p6, 7s2, 4f{rest1}, 6d{rest2}, 7p{rest3} "

    print(f"A distribuição ocorreu da forma: \n {config}")
    
