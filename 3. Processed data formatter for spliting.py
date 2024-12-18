# -*- coding: utf-8 -*-
"""
This program formats the program 2: Processed Data Merger.py 
to the specific format of the matlab output.
"""

import pandas as pd
from datetime import datetime
import numpy as np
start_time = datetime.now()



# reading the data
tide_merged = pd.read_excel(r'D:/OneDrive - BUET/Advanced HAMELS 15.05.2021/Processed Data/Merged_19.5_20_21.xlsx')


# splitting datetime into Date and Time
tide_merged['Date'] = np.floor(tide_merged['DateTime'])
tide_merged['Time'] = tide_merged['DateTime'] - np.floor(tide_merged['DateTime'])



# resetting column name as per MATLAB format
col_header = {'idSite': 'Station', 'Level(m)': 'WL(m)'}
out_frame = tide_merged.iloc[:, [0,4,5,3]]
out_frame.rename(columns = col_header, inplace = True)




out_frame.to_excel(r'D:/OneDrive - BUET/Advanced HAMELS 15.05.2021/Processed Data/Formatted_Merged_19.5_20_21.xlsx', index = False)




end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
