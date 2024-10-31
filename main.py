import streamlit as st
import pandas

st.set_page_config(layout='wide')


col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')


with col2:
    st.title('Mirko Ruhl')

    content = """Hi, my name is Mirko and I'm a python dev that loves to create things. I really like graphic design, I 
    have developed a lot of web and desktop apps using modern day graphics and themes, with technologies such as 
    bootstrap 5, css, tailwind, ttkbootstrap, tkinter and pysimple.   
    """
    st.info(content)


content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me
"""
st.write(content2)


col3, col4 = st.columns(2)
df = pandas.read_csv('data.csv', sep=';')
with col3:
    for index, row in df.iterrows():
        if index % 2 == 0:
            st.subheader(row['title'])
            st.write(row['description'])
            st.image(row['image'])

with col4:
    for index, row in df.iterrows():
        if index % 2 != 0:
            st.subheader(row['title'])
            st.write(row['description'])

