

import rasterio
import numpy
import os 
import matplotlib as mpl
import matplotlib.pyplot as plt

import rasterio as rio
import geopandas as gpd


with rio.open("C:\\Users\\ees407\\Desktop\\NDVI\\Originals\\NAIP2010\\2010.tif") as src:
    naip_data = src.read()
    
# View shape of the data
naip_data.shape

naip_ndvi = (naip_data[3] - naip_data[0]) / (naip_data[3] + naip_data[0])
print(naip_ndvi)
print(naip_ndvi.shape)


fig, ax = plt.subplots(figsize=(6,6))
ndvi = ax.imshow(naip_ndvi, cmap='PiYG',
                vmin=-1, vmax=1)
fig.colorbar(ndvi, fraction=.05)
ax.set(title="NAIP Derived NDVI\n 13 June 2010 - Northern Humboldt County , Ca")
ax.set_axis_off()
plt.show()