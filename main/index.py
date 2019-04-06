"""
Este sería el código que tendríamos que ejecutar muchas veces para probar cada
función.

Las pruebas unitarias sirven para no tener que hacer manualmente el trabajo

Para el siguiente ejemplo voy a realizar un algoritmo que use las funciones de calcular
la nota definitiva de un estudiante dadas N notas, pero quitando la peor de las notas
e indicando cuál fue la mejor nota

"""

from custom_functions import student_grades_methods

quantity = int(input("How many grades do you have: "))
print("Ok, lets read ", quantity, " grades")

# Lista vacía donde se agregarán las notas
grade_list = []

for i in range(0, quantity):
    # Creo un mensaje al que le agrego el valor de i+1 para que el usuario sepa que nota está digitando
    # El valor de i+1 se ubica en donde está {} en el texto
    grade = int(input("Please give me the {} grade ".format(i+1)))

    # Agrego la nota digitada a la lista
    grade_list.append(grade)

# Una vez finalizado el ciclo ya habré leído todas las notas, las cuales puedo imprimir

print("Your grades: ", grade_list)

# Ahora puedo usar las funciones creadas
final_grade = student_grades_methods.calculate_final_grade(grade_list)
best_grade = student_grades_methods.calculate_best_grade(grade_list)

print("Final grade: ", final_grade)
print("Your best grade was: ", best_grade )

# Ahora calculo la nota sin la peor nota
# Primero obtengo una lista sin la peor nota
new_grade_list = student_grades_methods.remove_worst_grade(grade_list)

# Ahora que tengo la nueva lista, pued usar la función que sirve para calcular la nota final
# pero utilizando la nueva lista de notas (sin la peor nota)
new_final_grade = student_grades_methods.calculate_final_grade(new_grade_list)
print("Your final grade (without your worst grade): ", new_final_grade)

# Sin utilizar pruebas unitarias se hace muy complicado que esté funcionando correctamente
# ya que debo digitar TODOS las notas y hacer varias pruebas
