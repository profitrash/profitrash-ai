
import streamlit as st

# Title of the app
st.title("ProfiTrash AI Demo")

# Description
st.write("This is a simple demo application for ProfiTrash AI. Please enter your message below and click the button to display it.")

# Text input form
message = st.text_input("Enter your message:")

# Button to display the message
if st.button("Display Message"):
    st.write(f"Your message: {message}")
