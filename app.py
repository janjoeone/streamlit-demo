import streamlit as st
import pandas as pd
import numpy as np
import time

st.write('hello world')
"I am Ray"

# 单行文本输入
username = st.text_input('What is your name?')
st.session_state['username'] = username

# 数字输入
choice = st.number_input('Pick a number', 0, 10)

# 多行文本输入
text = st.text_area('Text to translate')

# 日期输入
time_input = st.time_input('Meeting Time')
date_input = st.date_input('Meeting Date')

# 文件上传器
data = st.file_uploader('Upload File')
st.write(data)

# 侧边栏
st.sidebar.write('This lives in the sidebar')
st.sidebar.button('Click Me!')

# 列
col1, col2 = st.columns(2)
col1.write('this is column 1')
col2.write('this is column 2')

# 标签页
tab1, tab2 = st.tabs(['Tab1', 'Tab2'])
tab1.write('this is tab 1')
tab2.write('this is tab 2')

# 扩展器
with st.expander('Open to see more'):
    st.write('This is more info')

# 容器
c = st.container()
st.write('This will show last')
c.write('This will show first')
c.write('This will show second')

# 自动跳转
# st.switch_page('pages/chat_mock.py')

with st.echo():
    st.write('This code will be printed')

st.help(st.write)

if st.button('Say hello'):
    st.write('hello')
    st.session_state['clicked'] = True

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.write(chart_data)

def my_generator():
    for i in range(10):
        yield f'{i}'
        time.sleep(0.5)
st.write_stream(my_generator())