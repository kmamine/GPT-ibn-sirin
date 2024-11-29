import streamlit as st
import requests

st.title("Dream Interpreter")

dream_description = st.text_area("Describe your dream:")

if st.button("Interpret"):
    if dream_description:
        response = requests.post('http://localhost:5000/interpret-dream', json={'dream_description': dream_description})
        
        if response.status_code == 200:
            data = response.json()
            st.subheader("Interpretation:")
            st.write(data['interpretation'])
            st.subheader("Additional Insights:")
            st.write(data['details'])
        else:
            st.error(response.json().get('error', 'An error occurred.'))
    else:
        st.error("Please enter a dream description.")