# Code to seperate 29 data
'''
Note: The continous interval is of 29 days, so after DEC 2 Julian dat 336, we start to lose
data points, the data in each file becomes less that 8354; To avoid this we can add a condition.
'''


from datetime import datetime
start_time = datetime.now()





import pandas as pd
tide = pd.read_excel('D:/OneDrive - BUET/Advanced HAMELS 15.05.2021/Processed Data/Formatted_Merged_19.5_20_21.xlsx')


j = 1 # file name indexing
i = 0
while i+288 < len(tide):
    segment = tide[i:i+8353]

    name = r'D:\OneDrive - BUET\Advanced HAMELS 15.05.2021\29 Day Splitted Files\CTG_' + str(j) +'.xls'
    segment.to_excel(name, sheet_name = "Sheet1", index = False)
    
    if len(segment) < 8353:
        break # Any file having less than 29 days of data will be skipped
        # Still check the last file if the data is exactly 8353
    j = j + 1 
    i = i + 288 # 5 min interval 288 samples





end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))


