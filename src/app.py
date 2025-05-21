import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

# Spotify API credentials
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

#4
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

#5 ID del artista 
metallica_id = "2ye2Wgw4gimLv2eAKyk1NB"

# Los temas más populares del artista
results = spotify.artist_top_tracks(metallica_id)

# Extraer nombre, popularidad y duración (convertida a minutos)
tracks_info = [
    {
        "nombre": track["name"],
        "popularidad": track["popularity"],
        "duración_minutos": round(track["duration_ms"] / 60000, 2), #para convertir los milisegundos en minutos y limitar a dos decimales.
    }
    for track in results["tracks"]
]

# Mostrar resultados
for track in tracks_info:
    print(track)

#6 Convertir la lista de diccionarios a un DataFrame de Pandas
df_tracks = pd.DataFrame(tracks_info)

# Ordenar las canciones por popularidad de menor a mayor
df_tracks_sorted = df_tracks.sort_values(by="popularidad", ascending=True)

# Mostrar el top 3 con menor popularidad
print(df_tracks_sorted.head(3))

plt.figure(figsize=(8, 5))
plt.scatter(df_tracks_sorted["duración_minutos"], df_tracks_sorted["popularidad"], alpha=0.7)
plt.xlabel("Duración (minutos)")
plt.ylabel("Popularidad")
plt.title("Relación entre duración y popularidad de canciones")
plt.grid(True)
plt.show()