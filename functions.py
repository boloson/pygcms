def build_df(fname, time_as_column=False):
  ''' 
  Parse a ANDI netCDF file to a pandas dataframe 
  fname -- full file name path
  time_as_column --  use time values as column
  
  '''

  dataset = Dataset(fname, 'r')

  SCAN_INDEX = 'scan_index'
  POINT_COUNT = 'point_count'
  MASS_VALUES = 'mass_values'
  INTENSITY_VALUES = 'intensity_values'
  SCAN_ACQ_TIME = 'scan_acquisition_time'

  scan_indexes = dataset.variables[SCAN_INDEX]
  mz_values = np.asarray(dataset.variables[MASS_VALUES])
  mz_values = np.rint(mz_values).astype(int)
  point_counts =  dataset.variables[POINT_COUNT]
  intensity_values = dataset.variables[INTENSITY_VALUES]
  time_val = np.array([t.data for t in dataset.variables[SCAN_ACQ_TIME]])

  mz_max = int(round(np.max(mz_values), 0))
  mz_min = int(round(np.min(mz_values), 0))
  num_mz = mz_max - mz_min + 1
  point_upper_bound = len(intensity_values) - 1

  scan_list = []
  time_list = []
  start = time()
  for i in range(len(scan_indexes)):
    num_point = point_counts[i]
    if num_point == 0:
      continue
    start_i = scan_indexes[i]  
    row_intensity = intensity_values[start_i:start_i+ num_point]
    row_mz = mz_values[start_i:start_i+ num_point]
    np_fill_index = row_mz - mz_min
    time_row = np.zeros(num_mz)
    np.put(time_row, np_fill_index, row_intensity)

    scan_list.append(time_row)
    time_list.append(time_val[i])
  
  if time_as_column:
    df = pd.DataFrame(np.transpose(scan_list), columns=time_list, index=range(mz_min, mz_max+1))
  else:
    df = pd.DataFrame(scan_list, columns=range(mz_min, mz_max+1), index=time_list)

  return df
