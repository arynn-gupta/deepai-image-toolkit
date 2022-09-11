import streamlit as st
from lib.utils import render_content, styling

def main():
    styling()
        
    st.title("Nudity Detection")
    st.markdown("Detects the likelihood that an image contains nudity and should be considered NSFW.")
    render_content(style="Nudity Detection", api="https://api.deepai.org/api/nsfw-detector")

if __name__ == '__main__':
    main()