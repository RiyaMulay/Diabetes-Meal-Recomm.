import streamlit as st
import numpy as np
import joblib


def generate_recommendations(name,age, weight,height, activity_level, dietary_preferences):
    # Your recommendation logic goes here
    # Based on the inputs, generate meal recommendations
    recommendations = ["Breakfast: Oatmeal with fruits",
                       "Lunch: Grilled chicken salad",
                       "Dinner: Baked salmon with steamed vegetables"]
    return recommendations

def main():
    st.title("Diabetes Meal Recommendations")

    # User inputs
    name = st.text_input("Name")
    age = st.slider("Age", 18, 80, 30)
    weight = st.number_input("Weight (kg)", 40.0, 200.0, 70.0)
    height = st.number_input("Height (cm)", 155.0,170.0,160.0)
    activity_level = st.selectbox("Activity Level", ["Sedentary", "Moderately Active", "Active"])
    dietary_preferences = st.multiselect("Dietary Preferences", ["Low-carb", "Vegetarian", "Vegan"])

    # input hte data of user
    # Load the pre-trained model
    # model = joblib.load('C:\Users\riyam\Downloads\BE proj\Models\svc.pkl')
    model = joblib.load('svc.pkl')

    st.write("Enter the following details to predict:")

    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1, value=25.0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0.0, max_value=100.0, step=1.0, value=20.0)
    insulin = st.number_input("Insulin", min_value=0.0, max_value=1000.0, step=1.0, value=50.0)
    glucose = st.number_input("Glucose", min_value=50.0, max_value=300.0, step=1.0, value=100.0)
    blood_pressure = st.number_input("Blood Pressure", min_value=50.0, max_value=200.0, step=1.0, value=80.0)

    if st.button("Predict"):
        prediction = model.predict(np.array([[bmi, skin_thickness, insulin, glucose, blood_pressure]]))

        if  prediction == 0:
            st.write("The user is not diabetic")
        else:
            st.write("The user is diabetic")            

    # Generate recommendations
    recommendations = generate_recommendations(name,age, weight,height, activity_level,dietary_preferences)

    # Display recommendations
    st.header("Meal Recommendations")
    for i, recommendation in enumerate(recommendations):
        st.write(f"{i+1}. {recommendation}")
    

if __name__ == "__main__":
    main()

    



