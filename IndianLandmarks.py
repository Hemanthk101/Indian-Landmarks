import folium
import pandas 
data = pandas.read_csv("IL.csv")
name = list(data["Name"]) 
ty = list(data["Type"])
year = list(data["Year"])
lat = list(data["Latitude"])
lon = list(data["Longitude"])

map = folium.Map(location=[22.9734, 78.6569],zoom_start=5.5,tiles="OpenStreetMap")

fgD = folium.FeatureGroup(name="Details")
for n,t,y,la,ln in zip(name,ty,year,lat,lon):
    fgD.add_child(folium.Marker(
    location=[la, ln],
    popup=folium.Popup("Name: {}<br>Type: {}<br>Year: {}".format(n, t, y), max_width=250),
    icon=folium.CustomIcon("{}.jpg".format(n), icon_size=(50,50))
))

fgS = folium.FeatureGroup(name="States")
fgS.add_child(folium.GeoJson(data=(open('INDIA_STATES.geojson','r',encoding='utf-8-sig').read())))

map.add_child(fgD)
map.add_child(fgS)
map.add_child(folium.LayerControl())
map.save("Map.html")