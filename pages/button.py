import streamlit as st

# 按钮（会刷新页面）
if st.button('Say hello'):
    st.write('hello')
else:
    st.write('bye')

# 下载按钮
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

# 链接按钮
st.link_button('Google', 'https://www.google.com')

# 页面链接
st.page_link('app.py', label='My Home', icon='🏠')
st.page_link('pages/profile.py', label='My Profile', icon='⚙')