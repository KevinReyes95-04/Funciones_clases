# -----------------------------------------------
# Función para calcular el Bounding Box (BBOX)
# -----------------------------------------------

def calcular_bbox(coordenadas):
    """
    Calcula los límites geográficos (Bounding Box) de una lista de coordenadas.

    Parámetros
    ----------
    coordenadas : list of tuple
        Lista de coordenadas geográficas en formato (latitud, longitud).

    Retorna
    -------
    tuple
        Cuatro valores numéricos en el siguiente orden:
        lat_min : float -> Latitud mínima encontrada
        lat_max : float -> Latitud máxima encontrada
        lon_min : float -> Longitud mínima encontrada
        lon_max : float -> Longitud máxima encontrada

    Ejemplo
    -------
    calcular_bbox([(4.6, -74.0), (6.2, -75.5)])
    -> (4.6, 6.2, -75.5, -74.0)
    """

    # Extraer latitudes y longitudes
    latitudes = [lat for lat, lon in coordenadas]
    longitudes = [lon for lat, lon in coordenadas]

    # Calcular valores extremos
    lat_min = min(latitudes)
    lat_max = max(latitudes)
    lon_min = min(longitudes)
    lon_max = max(longitudes)

    return lat_min, lat_max, lon_min, lon_max

# -----------------------------------------------
# Coordenadas de 10 principales ciudades de Colombia
# -----------------------------------------------

ciudades_colombia = [
    (4.6097, -74.0817),   # Bogotá
    (6.2442, -75.5812),   # Medellín
    (3.4516, -76.5320),   # Cali
    (10.9639, -74.7964),  # Barranquilla
    (10.3910, -75.4794),  # Cartagena
    (7.1254, -73.1198),   # Bucaramanga
    (4.8133, -75.6961),   # Pereira
    (4.4389, -75.2322),   # Ibagué
    (2.4448, -76.6147),   # Popayán
    (7.8891, -72.4967)    # Cúcuta
]

# -----------------------------------------------
# Uso de la función
# -----------------------------------------------

lat_min, lat_max, lon_min, lon_max = calcular_bbox(ciudades_colombia)

print("Latitud mínima:", lat_min)
print("Latitud máxima:", lat_max)
print("Longitud mínima:", lon_min)
print("Longitud máxima:", lon_max)

