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
        print("1. Crear Almuno")
        print("2. Mostrar Alumnos")
        print("3. Guardar y salir")

        opcion = input("Seleccione una opcion : ")

        if opcion == '1':
            nombre = input("Ingrese el Nombre del Alumno : ")
            apellido = input("Ingrese el Apellido del Alumno : ")
            edad = input("Ingrese la Edad del Alumno : ")
            nota = input("Ingrese la Nota del Alumno : ")
            nacionalidad = input("Ingrese la Nacionalidad del Alumno : ")

            alum = Alumno(nombre, apellido, edad, nota, nacionalidad)
            lista_Alumnos.append(alum)
        elif opcion == '2':
            for productoInfo in lista_Alumnos:
                productoInfo.imprimirDatos()
        elif opcion == '3':
            guardar_Alumnos(lista_Alumnos, archivo_Alumnos)
            print("Saliendo del programa")
            break
        elif opcion == '4':
            pass
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()