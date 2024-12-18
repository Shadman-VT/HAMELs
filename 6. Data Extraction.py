
# Header added to the main csv file output from MATLAB
# Import the pandas library, renamed as pd 
import pandas as pd # for importing and selecting data in csv
import csv


for j in range(12): # 12: There are 12 parameters in the CSV files
    

    my_list = [] # to write a single csv file sequencially 
    
    Station = r'D:\OneDrive - BUET\Advanced HAMELS 15.05.2021\2015-2019\MATLAB Output file\CTG_1hr_'

    ########################################################################
    for i in range(1, 1463): # will depend on the number of input file
    ########################################################################
        
        df = pd.read_csv(Station + str(i) + '_Out.csv') # read file handle
        const_name = df.iloc[j,0] # constituent name
        
        if j < 9: # the constituents have amp, phase
            amp = df.iloc[j,1] # amplitude
            phase =df.iloc[j,2] # phase
            my_list.append([amp,phase])
        
        else:
            value = df.iloc[j,1] # statistical parameter value
            my_list.append([value])
        
       
       
    output_file = r'D:\OneDrive - BUET\Advanced HAMELS 15.05.2021\Constituient Results\CTG_' + const_name + '.csv' 
    with open(output_file, 'w', newline = '') as f:
        thewriter = csv.writer(f)
        
        # sequentially write all the values to csv
        i = 0
        while i < len(my_list):
            thewriter.writerow(my_list[i])
            i = i + 1
        