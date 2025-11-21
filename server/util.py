import numpy as np
import json
import pickle

__data_columns=None
__model=None
__scaler=None

def diabetes_prediction(gender,age,hypertension,heart_disease,smoking_history,bmi,hba1c_level,blood_glucose_level):
            
    input_data=np.array([[gender,age,hypertension,heart_disease,smoking_history,bmi,hba1c_level,blood_glucose_level]])

    if __scaler is not None:
         input = __scaler.transform(input_data)

    prediction = __model.predict(input)
    return float(prediction[0])
             

def get_data_columns():
    return __data_columns

def load_saved_artifacts():
    print('Loading saves artifacts...start')
    global __data_columns
    global __model
    global __scaler

    with open('./artifactes/columns.json','r') as f:
        __data_columns=json.load(f)['data_columns']
    
    with open ('./artifactes/Diabetes_prediction.pickle','rb') as f:
        __model=pickle.load(f)

    with open('./artifactes/scaler.pickle','rb') as f:
        __scaler=pickle.load(f)

    print('Loading saved artifacts...done')

if __name__=='__main__':
    load_saved_artifacts()
    print(get_data_columns())