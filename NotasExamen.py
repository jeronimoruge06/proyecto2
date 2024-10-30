listado = []
notas = []

def mostrarmenu() -> str:
    menu = input('''
------------------------------------------------------------
---------------------MENU PRINCIPAL-------------------------
------------------------------------------------------------
(1). Registrar estudiantes(10)
(2). Asignar 3 notas parciales a cada estudiante
(3). Registrar el numero de inasistencias de cada estudiante
(4). Mostrar el listado de todos los estudiantes
(5). Calcular nota final de los estudiantes
(9). Cerrar programa
''')
    return menu
def registro_estudiante() -> None:
    cantidad = int(input('''----------------------------------------------------
¿Cuantos Estudiantes nuevos desea crear? (maximo 10)
----------------------------------------------------

'''))
    if cantidad <= 10:
        for i in range(cantidad):
            codigo = input('Ingrese el codigo del estudiante #' + str(i + 1) + ': ')
            idExistente = True
            while idExistente:
                idExistente = False
                for j in listado:
                    if j[0] == codigo:
                        idExistente = True
                        codigo = input('''
----------------------------------------
El codigo que intenta ingresar ya existe
Por favor ingrese uno nuevo
----------------------------------------

''')
            name = input(f'Ingrese el nombre del estudiante #{(i+1)}: ')
            listado.append([codigo,name])
    else:
        print('La cantidad de estudiantes excede lo establecido')

def asignar_notas() -> None:
    for i in listado:
        print(f'''
--------------------------------------------
INGRESE LAS NOTAS DEL ESTUDIANTE: {i[1]}
--------------------------------------------
''')
        p1 = int(input('Ingrese la nota del parcial #1: '))
        p2 = int(input('Ingrese la nota del parcial #2: '))
        p3 = int(input('Ingrese la nota del parcial #3: '))

        notas.append([p1, p2, p3, 0])
        print(notas)

def inasistencias() -> None:
    for idx, i in enumerate(listado):
        print('''

-------------------------------------
Ingrese el total de las inasistencias
-------------------------------------
''')
        inasistencias = int(input(f'Asigne las inasistencias del estudiante {(i[1])}: '))
        notas[idx][3]  = inasistencias

def mostrar_lista() -> None:
    print('''

--------------------------------------
LISTADO DE LOS ESTUDIANTES REGISTRADOS
--------------------------------------
''')
    for i in listado:
        print(f'Codigo: {i[0]} Nombre: {i[1]}')

def nota_final() -> None:
    print('''
-- CODIGO -- NOMBRE -- P1 -- P2 -- P3 -- INASISTENCIAS -- NOTA FINAL --
''')
    for idx, i in enumerate(notas):
        n1 = i[0]
        n2 = i[1]
        n3 = i[2]
        ina = i[3]
        nota_f = float((n1 + n2 + n3) / 3)
        if ina >= 10 and ina < 15:
            nota_f -= 0.5
        elif ina >= 15:
            nota_f -= 1
        print(f'   {listado[idx][0]}         {listado[idx][1]}         {n1}     {n2}     {n3}     {ina}                {nota_f}')


#hola
opcion = ' '
while opcion != '9':
    opcion = mostrarmenu()
    match opcion:
        case '1':
            registro_estudiante()
        case '2':
            asignar_notas()
        case '3':
            inasistencias()
        case '4':
            mostrar_lista()
        case '5':
            nota_final()
        case _:
            print('La opcion no está dentro del rango establecido')