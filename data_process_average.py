import pandas as pd
import numpy as np
import csv

#old_file_name = 'art_load_balancer_spikes'
#file_extention = '.csv'

old_file_name = '_LBNL_a6_bus1_C1MAG_truncated'
file_extention = '.csv'


def INITIALIZE(func):
    setattr(func,"sample_number",0)
    setattr(func,"second",0)
    setattr(func,"minute",0)
    setattr(func,"hour",0)
    setattr(func,"day",1)
    setattr(func,"month",10)
    setattr(func,"year",2015)
    return func

"""
def INITIALIZE(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate
"""
#@INITIALIZE({"sample_number":0, "second":0, "minute":10, "hour":0, "day":1, "month":10, "year":2015})
#@INITIALIZE(sample_number=0, second=0, minute=0, hour=0, day=1, month=10, year=2015)

@INITIALIZE
def my_clock():
    my_clock.sample_number = my_clock.sample_number + 1
    #print(my_clock.sample_number)
    if my_clock.sample_number == 120:
        my_clock.sample_number = 0
        my_clock.second = my_clock.second + 1
        #print('second',my_clock.second)

    if my_clock.second == 60:
        my_clock.second = 0
        my_clock.minute = my_clock.minute + 1
        #print('minute',my_clock.minute)

    if my_clock.minute == 60:
        my_clock.minute = 0
        my_clock.hour = my_clock.hour + 1
        print('hour',my_clock.hour)

    if my_clock.hour == 24:
        my_clock.hour = 0
        my_clock.day = my_clock.day + 1
        print('day',my_clock.day)

    if (my_clock.day == 31) and ((my_clock.month == 10) or (my_clock.month == 12)):
        my_clock.day = 0
        my_clock.month = my_clock.month + 1
        print('month',my_clock.month)
    elif (my_clock.day == 30) and (my_clock.month == 11):
        my_clock.day = 0
        my_clock.month = my_clock.month + 1
        print('month',my_clock.month)

    return str(my_clock.month)+'/'+str(my_clock.day)+'/'+str(my_clock.year)+' '+str(my_clock.hour)+':'+str(my_clock.minute)


def read_modify_csv():
    with open(old_file_name+file_extention) as old_file:
        old_file_object = csv.reader(old_file, delimiter=',')
        add_row=['timestamp','value']
        with open(old_file_name + '_truncated_avg' + file_extention,'wb') as new_file:
            new_file_object = csv.writer(new_file, delimiter=',')
            new_file_object.writerow(add_row)

            time = '10/1/2015 0:00'
            tick = 0
            sum_data_7200_sample = 0
            for row in old_file_object:
                if 'timestamp' not in row:
                    time = my_clock()
                    tick = tick + 1
                    #print(tick)
                    sum_data_7200_sample = sum_data_7200_sample + float(row[1])
                    if tick == 7200: #1 minute
                        tick = 0
                        add_row = [time, str(sum_data_7200_sample/7200)]
                        new_file_object.writerow(add_row)
                        sum_data_7200_sample = 0
                    #print(row)
                #    time = my_clock()

                    #print(time)

                    #row_number = row_number + 1
                    #if row_number >10000:
                    #    break
    #with open(old_file_name + '_new' + file_extention,'r') as new_file:
    #    new_file_object = csv.reader(new_file, delimiter=',')
    #    for row in new_file_object:
    #        print(row)

    """
    with open(old_file_name + '_new' + file_extention,'r') as new_file:
        new_file_object = csv.reader(new_file)
        for row in new_file_object:
            print'data {} = {}'.format(row[0], row[1])
    """




def main():
    read_modify_csv()
#    for i in range(7000000):
#        time = my_clock()
#    print (time)


if __name__=='__main__':
    main()
