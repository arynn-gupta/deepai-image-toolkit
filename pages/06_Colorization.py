import streamlit as st
from lib.utils import styling, render_content

def main():
    styling()

    st.title("Colorization")
    st.markdown(
        "Colorize black and white images using the image colorization. Add color to old family photos and historic images, or bring an old film back to life with colorization."
    )
    render_content(style="Colorized")

if __name__ == '__main__':
    main()