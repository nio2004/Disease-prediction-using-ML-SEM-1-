from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from joblib import load

model = load('./livermodel.joblib')
cmodel = load('./cardiomodel.joblib')

def home(request):
    return render(request,'home.html')

def ieee(request):
    return render(request,'ieee.html')

def calculator(request):
    
    return render(request,'calculator.html')

def cardiovascular(request):
    
     return render(request,'cardiovascular.html')

def calc_result(request):

    age = request.GET['AGE']
    Gender = request.GET['Gender']
    Total_Bilirubin = request.GET['Total_Bilirubin']
    Direct_Bilirubin = request.GET['Direct_Bilirubin']
    Alkaline_Phosphotase = request.GET['Alkaline_Phosphotase']
    Alamine_Aminotransferase = request.GET['Alamine_Aminotransferase']
    Aspartate_Aminotransferase = request.GET['Aspartate_Aminotransferase']
    Total_Protiens = request.GET['Total_Protiens']
    Albumin = request.GET['Albumin']
    Albumin_and_Globulin_Ratio = request.GET['Albumin_and_Globulin_Ratio']

    print("prediction is:1")
    ypred = model.predict([[age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])
    print("prediction is:1")
    if ypred[0] == 1:
        ypred='have'
    elif ypred[0] == 2:
        ypred='dont have'

    return render(request,'calc_result.html', {'calc_result':ypred})

def cardio_result(request):

    Age = request.GET['Age']
    Gender = request.GET['Gender']
    Height = request.GET['Height']
    Weight = request.GET['Weight']
    Systolicbp = request.GET['Systolicbp']
    Diastolicbp = request.GET['Diastolicbp']
    Cholestrol = request.GET['Cholesterol']
    Glucose = request.GET['Glucose']
    Smoking = request.GET['Smoking']
    Alcohol = request.GET['Alcohol_intake']
    pa = request.GET['Physical_activity']
    

    #print("prediction is:1")
    ypred = cmodel.predict([[Age,Gender,Height,Weight,Systolicbp,Diastolicbp,Cholestrol,Glucose,Smoking,Alcohol,pa]])
    #print("prediction is:1")
    if ypred[0] == 1:
        ypred='have'
    elif ypred[0] == 0:
        ypred='dont have'

    return render(request,'cardio_result.html', {'cardio_result':ypred})
    