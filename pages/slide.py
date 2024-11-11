import streamlit as st

# 滑块
number = st.slider('Pick a number', 0, 100)

# 选择滑块
size = st.select_slider('Pick a size', ['S', 'M', 'L'])