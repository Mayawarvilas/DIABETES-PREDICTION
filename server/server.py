from unittest import result
from flask import Flask,jsonify,request
from flask_cors import CORS

import util

app=Flask(__name__)
CORS(app)

@app.route('/hello')
def hello_world():
    return "Hello, World!"

@app.route('/get_data_columns')
def get_data_columns():
    response=jsonify(
        {
            'data_columns': util.get_data_columns()
        }
    )
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_diabetes',methods=['POST'])
def predict_diabetes():
    try:
        gender=float(request.form['gender'])
        age=float(request.form['age'])
        hypertension=float(request.form['hypertension'])
        heart_disease=float(request.form['heart_disease'])
        smoking_history=float(request.form['smoking_history'])
        bmi=float(request.form['bmi'])
        hba1c_level=float(request.form['hba1c_level'])
        blood_glucose_level=float(request.form['blood_glucose_level'])

        prediction=util.diabetes_prediction(gender,age,hypertension,heart_disease,smoking_history,bmi,hba1c_level,blood_glucose_level)

        if prediction == 1.0:
            prediction= "The Person Is Diabetic"
        else:
            prediction= "The Person Is Not Diabetic"
            
        response=jsonify({
            'prediction': prediction
        })

        response.headers.add('Access-Control-Allow-Origin','*')

        return response
    
    except Exception as e:
        return jsonify({'error':str(e)})
    except ValueError as v:
        return jsonify({'error':str(v)})
    except KeyError as k:
        return jsonify({'error':str(k)})

if __name__=='__main__':
    print('starting server')
    util.load_saved_artifacts()
    app.run()