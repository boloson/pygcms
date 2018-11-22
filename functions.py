from netCDF4 import Dataset
import numpy as np
import pandas as pd

def build_df(file_name, time_as_column=False):
  '''
  Build intensity matraix dataframe from CDF files
  '''
  intensity_values = np.array(dataset.variables[__INTENSITY_STRING])
  intensity_list = []
  intensity_previous = intensity_values[0]
  intensity_list.append(intensity_previous)

  mz_strings = np.array(dataset.variables[__MASS_STRING])
  intensity = np.array(dataset.variables[__INTENSITY_STRING])
  time_list = np.array(dataset.variables[__TIME_STRING])

  mz_values = mz_strings.round().astype(np.int16)

  mass_list = []
  intensity_list = []
  scan_list = []

  intensity_prev = intensity[0]
  mass_prev = mz_values[0]

  mz_max = mz_values.max()
  mz_min = mz_values.min()

  num_mz = len(range(mz_min, mz_max)) + 1

  time_row = np.zeros(num_mz)

  mz_prev = mz_values[0]

  for i in range(len(mz_values)):
    mz = mz_values[i]
    if mz_prev <= mz:
      time_row[mz - mz_min] = intensity[i]
      mz_prev = mz

    else:
      scan_list.append(time_row)
      time_row = np.zeros(num_mz)
      time_row[mz - mz_min] = intensity[i]
      mz_prev = mz
  scan_list.append(time_row)   # add last row

  if not time_as_column:  
    df = pd.DataFrame(scan_list, columns=range(mz_min, mz_max+1), index=time_list)
  else:
    df = pd.DataFrame(np.transpose(scan_list), columns=time_list, index=range(mz_min, mz_max+1))
  
  return df