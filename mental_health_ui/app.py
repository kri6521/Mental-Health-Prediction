import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model and preprocessing objects
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')
poly = joblib.load('poly.pkl')

st.title("🧠 Self-Analysis Mental Health Prediction")
st.markdown("---")

# User Inputs
age = st.number_input('🔢 Age', min_value=18, max_value=100, value=44)
work_interfere = st.selectbox('💼 Work interference', ['None', 'Mild', 'Moderate', 'High'], index=2)
family_history = st.selectbox('👪 Family history of mental health', ['No', 'Yes'], index=0)
mental_health_consequence = st.selectbox('🧠 Mental health consequence', ['None', 'Moderate', 'High'], index=1)
seek_help = st.selectbox('🔍 Seek help tendency', ['No', 'Yes'], index=0)
gender = st.selectbox('⚥ Gender', ['Male', 'Female'], index=0)
mental_health_interview = st.selectbox('🗣️ Mental health interview willingness', ['No', 'Maybe', 'Yes'], index=1)
mental_vs_physical = st.selectbox('⚕️ Mental vs Physical health importance', ['Physical is prioritized', 'Equal importance'], index=0)
no_employees = st.slider('👨‍💼 Number of employees', 1, 1000, 5)
remote_work = st.selectbox('🏡 Remote work preference', ['No', 'Yes'], index=0)

# Convert categorical inputs to numerical values
work_interfere_map = {'None': 0, 'Mild': 1, 'Moderate': 2, 'High': 3}
family_history_map = {'No': 0, 'Yes': 1}
mental_health_consequence_map = {'None': 0, 'Moderate': 1, 'High': 2}
seek_help_map = {'No': 0, 'Yes': 1}
gender_map = {'Male': 0, 'Female': 1}
mental_health_interview_map = {'No': 0, 'Maybe': 1, 'Yes': 2}
mental_vs_physical_map = {'Physical is prioritized': 0, 'Equal importance': 1}
remote_work_map = {'No': 0, 'Yes': 1}

new_data = pd.DataFrame([{
    'Age': age,
    'work_interfere': work_interfere_map[work_interfere],
    'family_history': family_history_map[family_history],
    'mental_health_consequence': mental_health_consequence_map[mental_health_consequence],
    'seek_help': seek_help_map[seek_help],
    'Gender': gender_map[gender],
    'mental_health_interview': mental_health_interview_map[mental_health_interview],
    'mental_vs_physical': mental_vs_physical_map[mental_vs_physical],
    'no_employees': no_employees,
    'remote_work': remote_work_map[remote_work]
}])

# Scale the input data
numerical_features = ['Age', 'work_interfere', 'family_history',
                     'mental_health_consequence', 'seek_help', 'Gender',
                     'mental_health_interview', 'mental_vs_physical',
                     'no_employees', 'remote_work']

new_data[numerical_features] = scaler.transform(new_data[numerical_features])

# Ensure correct feature order before applying PolynomialFeatures
expected_columns = poly.feature_names_in_
for col in expected_columns:
    if col not in new_data:
        new_data[col] = 0

new_data = new_data[expected_columns]
new_data_poly = poly.transform(new_data)

# Make a prediction and get confidence score
prediction = model.predict(new_data_poly)
confidence = np.max(model.predict_proba(new_data_poly)) * 100  # Simulated confidence level

# Map prediction to condition
condition_map = {0: "No Mental Health Condition", 1: "Generalized Anxiety Disorder", 2: "Depression"}
predicted_condition = condition_map.get(prediction[0], "Unknown Condition")

# Define contributing factors
contributing_factors = []
if work_interfere == "High":
    contributing_factors.append("Work interference: High")
if family_history == "Yes":
    contributing_factors.append("Family history: Moderate")
if mental_health_consequence == "Moderate" or mental_health_consequence == "High":
    contributing_factors.append("Mental health consequence: " + mental_health_consequence)

# Define coping strategies based on condition
coping_strategies = {
    "No Mental Health Condition": [
        "Maintain a balanced work-life routine ✅",
        "Engage in social activities 👥",
        "Exercise regularly 🏃‍♂️"
    ],
    "Generalized Anxiety Disorder": [
        "Try relaxation techniques (meditation, breathing exercises) 🧘",
        "Establish a fixed sleep schedule 🛏️",
        "Engage in social activities 👥"
    ],
    "Depression": [
        "Seek support from a professional therapist 💬",
        "Engage in physical activities like walking 🚶‍♂️",
        "Maintain a structured daily routine 📅"
    ]
}

# Display results
st.markdown("### 🧠 Self-Analysis Mental Health Prediction")
st.markdown("---")
st.write(f"✅ **Predicted Condition:** {predicted_condition}")
st.write(f"📊 **Confidence Level:** {confidence:.1f}%")
st.markdown("---")

if contributing_factors:
    st.markdown("🔍 **Key Contributing Factors:**")
    for factor in contributing_factors:
        st.write(f"   - {factor}")
st.markdown("---")

st.markdown("💡 **Suggested Coping Strategies:**")
for strategy in coping_strategies[predicted_condition]:
    st.write(f"   - {strategy}")
