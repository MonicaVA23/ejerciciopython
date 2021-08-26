
dicci1 = { "excepciones":[2, 4],
            "tabla": int,
            "resultado": [ ]
            }
lista1 = [2, 4]

def pedir_datos() -> int:
    try:
        datos= int (input("Ingrese el numero de la tabla de multiplicar que desea\n"))
        return datos
    except: 
        print("Dato erroneo")

def tabla() -> list:
    tablafinal = []
    for i in range (1, 11):
        resultado = i * datos
        print(resultado)
        if i not in (lista1):
            tablafinal.append( str(i) + "x" + str (datos) + "=" +str (resultado))   
    
    return tablafinal

    
            

datos=pedir_datos()
print (tabla())
for i in  tabla():
    print (i)






