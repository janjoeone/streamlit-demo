import streamlit as st

if 'username' in st.session_state:
    st.write(st.session_state.username)