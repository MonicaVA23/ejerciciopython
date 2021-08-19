
dic1 = {"creditos":
    {
        "credito_p":{
            "pago_requerido":1050, 
            "monto_credito":10000,
            "tiempo_a_pagar_credito":30
        }, 
        "credito_m":{
            "pago_requerido":2000, 
            "monto_credito":20000,
            "tiempo_a_pagar_credito":60
        },
        "credito_g":{
            "pago_requerido":3000, 
            "monto_credito":30000,
            "tiempo_a_pagar_credito":90
        }
    }
}
#print( type(dic1))
lista_nombre=[]

def datos() -> list:
    print("Ingresa nombre, salario y gastos: ")
    for i in range (3):
        lista_nombre.append(input())
    print(lista_nombre)
    return lista_nombre
    
def buscar_creditos() -> list:
    ofertas=[]
    for i in dic1["creditos"]:
        #print (dic1["creditos"][i])
        if (int(lista_nombre[1])-int(lista_nombre[2])>dic1["creditos"][i]["pago_requerido"]):
            ofertas.append(i)
        else:
            ofertas.append("No cumples "+i)
    return ofertas   




datos()  
buscar_creditos()

