from read_sensor import read_data
from datetime import datetime as dt
import sys
import pickle
import os

# reading out user commands
user_input = sys.argv[1:]
store_data = False
if len(user_input) == 0:
    raise ExceptionType("pleae enter what a sample name.")
elif len(user_input) == 2:    
    store_data = True
    print("data will be stored")


# generate some data
data_ = read_data()
sample_name_ = user_input[0]
time_ = dt.now().strftime("%Y%m%d_%H%M%S")


# check if previous measurements were made
db_name = "data.pickle"
if os.path.exists( db_name ):
    print("loading previous data")
    with open( db_name , "rb" ) as f:
        data_stored = pickle.load( f )
else:
    print("making new database")
    data_stored = {}


# adding new data
data_stored[ time_ + "_" + sample_name_ ] = data_

# plot something or whatever
print(data_stored)


# add new data
if store_data == True:
   with open( db_name , 'wb') as f:
       pickle.dump( data_stored , f) 
