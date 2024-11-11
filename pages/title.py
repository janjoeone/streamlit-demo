import streamlit as st

# 大标题
st.title('This is a title')

# 标题
st.header('This is a header')

# 代码块
st.code('a = 123')
st.code('print("Hello world")')

# 分隔符
st.divider()

# 数据元素
st.json({
    'name': 'Ray',
    'age': 30,
})