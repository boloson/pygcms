SCAN_INDEX = 'scan_index'
POINT_COUNT = 'point_count'
MASS_VALUES = 'mass_values'
INTENSITY_VALUES = 'intensity_values'
SCAN_ACQ_TIME = 'scan_acquisition_time'

scan_indexes = dataset.variables[SCAN_INDEX]
mz_values = dataset.variables[MASS_VALUES]
point_counts =  dataset.variables[POINT_COUNT]
intensity_values = dataset.variables[INTENSITY_VALUES]
time_val = np.array([t.data for t in dataset.variables[SCAN_ACQ_TIME]])

mz_max = int(round(np.max(mz_values), 0))
mz_min = int(round(np.min(mz_values), 0))
num_mz = mz_max - mz_min + 1
point_upper_bound = len(intensity_values) - 1

scan_list = []
time_list = []

start = time.time()

for i in range(len(scan_indexes)):
  
  start_i = scan_indexes[i]
  num_point = point_counts[i]

  if num_point == 0 :
    continue
  time_row =  np.zeros(num_mz)
  
  value_index = start_i
  for incr in range(num_point):
    cur_i = start_i + incr
    mz = int(round(mz_values[cur_i]))
    intensity_val = intensity_values[cur_i]
    time_row[mz-mz_min] = time_row[mz-mz_min] + intensity_val
    
  scan_list.append(time_row)
  time_list.append(time_val[i])
  
  if time_as_column:
    df = pd.DataFrame(np.transpose(scan_list), columns=time_list, index=range(mz_min, mz_max+1))
  else:
    df = pd.DataFrame(scan_list, columns=range(mz_min, mz_max+1), index=time_list)

  return df
