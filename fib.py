import streamlit as st

st.title("Is Digit")

a = st.text_input(label="Enter the input (n)")

if st.button("Submit"):
    temp=True
    for i in a:
     if i.isalnum():
       temp=True
     else:
       temp=False
       st.write("no")
       break
    if temp :
      st.write("yes")
    