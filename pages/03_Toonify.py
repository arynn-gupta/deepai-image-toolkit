import streamlit as st
from lib.utils import render_content, styling

def main():
    styling()
        
    st.title("Toonify")
    st.markdown(
        "Turn a photo of any face into a cartoon instantly with artificial intelligence. Toonify uses a convolutional neural network to quickly transform the photo into a cartoon."
    )
    render_content(style="Toonified", api="https://api.deepai.org/api/toonify")

if __name__ == '__main__':
    main()