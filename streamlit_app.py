import streamlit as st

st.markdown("""
<style>
div.stButton > button {
    width: 100%;
    height: 160px;
    font-size: 40px;
    border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)

if st.button("Just a little app"):
    st.video("https://www.youtube.com/watch?v=xvFZjo5PgG0", start_time=0)
