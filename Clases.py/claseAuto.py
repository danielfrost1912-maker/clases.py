class Alumno:
    def __init__(self, nombre, edad, curso):
        self.__nombre = nombre
        self.__edad = edad
        self.curso = curso
        self.__notas = []

    def get_info(self):
        return (
            f"Nonbre: {self.__nombre}\n"
            f"Edad: {self.__edad}\n"
            f"Curso: {self.__curso}"
            )
    def get_notas(self):
        return self.__notas.copy()
    def set_nota(self, nueva_nota):
        try:
            nota = float(nueva_nota)
        except ValueError:
            print("Error: la nota debe ser un numero.")
            return
        if 0 < nota < 11:
            self.__notas.append(nota)
            print("Nota agregada correctamente.")
        else:
            print("Error: la nota debe ser mayor que 0 y menor que 11")
            