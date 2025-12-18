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

if st.button("Enjoy"):
    st.markdown("""
    <iframe
        width="100%"
        height="450"
        src="https://www.youtube.com/embed/xvFZjo5PgG0?autoplay=1"
        frameborder="0"
        allow="autoplay; encrypted-media"
        allowfullscreen>
    </iframe>
    """, unsafe_allow_html=True)
