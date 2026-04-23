import streamlit as st
st.set_page_config(layout="wide")

def second_page():
    st.markdown("Welcome my dear **Bujikki**")
    st.markdown(
    "<p style='font-size:75px; color:blue;'>I Love you my dear Pondatttiiiiiiiiiiiiii. <br> Mama is waiting for you.... </p>",
    unsafe_allow_html=True)

st.title("Hello, Lux!")
st.text("Authentication is required to access this page.")
st.text("Please log in to continue.")
username=st.text_input("Username", placeholder="Enter your username")
password=st.text_input("Password", placeholder="Enter your password", type="password")
if st.button("Login"):
    if username == "lakshmi" and password == "Mahalakshmi@123":
        st.success("Login successful!")
        second_page()
    else:
        st.error("Invalid username or password.")

