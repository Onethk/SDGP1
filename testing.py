import pickle
import numpy as np


with open('model_pickle_final.h5','rb') as f:
    mod =  pickle.load(f)
    
test = mod.predict([[3,0,0,1,1,2,1,1,1,3,1,4]])


print(test);    

