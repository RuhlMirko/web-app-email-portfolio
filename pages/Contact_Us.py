import streamlit as st
from send_email import send_email

st.header('Contact Me')

with st.form(key='email_form'):
    user_email = st.text_input('Your email address')
    raw_message = st.text_area('Your message here')
    message = f"""\
    Subject: New Email from {user_email}
    From: {user_email}\n    
    {raw_message}
    """
    submit_btn = st.form_submit_button('Send email')

    if submit_btn:
        st.write(raw_message)
        st.write(message)

        send_email(message)
        st.info("Email sent")
