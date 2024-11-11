import streamlit as st

container = st.container()

if 'messages' not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input('Please input your question')
if prompt:
    st.session_state.messages.append(prompt)

with container:
    with st.chat_message('User'):
        for message in st.session_state.messages:
            st.write(message)