import streamlit as st
from lib.utils import render_form, styling

def main():
    styling()
        
    st.title("Text To Image")
    st.markdown(
        "This is an AI image Generator. It creates an image from scratch from a text description. Text-to-image uses AI to understand your words and convert them to a unique image each time. Like magic."
    )
    render_form(api="https://api.deepai.org/api/text2img", label="Describe your image")

if __name__ == '__main__':
    main()