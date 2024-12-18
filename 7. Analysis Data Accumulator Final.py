# -*- coding: utf-8 -*-
"""
This programs takes in the output of program 6 and creates one single csv that has all the data
"""

import pandas as pd
import glob


wl_dir = r"D:\OneDrive - BUET\Advanced HAMELS 15.05.2021\Constituient Results"
wl_files = sorted(glob.glob(wl_dir+"\*.csv"))

main_frame = pd.DataFrame()

for i in range(len(wl_files)): # summing just the contituients 

    if i < 9:
        
        # Creating column header based on read file
        col_header = wl_files[i].split('\\')[-1].split(".")[1].strip()
        amp = col_header + '_Amp'
        phs = col_header + '_Phase'
        
        
        df = pd.read_csv(wl_files[i], header = None)
        
        # Renaming the read dataframe columns
        df.rename(columns = {0: amp, 1: phs}, inplace= True)
        
        main_frame = pd.concat([main_frame, df], axis = 1)
        
    
    else:
        # Creating column header based on read file
        col_header = wl_files[i].split('\\')[-1].split(".")[1].strip()
        
    
        df = pd.read_csv(wl_files[i], header = None)
        
        # Renaming the read dataframe columns
        df.rename(columns = {0: col_header}, inplace= True)
        
        main_frame = pd.concat([main_frame, df], axis = 1)
        
        
        
    

main_frame.to_csv(r'D:\OneDrive - BUET\Advanced HAMELS 15.05.2021\Constituient Results\CTG_Analysis_Data_2015_2019.csv', index = None)