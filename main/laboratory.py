"""
Solución del laboratorio
"""

datosSantander = {
    "Enero": 22,
    "Febrero": 27,
    "Marzo": 21,
    "Abril": 24,
    "Mayo": 32,
    "Junio": 33,
    "Julio": 30,
    "Agosto": 29,
    "Septiembre": 24,
    "Octubre": 26,
    "Noviembre": 33,
    "Diciembre": 32
}

datosGuajira = {
    "Enero": 28,
    "Febrero": 30,
    "Marzo": 31,
    "Abril": 35,
    "Mayo": 30,
    "Junio": 28,
    "Julio": 26,
    "Agosto": 26,
    "Septiembre": 28,
    "Octubre": 30,
    "Noviembre": 32,
    "Diciembre": 34
}

datosNarino = {
    "Enero": 24,
    "Febrero": 22,
    "Marzo": 19,
    "Abril": 15,
    "Mayo": 20,
    "Junio": 22,
    "Julio": 25,
    "Agosto": 22,
    "Septiembre": 23,
    "Octubre": 24,
    "Noviembre": 28,
    "Diciembre": 29
}


def promedio_temperaturas(datos):
    suma_temp = 0
    for dato in datos.values():
        suma_temp = suma_temp + dato

    return suma_temp / 12


promedioSantander = promedio_temperaturas(datosSantander)

print("el promedio de temperaturas de SANTANDER fue", promedioSantander)

promedioGuajira = promedio_temperaturas(datosGuajira)

print("el promedio de temperaturas de LA GUAJIRA fue", promedioGuajira)

promedioNarino = promedio_temperaturas(datosNarino)

print("el promedio de temperaturas de NARIÑO fue", promedioNarino)

promedioNacional = (promedioSantander + promedioNarino + promedioGuajira) / 3
print("El promedio nacional fue", promedioNacional)


def mes_mas_caliente(datos):
    temp = 0
    mes = ""

    for key, value in datos.items():
        if value > temp:
            temp = value
            mes = key

    return mes, temp


mesCalienteSantander = mes_mas_caliente(datosSantander)
print("el mes mas caliente de SANTANDER fue", mesCalienteSantander[0], "con", mesCalienteSantander[1], "grados")

mesCalienteGuajira = mes_mas_caliente(datosGuajira)
print("el mes mas caliente de LA GUAJIRA fue", mesCalienteGuajira[0], "con", mesCalienteGuajira[1], "grados")

mesCalienteNarino = mes_mas_caliente(datosNarino)
print("el mes mas caliente de NARIÑO fue", mesCalienteNarino[0], "con", mesCalienteNarino[1], "grados")
