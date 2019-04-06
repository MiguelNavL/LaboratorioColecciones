"""
Los comentarios está ocultos para ver más fácil el código, al hacer clic en "+" en la parte
izquierda del editor (yo estoy trabajando con PyCharm para este laboratorio (en la linea 10 por ejemplo)
"""


def calculate_final_grade(student_grades_list):

    grade_sum = 0
    grade_count = len(student_grades_list)

    '''
    Recorro la lista sacando cada uno de los elementos 
    y guardando momentaneamente cada uno en la variable "grade"
    y sumarlo a la suma total
    '''
    for grade in student_grades_list:
        grade_sum += grade

    '''        
    También se pudo hacer de la siguiente manera pero es muy largo:
    
    recorrrer "i" entre 0 y la longitud de la lista (por ejemplo de 0 a 4
    y luego buscar el elemento en la posición "i" de la lista, de la siguiente manera
    
    for i in range(0, len(student_grades_list)):
        grade_sum += student_grades_list[i]

    Normalmente de una manera similar a esta se hace en java o c, pero Python es nás compacto ;)

    '''

    # La nota final es la suma de todos los elementos dividido en la cantidad de elementos
    # len(student_grades_list) es una función que me da la cantidad de elementos en una lista o longitud
    final_grade = grade_sum / grade_count

    return final_grade


def calculate_best_grade(student_grades_list):

    # Inicialmente, asumamos que la mejor nota es la primera de la lista, es decir la posición 0
    best_grade = student_grades_list[0]

    '''
    Recorro la lista sacando cada uno de los elementos 
    y guardando momentaneamente cada uno en la variable "grade"
    y sumarlo a la suma total
    '''
    for grade in student_grades_list:
        # Si la nota actual en la que vamos recorriendo la lista es mayor que la mayor
        # entonces la nueva nota mayor será la nota actual
        if grade > best_grade:
            best_grade = grade

    # Al finalizar la nota mayor será la que esté en best_grade, si ninguna fue mayor que la primera
    # entonces la nota mayor será la primera
    return best_grade


def remove_worst_grade(student_grades_list):

    # Inicialmente, asumamos que la peor nota es la primera de la lista, es decir la posición 0
    # así que guardo el valor de la nota en la posición 0 e indico que la posición de la peor es 0
    worst_grade = student_grades_list[0]
    worst_grade_position = 0

    # Necesito la cantidad de notas para calcular el promedio
    grades_count = len(student_grades_list)

    # A la suma final se le debe restar la primera nota
    grade_sum = 0

    '''
    Recorro la lista sacando cada uno de los elementos 
    y guardando momentaneamente cada uno en la variable "grade" 
    '''

    # Antes de iniciar el ciclo llevo un contador de la posición en la que se va
    position_count = 0

    for grade in student_grades_list:
        # Si la nota actual en la que vamos recorriendo la lista es menor que la peor
        # entonces la nueva peor será la nota actual
        # sin embargo debemos recordar que la primera nota fue restada de la suma

        if grade < worst_grade:
            # Actualizo la posición de la peor nota y el valor de la peor nota
            worst_grade_position = position_count
            worst_grade = grade

        # Una vez finalizado el ciclo, incremento el contador de la posición en 1
        position_count += 1

    # Remuevo la peor nota de la lista, quitando el elemento que está en la posición de la peor nota
    student_grades_list.pop(worst_grade_position)

    # Al finalizar se retorna una lista sin la nota menor
    return student_grades_list

