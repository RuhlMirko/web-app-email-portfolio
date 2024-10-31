import streamlit as st

st.header('Contact Me')

with st.form(key='email_form'):
    user_email = st.text_input('Your email address')
    message = st.text_area('Your message here')

    submit_btn = st.form_submit_button()
    if submit_btn:

        st.write("Thank you for your cooperation")
