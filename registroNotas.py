import pickle

class Alumno:
    def __init__(self,nombre, apellido, edad, nota, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota = nota
        self.nacionalidad = nacionalidad
            
    def imprimirDatos(self):
        print(f"Nombre : {self.nombre}, Apellido: {self.apellido}, Edad : {self.edad}, Nota : {self.nota}, Nacionalidad : {self.nacionalidad}")
    
    def validarNota(self, nota):
        while True:
            try:
                nota = int(input("Ingrese la nota (0-20): "))
                if 0 <= nota <= 20:
                    return nota
                else:
                    print("La nota debe estar en el rango de 0 a 20. Inténtelo nuevamente.")
                    return nota
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")

def guardar_Alumnos(lista_Alumnos,archivo):
    with open(archivo, 'wb') as f:
        pickle.dump(lista_Alumnos,f)

def cargar_Alumnos(archivo):
    try:
        with open(archivo, 'rb') as f:
            productos_datos = pickle.load(f)
        return productos_datos
    except FileNotFoundError:
        return []


def main():
    archivo_Alumnos = "alumnosInfo.pkl"
    lista_Alumnos = cargar_Alumnos(archivo_Alumnos)
    while True:
        print("BIENVENIDOS AL REGISTRO DE NOTAS")
        print("INGRESE CAMANDO: R, C, P, S, X")
        print("R). Registrar Alumno")
        print("C) Calificar Alumno")
        print("P) Promedio de todos los Alumnos")
        print("S) Suma de notas de todos los Alumnos")
        print("X) Guardar y Salir")

        opcion = input("Seleccione una opcion : ")

        if opcion == 'R':
            nombre = input("Ingrese el Nombre del Alumno : ")
            apellido = input("Ingrese el Apellido del Alumno : ")
            edad = input("Ingrese la Edad del Alumno : ")
            nota = input("Ingrese la Nota del Alumno : ")
            nacionalidad = input("Ingrese la Nacionalidad del Alumno : ")

            alum = Alumno(nombre, apellido, edad, nota, nacionalidad)
            lista_Alumnos.append(alum)
        elif opcion == 'C':
            for productoInfo in lista_Alumnos:
                print("Alumno " + productoInfo.nombre  + productoInfo.apellido)
                productoInfo.nota = productoInfo.validarNota(input("Ingrese Nota : "))
                productoInfo.imprimirDatos()
        elif opcion == 'P':
            sumanotas = 0
            cantidad_alumno = len(lista_Alumnos)
            if cantidad_alumno >= 0:
                for productoInfo in lista_Alumnos:
                    sumanotas += productoInfo.nota
                promedionota = sumanotas / cantidad_alumno
                print("promedio nota:", promedionota)
        elif opcion == 'S':
            sumanotas = 0
            cantidad_alumno = len(lista_Alumnos)
            if cantidad_alumno >= 0:
                for productoInfo in lista_Alumnos:
                    sumanotas += productoInfo.nota
                print("La suma de notas de:", cantidad_alumno, "es:", sumanotas)
        elif opcion == 'X':
            guardar_Alumnos(lista_Alumnos, archivo_Alumnos)
            print("Saliendo del programa")
            break
        elif opcion == '4':
            pass
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()