import spidev
import time
import pandas as pd
import numpy as np

spi = spidev.SpiDev()
spi.open( 0, 0 )
spi.max_speed_hz = 1350000

time_sleep = 0.05
data_points = 10

def read_channel(data):
    adc = spi.xfer( [ 1, (8+data) << 4 , 0] )
    data_ = ((adc[1] & 3 ) <<8 ) + adc[2]
    return data_


def read_data_full( mode="full"):
    channel_data_dic = {
            0 : [] ,
            1 : [] ,
            2 : [] ,
            }
    
    for x in range(data_points):
            for i  in range(3):
                channel_data_dic[i].append( read_channel(i) )
            time.sleep(time_sleep)
 
    
    if mode=="full":
        return channel_data_dic 
    
    elif mode=="normal":
        return pd.DataFrame(channel_data_dic).mean()
    else:
        print("please enter 'full', 'normal' or 'test")


def read_data():
    channel_data_dic = {
        'sensor_0': [],
        'sensor_1': [],
        'sensor_2': [],
    }
    
    for x in range(data_points):
        channel_data_dic['sensor_0'].append(read_channel(0))
        channel_data_dic['sensor_1'].append(read_channel(1))
        channel_data_dic['sensor_2'].append(read_channel(2))
        time.sleep(time_sleep)

    df = pd.DataFrame(channel_data_dic)
    return df.mean()

if __name__ == "__main__":
    data_dic_temp = read_data()
    for channel, data_list in data_dic_temp.items():
        print(channel, sum(data_list) / len(data_list) )
    


