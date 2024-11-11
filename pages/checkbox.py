import streamlit as st

# 复选框（会刷新页面）
selected = st.checkbox('I agree')

# 单选框
choice = st.radio('Pick one', ['Apple', 'Orange', 'Banana'])
st.write(f'Your choice is {choice}')

single_choice = st.selectbox('Your favorite animal', ['Cat', 'Dog'])
st.write(f'Your single choice is {single_choice}')

multi_choice = st.multiselect('Your hobby', ['Swimming', 'Basketball', 'Football', 'Running'])
st.write(f'Your multi choice is {multi_choice}')

# 切换开关
activated = st.toggle('Activate')
st.write(f'Activated: {activated}')