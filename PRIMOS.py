
def pedirdatos():
    try:
        datos = int (input ("Ingrese numero: "))
        return datos
    except:
        print("Ingrese un valor numerico")

def proceso(datos):
    if (datos % 2 ==0):
        print ("No es primo")
    else:   
        print ("si es primo")     

 
proceso(pedirdatos())





