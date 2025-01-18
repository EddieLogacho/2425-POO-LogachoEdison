class Equipos:
    def __init__(self, nombre,pais):
        self.nombre=nombre
        self.pais=pais
    def mostrar_informacion(self):
        print(f"El nombre del Equipo es:",self.nombre)
        print(f"El pais de origen es:",self.pais)

class Figura(Equipos):
    def __init__(self,nombre,pais,jugador):
        super().__init__(nombre,pais)
        self.jugador=jugador
    def mostrar_informacion(self):
        print(f"El nombre del jugador es:",self.jugador)

equipo1=Equipos("Aucas","Ecuador")
equipo1.mostrar_informacion()
equipo2=Equipos("al-Nassr","Arabia")
equipo2.mostrar_informacion()
equipo3=Figura("Inter","Estados Unidos","messi")
equipo3.mostrar_informacion()
equipo4=Figura("Chelse","Inglatera","Moises ")
equipo4.mostrar_informacion()


