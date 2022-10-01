import streamlit as st
from lib.utils import styling, render_content

def main():
    styling()
        
    st.title("Nudity Detection")
    st.markdown("Detects the likelihood that an image contains nudity and should be considered NSFW.")
    render_content(style="Nudity Detection")

if __name__ == '__main__':
    main()