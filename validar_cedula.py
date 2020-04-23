import sys 

cedula = input("Por favor introducir la cedula a validar: ") 
lcedula = list(cedula)
formato = ["*", "-","*", "*","*", "-","*", "*","*", "*" ]

for c, i in enumerate(lcedula):

    if i in {"0","1","2","3","4","5","6","7","8","9"} :
        lcedula[c] = "*"

if lcedula == formato:
    print("Es una cedula VALIDA.")
else:
     print("Es una cedula INVALIDA.")

print(lcedula) 