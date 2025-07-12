import streamlit as st
import pandas as pd
from datetime import datetime
import os

DATA_PATH = "data/intake_data.csv"
os.makedirs("data", exist_ok=True)

st.title("Hemovive - Anemia Intake Form")

with st.form("intake_form"):
    name = st.text_input("Full Name")
    age = st.number_input("Age", 0, 120, step=1)
    hb = st.number_input("Hemoglobin Level (g/dL)", 0.0, 25.0, step=0.1)
    pregnancy = st.radio("Pregnancy Status", ["Yes", "No"])
    ifa_status = st.selectbox("IFA Supplementation", ["Yes", "No", "Ongoing"])
    state = st.text_input("State")
    district = st.text_input("District")
    submit = st.form_submit_button("Submit")

    if submit:
        data = {
            "Timestamp": datetime.now().isoformat(),
            "Name": name,
            "Age": age,
            "Hemoglobin": hb,
            "Pregnancy": pregnancy,
            "IFA": ifa_status,
            "State": state,
            "District": district
        }
        df = pd.DataFrame([data])
        if os.path.exists(DATA_PATH):
            df.to_csv(DATA_PATH, mode='a', header=False, index=False)
        else:
            df.to_csv(DATA_PATH, index=False)
        st.success("Data submitted successfully!")

# Show latest entries
if os.path.exists(DATA_PATH):
    st.subheader("Last 5 Submissions")
    st.dataframe(pd.read_csv(DATA_PATH).tail(5))
