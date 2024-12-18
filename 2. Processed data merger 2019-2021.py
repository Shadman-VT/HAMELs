# -*- coding: utf-8 -*-
"""
Concat 2019+ 2020 2021 files
"""

import pandas as pd



from datetime import datetime
start_time = datetime.now()
# do your work here






file_19 = pd.read_excel(r'D:/OneDrive - BUET/Advanced HAMELS 15.05.2021/Processed Data/CTG_2019.5_Processed.xlsx')
file_20 = pd.read_excel(r'D:/OneDrive - BUET/Advanced HAMELS 15.05.2021/Processed Data/CTG_2020_Processed.xlsx')
file_21 = pd.read_excel(r'D:/OneDrive - BUET/Advanced HAMELS 15.05.2021/Processed Data/CTG_2021_Processed.xlsx')



df = pd.concat([file_19, file_20, file_21], ignore_index = True )


df.to_excel(r'D:/OneDrive - BUET/Advanced HAMELS 15.05.2021/Processed Data/Merged_19.5_20_21.xlsx', index = False)



end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))



