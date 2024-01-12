# util.py will contain the function called get_location_name.
# get_location_name function will read the file columns.json and it will
# return the names of the locations.
import json
import pickle
import numpy as np

# Creating 3 variables.
__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, BHK, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = BHK
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


# Routine 1
def get_location_names():
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts....")
    global __data_columns  # Setting the variable as global variable.
    global __locations

    with open("artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)["data_columns"]  # Whatever object is loaded will be converted as dictionary.
        # Using python index slicing
        __locations = __data_columns[3:]  # Locations saved into __locations

    global __model
    with open("artifacts/banglore_home_price_prediction_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("Loading done...")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000,3,3))
    print(get_estimated_price('1st Phase JP Nagar',1000,2,2))