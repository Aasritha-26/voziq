import streamlit as st

st.header("EMI Calculator")
p = st.number_input("Enter Principal: ")
r = st.number_input("Enter Rate: ")
t = st.number_input("Enter Time: ")


i = p*t*r/100
st.write(f"Interest is {i}")