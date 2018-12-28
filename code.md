# Python

```
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from datetime import datetime
%matplotlib inline

import importlib

import sys

xxpath = 'c:/work/code'
if xxpath not in sys.path:
    sys.path.append( xxpath )
import xxds

importlib.reload(xxds)

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)

%matplotlib inline
```

# pandas

```
df.drop( columns=['col1', 'col2'] )

gdf_2163 = gdf.to_crs({'init': 'epsg:2163'})
gdf_2163['area_km'] = gdf_2163.area/10.e6

good to create buffer
gdf_3174 = gdf.to_crs({'init': 'epsg:3174'})
gdf_3174['area_km'] = gdf_3174.area/10.e6


gpd_out.sjoin( gdf1, gdf2, how='left', op='intersects' )
```
