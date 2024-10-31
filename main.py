import streamlit as st

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
