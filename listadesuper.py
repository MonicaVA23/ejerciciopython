listasuper=[ ]

def pedirdatos(instruccion: str) -> str:
    elemento = input (instruccion)
    return elemento

def llenar_lista() -> list:
    for i in range (5):
        listasuper.append(pedirdatos("Ingrese articulo a la lista:\n"))
    return listasuper 

def funcion_pop():
    print("El articulo removido en el indice 3 es:", listasuper.pop(3))
   # return listasuper

def funcion_remove():
    try:
        instruccion_enviar = "Elimine articulo de la lista:"
        for i in range (2):
            listasuper.remove(pedirdatos(instruccion_enviar))
    except:
        print("Ese articulo no esta en la lista")        


llenar_lista()
print(listasuper)           
#funcion_pop()
funcion_remove()
print(listasuper)
   