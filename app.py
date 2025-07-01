import streamlit as st # type: ignore
import joblib # type: ignore
import pandas as pd # type: ignore

model= joblib.load('fraud_detection_model.pkl')
st.title("Fraud Detection Prediction")

st.write("Enter the transaction details below:")
amount = st.number_input("Transaction Amount", min_value=0.0, value=10000)

type = st.selectbox("Transaction Type", ["CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"])

oldbalanceOrg = st.number_input("Old Balance Original", min_value=0.0,value=10000)
newbalanceOrig = st.number_input("New Balance Original", min_value=0.0, value=1000)
oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0, value=10000)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0, value=10000)


if st.button("Predict"):
    input_data = pd.DataFrame({
        'amount': amount,
        'type': type,
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })
    
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.success("The transaction is likely to be fraudulent.")
    else:
        st.success("The transaction is likely to be legitimate.")
