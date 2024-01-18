import json
import pickle
import numpy as np

# Global variables
__locations = None
__model = None
__data_columns = None


def get_estimated_price(locations, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(locations.lower())
        # Here we are finding the index of location from x columns and
        # storing in loc_index
    except:
        loc_index = -1

    arr = np.zeros(len(__data_columns))
    # initializes an array 'arr' with zeros, where the length of the array
    # is equal to the number of columns in the DataFrame x.
    arr[0] = sqft
    arr[1] = bath
    arr[2] = bhk
    if loc_index >= 0:
        arr[loc_index] = 1

    return round(__model.predict([arr])[0], 2)


# Create global variables and extract the related data and model from artifacts.
def load_saved_artifacts():
    print("Loading artifacts....")
    global __data_columns
    global __locations

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    if __model is None:
        with open('./artifacts/banglore_home_price_prediction_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("Loading done..")


# Function that will return locations.
def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    # Other locations.
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))