# PyGCMS - Tools for processing GCMS data

### Prerequisite:
pip install netCDF4 

!git clone https://github.com/boloson/pygcms.git


### Usage:
```
from pygcms.functions import build_df

# build pandas dataframe from cdf file with time as row index and mz as column if time_as_column=False

df = build_df('mycdf.cdf', time_as_column=False)

```
