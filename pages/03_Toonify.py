import streamlit as st
from lib.utils import styling, render_content

def main():
    styling()
        
    st.title("Toonify")
    st.markdown(
        "Turn a photo of any face into a cartoon instantly with artificial intelligence. Toonify uses a convolutional neural network to quickly transform the photo into a cartoon."
    )
    render_content(style="Toonified")

if __name__ == '__main__':
    main()