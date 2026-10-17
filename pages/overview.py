
import streamlit as st

st.title("Bussiness Command centre")
st.caption("Customer Intelligence & Loyalty Operations Platform.")

st.divider()

st.subheader("Bussiness Overview")
col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.container(border=True):
        st.metric("Total customer", "--")
        st.caption("Registered Customers")

with col2:
    with st.container(border=True):
        st.metric("Total Transaction", "--")
        st.caption("Recorder Transactions")

with col3:
    with st.container(border=True):
        st.metric("Gross sale", "--")
        st.caption("Sales Before Adjustment")

with col4:
    with st.container(border=True):
        st.metric("Point Issued", "--")
        st.caption("Loyalty point awarded")

st.divider()

left_col, right_col = st.columns([2,1])

with left_col:
    st.subheader("Bussiness Activites")
    st.info("transaction activity will appear here once transaction data is available")

with right_col:
    st.subheader("Customers Segments")
    st.info("Customer segments will appear here once customer data is available")

st.divider()
st.subheader("Data Quality & System Alerts")
st.info("Data validation alerts will appear here once the data validation system is implemented.")
