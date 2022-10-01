import streamlit as st
from lib.utils import styling, render_content

def main():
    styling()
        
    st.title("Noise Reduction")
    st.markdown(
        "This tool upscales images while reducing noise within the image. It gets its name from the anime-style art known as 'waifu' that it was largely trained on."
    )
    render_content(style="Reduced Noise")

if __name__ == '__main__':
    main()