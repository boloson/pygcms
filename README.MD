# PyGCMS - Tools for processing GCMS data

### Prerequisite:
pip install netCDF4

### Usage:

```
from pygcms import build_df

# build pandas dataframe from cdf file with time as row index and mz as column if time_as_column=False

df = build_df('mycdf.cdf', time_as_column=False)

```
