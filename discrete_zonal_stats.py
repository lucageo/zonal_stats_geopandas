

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

zones = '/Users/lucabattistella/Documents/gis_data/WDPA_WDOECM_Jan2023_Public_TZA_shp_0/WDPA_WDOECM_Jan2023_Public_TZA_shp-polygons.shp'
values= "/Users/lucabattistella/Documents/gis_data/tanzania_test/geonode__tanzanialandcover2015.tif"

gdf = gpd.read_file(zones)
df = gpd.read_file(zones)


stats = gpd.GeoDataFrame(zonal_stats(gdf, values, categorical=True, stats=["count"]))

gdf = gdf.join(stats)


ras = rasterio.open(values)
a = ras.transform
x, y = abs(a[0]), abs(a[4])
pixelarea = x*y

stats = stats.fillna(0)*pixelarea/1e6 #Area in sq km per pixel value

result = pd.merge(left=df, right=stats, left_index=True, right_index=True)


del result['geometry']

# export the result to a CSV file
result.to_csv(r'/Users/lucabattistella/Desktop/test.csv')



