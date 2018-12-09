# PyGCMS - Tools for processing GCMS data

### Prerequisite:
pip install netCDF4
python 2.7

### Usage:

```
from pygcms import build_df

# build pandas dataframe from cdf file
df = build_df('mycdf.cdf', time_as_column=False)

```
