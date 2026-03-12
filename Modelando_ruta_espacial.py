# -----------------------------------------------
# Taller: Clases e interacción
# -----------------------------------------------

# 1️ Importación de librerías
import math


# -----------------------------------------------
# 2️ Definición de la clase PuntoEspacial
# -----------------------------------------------

class PuntoEspacial:
    """
    Representa un punto geográfico con latitud, longitud y nombre.
    Incluye un método para calcular la distancia hacia otro punto
    usando la fórmula de Haversine.
    """

    def __init__(self, latitud, longitud, nombre="Punto"):
        self.latitud = latitud
        self.longitud = longitud
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} ({self.latitud}, {self.longitud})"

    def distancia_hacia(self, otro_punto, radio=6371.0):
        """
        Calcula la distancia geodésica hacia otro PuntoEspacial.

        Parámetros
        ----------
        otro_punto : PuntoEspacial
        radio : float
            Radio de la Tierra (6371 km por defecto)

        Retorna
        -------
        float
            Distancia entre los puntos.
        """

        lat1 = math.radians(self.latitud)
        lon1 = math.radians(self.longitud)
        lat2 = math.radians(otro_punto.latitud)
        lon2 = math.radians(otro_punto.longitud)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        return radio * c


# -----------------------------------------------
# 3️ Definición de la clase RutaGeografica
# -----------------------------------------------

class RutaGeografica:
    """
    Representa una ruta compuesta por múltiples objetos PuntoEspacial.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = []

    def agregar_punto(self, punto):
        """
        Agrega un PuntoEspacial a la ruta.
        """
        if not isinstance(punto, PuntoEspacial):
            raise TypeError("El objeto debe ser de tipo PuntoEspacial")

        self.puntos.append(punto)

    def medir_distancia_total(self):
        """
        Calcula la distancia total de la ruta.
        """

        distancia_total = 0

        for i in range(len(self.puntos) - 1):

            punto_actual = self.puntos[i]
            punto_siguiente = self.puntos[i + 1]

            distancia_total += punto_actual.distancia_hacia(punto_siguiente)

        return distancia_total

    def imprimir_distancias(self):
        """
        Imprime la distancia entre cada par de ciudades consecutivas.
        """

        for i in range(len(self.puntos) - 1):

            punto_actual = self.puntos[i]
            punto_siguiente = self.puntos[i + 1]

            distancia = punto_actual.distancia_hacia(punto_siguiente)

            print(f"Distancia de {punto_actual.nombre} a {punto_siguiente.nombre}: {distancia:.2f} km")


# -----------------------------------------------
# 4️ Creación de puntos (ciudades)
# -----------------------------------------------

bogota = PuntoEspacial(4.6097, -74.0817, "Bogotá")
medellin = PuntoEspacial(6.2442, -75.5812, "Medellín")
cali = PuntoEspacial(3.4516, -76.5320, "Cali")
barranquilla = PuntoEspacial(10.9639, -74.7964, "Barranquilla")
cartagena = PuntoEspacial(10.3910, -75.4794, "Cartagena")
bucaramanga = PuntoEspacial(7.1254, -73.1198, "Bucaramanga")
pereira = PuntoEspacial(4.8133, -75.6961, "Pereira")
ibague = PuntoEspacial(4.4389, -75.2322, "Ibagué")
popayan = PuntoEspacial(2.4448, -76.6147, "Popayán")
cucuta = PuntoEspacial(7.8891, -72.4967, "Cúcuta")


# -----------------------------------------------
# 5 Construcción de la ruta
# -----------------------------------------------

ruta_andes = RutaGeografica("Ruta de los Andes")

ciudades = [
    bogota, medellin, cali, barranquilla, cartagena,
    bucaramanga, pereira, ibague, popayan, cucuta
]

for ciudad in ciudades:
    ruta_andes.agregar_punto(ciudad)


# -----------------------------------------------
# 6️ Ejecución
# -----------------------------------------------

print("Ruta:", ruta_andes.nombre)
print()

ruta_andes.imprimir_distancias()

print()
print("Distancia total de la ruta:", round(ruta_andes.medir_distancia_total(), 2), "km")