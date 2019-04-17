"""
Solución del laboratorio
"""

import statistics

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


# Los ultimos 2 meses mas calientes

def promedio_tres_meses_mas_calientes(datos):
    orden = sorted(datos.values())
    return (orden[9] + orden[10] + orden[11]) / 3


promMesesSantander = promedio_tres_meses_mas_calientes(datosSantander)
print("el promedio de los tres mes mas caliente de SANTANDER fue", promMesesSantander)

promMesesNarino = promedio_tres_meses_mas_calientes(datosNarino)
print("el promedio de los tres mes mas caliente de NARIÑO fue", promMesesNarino)

promMesesGuajira = promedio_tres_meses_mas_calientes(datosGuajira)
print("el promedio de los tres mes mas caliente de GUAJIRA fue", promMesesGuajira)

ordenPromedio = sorted([promMesesSantander, promMesesNarino, promMesesGuajira])
print("el promedio mayor es", ordenPromedio[2])

"""
conglomerado = {
    33: {
        "mes": "Noviembre",
        "region": "Santander"
    },
    35: {
        "mes": "Abril",
        "region": "Guajira"
    },
    29: {
        "mes": "Diciembre",
        "region": "Nariño"
    }
}
"""

conglomerado = {
    mesCalienteSantander[1]: {
        "mes": mesCalienteSantander[0],
        "region": "Santander"
    },
    mesCalienteGuajira[1]: {
        "mes": mesCalienteGuajira[0],
        "region": "Guajira"
    },
    mesCalienteNarino[1]: {
        "mes": mesCalienteNarino[0],
        "region": "Nariño"
    }
}

tempMasCaliente = sorted(conglomerado)[2]
print("la temperatura mas caliente del año es", tempMasCaliente)

datosMasCaliente = conglomerado.get(tempMasCaliente)
print("el mes mas caliente del año es", datosMasCaliente.get("mes"))
print("la region mas caliente del año es", datosMasCaliente.get("region"))

desviacionEstandarSantander = statistics.stdev(datosSantander.values())
print("la desviasión estandar de la región de SANTANDER es", desviacionEstandarSantander)

desviacionEstandarGuajira = statistics.stdev(datosGuajira.values())
print("la desviasión estandar de la región de GUAJIRA es", desviacionEstandarGuajira)

desviacionEstandarNarino = statistics.stdev(datosNarino.values())
print("la desviasión estandar de la región de NARIÑO es", desviacionEstandarNarino)
