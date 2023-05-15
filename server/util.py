import json
import pickle
import numpy as np
import sklearn

__locations = None
__data_columns = None
__model = None

def predict_price(bedroom,bathrooms,area,floor_number,Furnished,Semifurnished,c0_to_1_Year_Old, c1_to_5_Year_Old, c10_Year_Old, address):    
    try:
        loc_index = __data_columns.index(address.lower())
    except:
        loc_index = -1                    #so if all address bits becomes 0, it will be classified as 'other'

    x = np.zeros(len(__data_columns))
    x[0] = bedroom
    x[1] = bathrooms
    x[2] = area
    x[3] = floor_number
    x[4] = Furnished
    x[5] = Semifurnished
    x[6] = c0_to_1_Year_Old
    x[7] = c1_to_5_Year_Old
    x[8] = c10_Year_Old
    
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2) #rounding result float number to 2 decimals

def load_artifacts():
    print("Loading saved artifacts...")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[9:]

    global __model
    with open("./artifacts/model1.pickle", 'rb') as f:
        __model = pickle.load(f)

def get_locations():
    load_artifacts()
    return __locations


if __name__ == '__main__':
    load_artifacts()
    print(get_locations())

    print(predict_price(2,2,1450,3,0,0,0,0,0,0,0,1,'Aundh'))
    print(predict_price(1,1,650,4,1,1,0,1,0,0,0,1,'Wakad'))
    print(predict_price(1,1,650,4,1,1,0,1,0,0,0,1,'Wakd'))


