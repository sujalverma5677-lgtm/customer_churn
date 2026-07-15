import streamlit as st
import pandas as pd
import pickle
import pickle

model = pickle.load(open("model.pkl", "rb"))
st.title("Customer Churn Prediction")

st.write("Enter customer information below")
credit = st.number_input("Credit Score")

age = st.number_input("Age")

tenure = st.number_input("Tenure")

balance = st.number_input("Balance")

products = st.number_input("Number of Products")

salary = st.number_input("Estimated Salary")
if st.button("Predict"):

    data = pd.DataFrame({
        "CreditScore":[credit],
        "Age":[age],
        "Tenure":[tenure],
        "Balance":[balance],
        "NumOfProducts":[products],
        "EstimatedSalary":[salary]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer is likely to churn.")
    else:
        st.success("Customer is likely to stay.")
