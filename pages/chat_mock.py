import streamlit as st

# 聊天输入
prompt = st.chat_input('Say something')
if prompt:
    st.write(f'The user has sent: {prompt}')

# 聊天消息
import numpy as np
with st.chat_message('User'):
    st.write('Hello 🦒🦒🦒')
    st.line_chart(np.random.randn(30, 3))
with st.chat_message('AI'):
    st.write('I am an AI assistant👩‍🚀')