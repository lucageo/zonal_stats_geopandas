import geopandas as gpd
from rasterstats import zonal_stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import mapclassify
from rasterio.plot import show
from rasterio.plot import show_hist
import rasterio

zones = "/Users/lucabattistella/Desktop/geopandas/shp/WDPA_WDOECM_Jan2023_Public_TZA_shp_0/WDPA_WDOECM_Jan2023_Public_TZA_shp-polygons.shp"
values = "/Users/lucabattistella/Desktop/geopandas/GSOCmapV1.2.0.tif"
gdf = gpd.read_file(zones)


stats = gpd.GeoDataFrame(zonal_stats(gdf, values, stats=["mean"]))
gdf = gdf.join(stats)
#gdf = gdf.assign(mean_norm= gdf['mean'] / gdf['GIS_AREA'])
gdf.drop('geometry',axis=1).to_csv(r'/Users/lucabattistella/Desktop/geopandas/test.csv') 

# Create a figure and axes
fig, ax = plt.subplots(figsize=(5,5))
gdf.plot(ax=ax, column='mean', 
legend = True, cmap='GnBu',
    missing_kwds={
        "color": "Red",
        "edgecolor": "Red",
        "hatch": "///",
        "label": "Missing values",
    },
)
plt.show()

