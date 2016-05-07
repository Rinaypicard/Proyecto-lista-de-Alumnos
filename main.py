from alumnos import alumno

lista = []

def start():
    i = input("¿Que deseas hacer?\n (1) Mostrar Alumnos\n (2) Crear Nuevo Alumno\n (3) Salir del Programa")

    if i == "1":
        show()

    elif i == "2":
        add()
    elif i == "3":
        print("   ¡Gracias!\n Regresa pronto")
    else:
        print("No se reconocio la respuesta\n Vuelva a intentarlo")
        start()

def add():
    name = input("Nombre:")
    lastName = input("Apellido:")
    age = input("Edad:")
    cinta = input("Cinta:")
    new = alumno(name, lastName, age, ("Cinta " + cinta))
    lista.append(new)
    start()

def show():
    for i in lista:
        print(i.getAll())
    start()


start()