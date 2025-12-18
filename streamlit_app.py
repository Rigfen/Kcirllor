import streamlit as st

st.markdown("""
<style>
div.stButton > button {
    width: 100%;
    height: 120px;
    font-size: 32px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

if st.button("▶ WATCH VIDEO"):
    st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID")
