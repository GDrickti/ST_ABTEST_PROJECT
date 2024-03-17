
import streamlit as st
from scipy.stats import norm

def ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level):
    # Calculate conversion rates and the difference
    control_rate = control_conversions / control_visitors
    treatment_rate = treatment_conversions / treatment_visitors
    rate_difference = treatment_rate - control_rate

    # Calculate the standard errors
    control_se = (control_rate * (1 - control_rate)) / control_visitors
    treatment_se = (treatment_rate * (1 - treatment_rate)) / treatment_visitors

    # Calculate the z-score
    z_score = rate_difference / ((control_se + treatment_se) ** 0.5)

    # Determine the confidence interval
    if confidence_level == 90:
        z_critical = norm.ppf(0.95)
    elif confidence_level == 95:
        z_critical = norm.ppf(0.975)
    elif confidence_level == 99:
        z_critical = norm.ppf(0.995)

    # Perform the hypothesis test
    if z_score > z_critical:
        return "Experiment Group is Better"
    elif z_score < -z_critical:
        return "Control Group is Better"
    else:
        return "Indeterminate"

# Streamlit app
st.title("AB Test Calculator")

control_visitors = st.number_input("Control Group Visitors", min_value=0, value=100)
control_conversions = st.number_input("Control Group Conversions", min_value=0, value=50)
treatment_visitors = st.number_input("Treatment Group Visitors", min_value=0, value=100)
treatment_conversions = st.number_input("Treatment Group Conversions", min_value=0, value=50)
confidence_level = st.selectbox("Confidence Level", [90, 95, 99])

if st.button("Perform AB Test"):
    result = ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level)
    st.write(f"Result: {result}")
