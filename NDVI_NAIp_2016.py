#NDVI 
#https://www.earthdatascience.org/courses/earth-analytics-python/multispectral-remote-sensing-in-python/vegetation-indices-NDVI-in-python/

import rasterio
import numpy
import os 
import matplotlib as mpl
import matplotlib.pyplot as plt

import rasterio as rio
import geopandas as gpd

Inputpath="C:\\Users\\ees407\\Desktop\\NDVI\\Originals\\"

with rio.open(Inputpath+"2016_tiff.tif") as src:
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
ax.set(title="NAIP Derived NDVI\n 16 September 2016 - Northern Humboldt County , Ca")
ax.set_axis_off()
plt.show()


    