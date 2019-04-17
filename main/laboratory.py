"""
Solución del laboratorio
"""

import statistics
from LaboratorioColecciones.custom_functions.temperature_methods import *

# Datos de entrada
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

# ========= Solución a =========
promedioSantander = promedio_temperaturas(datosSantander)
print("el promedio de temperaturas de SANTANDER fue", promedioSantander)

promedioGuajira = promedio_temperaturas(datosGuajira)
print("el promedio de temperaturas de LA GUAJIRA fue", promedioGuajira)

promedioNarino = promedio_temperaturas(datosNarino)
print("el promedio de temperaturas de NARIÑO fue", promedioNarino)


# ========= Solución b =========
promedioNacional = (promedioSantander + promedioNarino + promedioGuajira) / 3
print("El promedio nacional fue", promedioNacional)


# ========= Solución c =========
mesCalienteSantander = mes_mas_caliente(datosSantander)
print("el mes mas caliente de SANTANDER fue", mesCalienteSantander[0], "con", mesCalienteSantander[1], "grados")

mesCalienteGuajira = mes_mas_caliente(datosGuajira)
print("el mes mas caliente de LA GUAJIRA fue", mesCalienteGuajira[0], "con", mesCalienteGuajira[1], "grados")

mesCalienteNarino = mes_mas_caliente(datosNarino)
print("el mes mas caliente de NARIÑO fue", mesCalienteNarino[0], "con", mesCalienteNarino[1], "grados")


# ========= Solución d =========
promMesesSantander = promedio_tres_meses_mas_calientes(datosSantander)
print("el promedio de los tres mes mas caliente de SANTANDER fue", promMesesSantander)

promMesesNarino = promedio_tres_meses_mas_calientes(datosNarino)
print("el promedio de los tres mes mas caliente de NARIÑO fue", promMesesNarino)

promMesesGuajira = promedio_tres_meses_mas_calientes(datosGuajira)
print("el promedio de los tres mes mas caliente de GUAJIRA fue", promMesesGuajira)


# ========= Solución e =========
ordenPromedio = sorted([promMesesSantander, promMesesNarino, promMesesGuajira])
print("el promedio mayor es", ordenPromedio[2])


# ========= Solución f =========
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


# ========= Solución g =========
desviacionEstandarSantander = statistics.stdev(datosSantander.values())
print("la desviasión estandar de la región de SANTANDER es", desviacionEstandarSantander)

desviacionEstandarGuajira = statistics.stdev(datosGuajira.values())
print("la desviasión estandar de la región de GUAJIRA es", desviacionEstandarGuajira)

desviacionEstandarNarino = statistics.stdev(datosNarino.values())
print("la desviasión estandar de la región de NARIÑO es", desviacionEstandarNarino)
