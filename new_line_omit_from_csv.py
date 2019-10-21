import pandas as pd
import numpy as np
import csv
import os
from os import path

#old_file_name = 'art_load_balancer_spikes'
#file_extention = '.csv'

old_file_name = 'nyc_taxi_TM_pred'
add = '_fault'
file_extention = '.csv'

def rename_read_modify_csv():
    os.rename( "./prediction./" + old_file_name+'.csv', "./prediction./"+old_file_name+add+file_extention)

    with open("./prediction./" + old_file_name+add+file_extention) as old_file:
        old_file_object = csv.reader(old_file, delimiter=',')
        with open("./prediction./" + old_file_name + file_extention,'wb') as new_file:
            new_file_object = csv.writer(new_file, delimiter=',')

            for row in old_file_object:
                    new_file_object.writerow(row)

def main():
    rename_read_modify_csv()

if __name__=='__main__':
    main()
