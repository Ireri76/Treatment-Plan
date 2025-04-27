import streamlit as st
import numpy as np

# Dummy Q-table (replace with your trained Q-table)
q_table = np.random.rand(3, 3, 3, 3)  # Age x Comorbidity x Symptom x Action

# Define action labels
actions = ["Treatment A", "Treatment B", "Treatment C"]

# Sidebar: Input patient details
st.sidebar.title("Patient Profile")
age_group = st.sidebar.selectbox("Select Age Group", options=[0, 1, 2])
comorbidity = st.sidebar.selectbox("Select Comorbidity Level", options=[0, 1, 2])
symptom = st.sidebar.selectbox("Select Symptom Severity", options=[0, 1, 2])

# Main content
st.title("Treatment Recommendation System")
st.write("Using Q-learning to suggest personalized treatment based on patient profile.")

# Recommendation logic
if st.button("Recommend Treatment"):
    q_values = q_table[age_group, comorbidity, symptom]
    best_action = np.argmax(q_values)

    st.subheader("Recommended Treatment")
    st.success(f"{actions[best_action]}")

    st.subheader("Q-values for all actions")
    for i, val in enumerate(q_values):
        st.write(f"{actions[i]}: {val:.4f}")

# --- Footer ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #999999; font-size: 12px; padding-top: 10px;'>
        © Ireri Mugambi 2025. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)
