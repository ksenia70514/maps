import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def create_graph(cities):
    fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': ccrs.PlateCarree()})
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.set_global()

   
    for city in cities:
        ax.plot(city['lon'], city['lat'], 'ro') 
        ax.text(city['lon'], city['lat'], city['name'], fontsize=8)

    filename = 'cities_map.png'
    plt.savefig(filename)
    plt.close()
    return filename