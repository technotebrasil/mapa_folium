#Importa a biblioteca
import folium
from folium.plugins import MarkerCluster
import pandas as pd

#carrega os dados
data = pd.read_csv("volcanos_USA.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']

#Funcão pra mudar as cores
def color_change(elev):
    if(elev < 1000):
        return('green')
    elif(1000 <= elev <3000):
        return('orange')
    else:
        return('red')


#Cria o mapa base
map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 5, tiles = "CartoDB dark_matter")

#Cria o cluster
marker_cluster = MarkerCluster().add_to(map)

#Plota os marcadores e add em 'marker_cluster'
for lat, lon, elevation in zip(lat, lon, elevation):
    folium.CircleMarker(location=[lat, lon], radius = 9, popup=str(elevation)+" m", fill_color=color_change(elevation), color="gray", fill_opacity = 0.9).add_to(marker_cluster)



#Salva o mapa
map.save("map2.html")
