import streamlit as st 
import pickle
import numpy as np

# load the model
model = pickle.load(open('model.pkl','rb'))

st.title("Heart Disease Prediction")
st.markdown("### Enter the necessry values")

with st.sidebar:
    st.header("Input features")
    age=st.slider("Age",1.0,80.0,step=.1)
    sex=st.slider("sex",0,1,step=1)
    cp=st.selectbox("CP",[0,1,2,3,4,5])
    trestbps = st.text_input("Resting Blood Pressure (trestbps)", placeholder="e.g., 120")
    chol=st.text_input("chol",placeholder="Enter")
    fbs=st.selectbox("Fbs",[0,1])
    restecg=st.slider("restecg",0,10,step=1)
    thalach=st.slider('thalach',1.0,80.0,step=1.0)
    exang=st.selectbox("exang",[0,1,2,3,4,5])
    oldpeak=st.slider("oldpeak",1.0,10.0,step=.1)
    slope = st.selectbox("Slope of Peak Exercise ST Segment (slope)", [0, 1, 2])
    ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (ca)", [0, 1, 2, 3, 4])
    thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])
    
    submit= st.button("prediction")
    
    if submit:
        try:
            feature=[[age,sex,cp,int(trestbps) if chol else 0,int(chol) if chol else 0,fbs,
                      restecg,thalach,exang,oldpeak,slope,ca,thal]]
            prediction = model.predict(feature)
            result = "Yes" if prediction[0] == 1 else "No Disease"
            st.markdown({result})
        except Exception as e:
            st.error(f"Error is {e}")