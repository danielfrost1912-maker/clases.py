from claseAuto import Alumno
def main():
    print("Registro de alumno")
    nombre = input("Ingrese el nombre del alumno: ").strip()
    while True:
        try:
            edad = int(input("Ingrese la edad del alumno: "))
            if edad <= 0:
                print("La edad debe ser mayor que cero.")
                continue
            break
        except ValueError:
            print("Ingrese una edad valida.")
            curso = input("Ingrese el curso del alumnop: ").strip()
            alumno = Alumno(nombre, edad, curso)
            while True:
                print("Menu")
                print("1. Ver informacion")
                print("2. Agregar una nota")
                print("3. Ver notas")
                print("4. Salir")
                opcion = input("Elija una opcion: ").strip()
                if opcion == "1":
                    print("\n" + alumno.get_info())
                elif opcion == "2":
                    nota = input("Ingrese la nota (mayoe que 0 y menor que 11): ")
                    alumno.set_nota(nota)
                elif opcion == "3":
                    notas = alumno.get_notas()
                    if notas:
                        print("Notas:", notas)
                    else:
                        print("El alumno todavia no tiene notas")
                elif opcion == "4":
                    print("programa finalizao.")
                    break
                else:
                    print("Opcion no valida. Intente de nuevo.")

            if __name__ == "__main__":
                main()AAA