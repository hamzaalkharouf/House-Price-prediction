import pickle
import argparse
import numpy as np


#take model
#Calculate price from scikit
def path(list_data):
    parser = argparse.ArgumentParser()
    parser.add_argument("-path","--path",type = str)
    args = parser.parse_args()
    # './model.pickle'
    loaded_model = pickle.load(open(args.path, 'rb'))
    x = np.array(list_data).reshape(1,6)
    result = loaded_model.predict(x)
    if x.shape[0] == 1:
        result = result[0]
    return result
