function get_gender_value(){
    var gender=document.getElementById('gender').value;
    return gender;
}

function get_age_value(){
    var age=document.getElementById('age').value;
    return age;
}

function get_hypertension_value(){
    var hypertension=document.getElementById('hypertension').value;
    return hypertension;
}

function get_heart_disease_value(){
    var heart_disease=document.getElementById('heart_disease').value;
    return heart_disease;
}

function get_smoking_history_value(){
    var smoking_history=document.getElementById('smoking_history').value;
    return smoking_history;
}

function get_bmi_value(){
    var bmi=document.getElementById('bmi').value;
    return bmi;
}

function get_hemoglobin_value(){
    var hemoglobin=document.getElementById('HbA1c_level').value;
    return hemoglobin;
}

function get_blood_glucose_value(){
    var blood_glucose=document.getElementById('blood_glucose_level').value;
    return blood_glucose;
}


function onClickedPredict(){
    var gender=get_gender_value()
    var age=get_age_value()
    var hypertension=get_hypertension_value()
    var heart_disease=get_heart_disease_value()
    var smoking_history=get_smoking_history_value()
    var bmi=get_bmi_value()
    var hba1c_level=get_hemoglobin_value()
    var blood_glucose_level=get_blood_glucose_value()

    var result=document.getElementById('uipredict')

    var url='http://127.0.0.1:5000/predict_diabetes'

    $.post(url,{
        gender: gender,
        age: age,
        hypertension: hypertension, 
        heart_disease: heart_disease,
        smoking_history: smoking_history,
        bmi:bmi,
        hba1c_level:hba1c_level,
        blood_glucose_level:blood_glucose_level
    },function(data,status){
        console.log({gender,age});
        console.log(data.prediction);
        result.innerHTML="<h3>"+data.prediction+"</h3>";
        console.log(status);
    })
    
}

