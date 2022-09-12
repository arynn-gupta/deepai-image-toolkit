import streamlit as st
from lib.utils import styling, stable_dffusion

def main():
    styling()
        
    st.title("Stable Diffusion")
    st.markdown(
        "Stable Diffusion is a state of the art text-to-image model that generates images from text. It uses AI to understand your words and convert them to a unique image each time. Like magic."
    )
    st.caption("For faster results use our Text to Image tool.")
    stable_dffusion(label="Describe your image")
    

if __name__ == '__main__':
    main()