import pandas
import streamlit as st
from send_email import send_email

st.header('Contact Me')

with st.form(key='email_form'):
    user_email = st.text_input('Your email address')

    df = pandas.read_csv('topics.csv')
    topics_list = []
    for index, row in df.iterrows():
        topics_list.append(row['topic'])
    selection = st.selectbox("What topic do you want to discuss", topics_list)

    raw_message = st.text_area('Your message here')

    message = f"Subject: New email from localhost\n\nFrom: {user_email} \nTopic: {selection}\n" + raw_message
    submit_btn = st.form_submit_button('Send email')

    if submit_btn:
        send_email(message)
        st.info("Email sent")
