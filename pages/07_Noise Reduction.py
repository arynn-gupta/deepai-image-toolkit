import streamlit as st
from lib.utils import render_content, styling

def main():
    styling()
        
    st.title("Noise Reduction")
    st.markdown(
        "This tool upscales images while reducing noise within the image. It gets its name from the anime-style art known as 'waifu' that it was largely trained on."
    )
    render_content(style="Reduced Noise", api="https://api.deepai.org/api/waifu2x")

if __name__ == '__main__':
    main()