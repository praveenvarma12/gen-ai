import streamlit as st
st.set_page_config(page_icon="♾️")
st.title("praveen",anchor=False)
st.subheader("AI developer | gamer")
with st.container(border=True):
    st.warning("i am a student.....")
col1,col2,col3=st.columns(3)
with col1:
   with st.expander(label="know me more",expanded=False):
        st.info("hi.....")
with col2:
    st.image("praveen.jpg")
with col3:
     with st.expander(label="know me more",expanded=False):
     st.warning("hello...")
        