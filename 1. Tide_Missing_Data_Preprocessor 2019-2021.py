"""
Import the data
Create a similar time series
Merge both data set
Fill the missing values in all columns except the water level columns
Fill the missing values using linear interpolation 
Save the data and compare with the original
"""




import pandas as pd



# declaration
in_dir = r'D:/OneDrive - BUET/Advanced HAMELS 15.05.2021/Raw Data/H1330-19.5.xlsx'
out_file = r'D:/OneDrive - BUET/Advanced HAMELS 15.05.2021/Processed Data/CTG_2019.5_Processed.xlsx'




# Import the data
ori_data = pd.read_excel(in_dir)
start_time = ori_data['DateTime'].iloc[0]
end_time = ori_data['DateTime'].iloc[-1]

# Create a similar time series
full_frame = pd.DataFrame(pd.date_range(start_time, end_time, freq = '5min'), columns = ['DateTime'])

# Merge both DataFrame + Sorting
merged_time_line = pd.merge(ori_data, full_frame, on = 'DateTime', how = 'outer', sort = True)

# Fill the missing values in all columns except the water level columns
merged_time_line['Site Name'] = merged_time_line['Site Name'].ffill()
merged_time_line['idSite'] = merged_time_line['idSite'].ffill()


# Fill the missing values using linear interpolation
merged_time_line['Level(m)'] = merged_time_line['Level(m)'].interpolate(method = 'linear')

# Save the data and compare with the original
merged_time_line.to_excel(out_file, index = False)


