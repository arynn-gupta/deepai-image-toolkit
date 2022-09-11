import streamlit as st
from lib.utils import render_content, styling

def main():
    styling()

    st.title("Colorization")
    st.markdown(
        "Colorize black and white images using the image colorization. Add color to old family photos and historic images, or bring an old film back to life with colorization."
    )
    render_content(style="Colorized", api="https://api.deepai.org/api/colorizer")

if __name__ == '__main__':
    main()