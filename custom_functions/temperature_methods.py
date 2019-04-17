def promedio_temperaturas(datos):
    suma_temp = 0
    for dato in datos.values():
        suma_temp = suma_temp + dato

    return suma_temp / 12


def mes_mas_caliente(datos):
    temp = 0
    mes = ""

    for key, value in datos.items():
        if value > temp:
            temp = value
            mes = key

    return mes, temp


# Los ultimos 2 meses mas calientes
def promedio_tres_meses_mas_calientes(datos):
    orden = sorted(datos.values())
    return (orden[9] + orden[10] + orden[11]) / 3
