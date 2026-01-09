import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def create_contour_map(region):
    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw={'projection': ccrs.PlateCarree()})
    ax.set_extent(region['extent'], ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE) 
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.stock_img() 
    filename = region['name'].replace(' ', '_') + '.png'
    plt.savefig(filename) 
    plt.close()

regions = [
    {'name': 'Africa', 'extent': [-20, 60, -40, 40]},
    {'name': 'Canada', 'extent': [-140, -50, 40, 85]},
    {'name': 'Japan', 'extent': [129, 146, 30, 46]},
    {'name': 'China', 'extent': [73, 135, 18, 54]},
    {'name': 'India', 'extent': [68, 90, 6, 37]}
]

for region in regions:
    create_contour_map(region)