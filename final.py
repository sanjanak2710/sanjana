import numpy as np
import streamlit as st
import joblib

model = joblib.load("final_model.pkl")

input_data=(63,1,3,145,233,1,0,150,0,2.3,0,0,1)

def heart_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person does not have a presence of heart disease'
    else:
      return 'The person does have a presence of heart disease'

def main():
    
    
    # giving a title
    st.title('Presence Of Heart Disease Prediction Web App')
    st.subheader('by Kuchipudi Sanjana ')

    st.sidebar.info("This web app is made as part of Presence Of Heart Disease Prediction Project")
    st.sidebar.info("Give all the information in beside coloumn")
    st.sidebar.info("Click on the 'Predict' button to check whether there is a presence of heart disease ")
    st.sidebar.info("Have A Nice Day")

    # getting the input data from the user
    
    
    age = st.text_input('Age') #1
    sex = st.selectbox("Sex",["Male","Female"])#2
    if sex=="Male":
        sex=1
    else:
        sex=0
    cp=st.selectbox("chest pain type \n-- Value 0: typical angina \n-- Value 1: atypical angina\n-- Value 2: non-anginal pain\n-- Value 3: asymptomatic",[0,1,2,3])              #3
    resting_bp=st.text_input('resting bp')  #4
    sc=st.text_input("serum cholestoral in mg/dl")   #5
    fbs=st.selectbox("fasting blood sugar above 130 ",[True,False])#6
    if fbs==True:
        fbs=1
    else:
        fbs=0
    rer=st.selectbox("resting electrocardiographic results",[0,1,2]) #7
    mhr=st.text_input("maximum heart rate achieved")  #8
    eia=st.selectbox("exercise induced angina type ",["yes","no"])    #9
    if eia=="yes":
        eia=1
    else:
        eia=0
    oldpeak = st.text_input("old peak")   #10
    slope=st.selectbox("slope -- Value 0: upsloping -- Value 1: flat -- Value 2: downsloping",[0,1,2])  #11
    ca=st.selectbox("number of major vessels  values - 0 to 4",[0,1,2,3,4])#12
    thal=st.selectbox("thal values 0 to 3",[0,1,2,3])
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Predict'):
        diagnosis = heart_prediction([age,sex,cp,resting_bp,sc,fbs,rer,mhr,eia,oldpeak,slope,ca,thal])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()