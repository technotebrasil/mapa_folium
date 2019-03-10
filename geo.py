#Importa a biblioteca
import folium

#Cria o mapa base
map = folium.Map(location=[-20.807382,-49.360453], zoom_start = 10)

#Multiplos marcadores
for coordinates in [[-20.800385, -49.367797],[-20.800154, -49.368665]]:
    folium.Marker(location=coordinates, icon=folium.Icon(color = 'green')).add_to(map)

#Salva o mapa
map.save("mapa.html")
