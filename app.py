import streamlit as st
from cal import *

st.header('Calculator')
st.write("This is the app for calculator")
a = st.number_input('Enter first number: ')
b = st.number_input('Enter second number: ')
op = st.selectbox("Operator", ['+','-','*','/','%', '**'])

submit = st.button('Answer')
if submit:
    if op == '+':
        res = add(a, b)
    elif op == '-':
        res = sub(a, b) 
    elif op == '*':
        res = mul(a, b)
    elif op == '/':
        res = div(a, b)
    elif op == '%': 
        res = mod(a, b)
    elif op == '**': 
        res = power(a, b)

    st.write(f"Result: {res}")