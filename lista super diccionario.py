dic1 = { "fruta":[], "limpieza": [ ], "abarrotes": [ ]}

def pedirdatos(instruccion: str) -> str:
    articulo = input (instruccion)
    return articulo

def llenar_lista_fruta() -> list:
    for i in range (3):
        dic1["fruta"].append(pedirdatos("Ingrese fruta:\n"))
    return dic1["fruta"]

def llenar_lista_limpieza() -> list:
    for j in range (3):
        dic1["limpieza"].append(pedirdatos("Ingrese articulo de limpieza:\n"))
    return dic1["limpieza"]

def llenar_lista_abarrotes() -> list:
    for k in range (3):
        dic1["abarrotes"].append(pedirdatos("Ingrese abarrotes:\n"))
    return dic1["abarrotes"]


llenar_lista_abarrotes()
llenar_lista_limpieza()
llenar_lista_fruta()    

print("Los abarrotes son:\n ", dic1["abarrotes"])
print("Los articulos de limpieza son:\n ", dic1["limpieza"])
print("Las frutas son:\n ", dic1["fruta"])
