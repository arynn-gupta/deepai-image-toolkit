import streamlit as st
from lib.utils import render_content, styling

def main():
    styling()
        
    st.title("Super Resolution")
    st.markdown(
        "Blurry images are unfortunately common and are a problem for professionals and hobbyists alike. Super Resolution uses machine learning to clarify, sharpen, and upscale the photo without losing its content and defining characteristics."
    )
    render_content(style="Increased Resolution", api="https://api.deepai.org/api/torch-srgan")

if __name__ == '__main__':
    main()