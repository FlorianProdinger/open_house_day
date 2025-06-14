
import spidev
import time
spi = spidev.SpiDev()
spi.open( 0, 0 )
spi.max_speed_hz = 1350000

def read_channel(data):
     adc = spi.xfer( [ 1, (8+data) << 4 , 0] )
     data_ = ((adc[1] & 3 ) <<8 ) + adc[2]
     return data_


while True:
  for i  in range(8):
   va = read_channel(i)
   print(f" channel {i} \t value: {va} ")
  time.sleep(1)




