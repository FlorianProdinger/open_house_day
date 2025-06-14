import spidev
import time
spi = spidev.SpiDev()
spi.open( 0, 0 )
spi.max_speed_hz = 1350000

def read_channel(data):
    adc = spi.xfer( [ 1, (8+data) << 4 , 0] )
    data_ = ((adc[1] & 3 ) <<8 ) + adc[2]
    return data_


def read_data( ):
    channel_data_dic = {
            0 : [] ,
            1 : [] ,
            2 : [] ,
            }
    
    for x in range(50):
        for i  in range(3):
            channel_data_dic[i].append( read_channel(i) )
        time.sleep(0.05)

    return channel_data_dic 


if __name__ == "__main__":
    data_dic_temp = read_data()
    for channel, data_list in data_dic_temp.items():
        print(channel, sum(data_list) / len(data_list) )
    


