import pandas
import streamlit as st
from send_email import send_email

st.header('Contact Me')

with st.form(key='email_form'):
    user_email = st.text_input('Your email address')

    df = pandas.read_csv('topics.csv')
    selection = st.selectbox("What topic do you want to discuss", df['topic'])

    raw_message = st.text_area('Your message here')

    message = f"Subject: New email from localhost\n" \
              f"\nFrom: {user_email} " \
              f"\nTopic: {selection}" \
              f"\n{raw_message}"
    submit_btn = st.form_submit_button('Send email')

    if submit_btn:
        send_email(message)
        st.info("Email sent")
