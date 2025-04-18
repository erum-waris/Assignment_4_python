import streamlit as st # type: ignore

st.title("Simple BMI Calculator")

# Get height input (in meters)
height_m = st.number_input(
    "Enter your height (in meters):",
    min_value=0.1,
    max_value=3.0,
    step=0.01,
    value=1.7  # Default as float
)

# Get weight input (in kilograms)
weight_kg = st.number_input(
    "Enter your weight (in kilograms):",
    min_value=10.0,
    max_value=300.0,
    step=0.1,
    value=70.0  # Default as float
)

def calculate_bmi(height, weight):
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        return "Cannot calculate BMI with zero height."

def interpret_bmi(bmi):
    if isinstance(bmi, str):
        return bmi
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Healthy weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

if st.button("Calculate BMI"):
    bmi_result = calculate_bmi(height_m, weight_kg)
    st.subheader(f"Your BMI is: {bmi_result:.2f}")
    interpretation = interpret_bmi(bmi_result)
    st.write(f"Interpretation: {interpretation}")