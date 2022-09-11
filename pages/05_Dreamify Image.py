import streamlit as st
from lib.utils import render_content, styling

def main():
    styling()
        
    st.title("Dreamify Image")
    st.markdown(
        "Exaggerates feature attributes or textures using information that the bvlc_googlenet model learned during training."
    )
    render_content(style="Dreamified", api="https://api.deepai.org/api/deepdream")

if __name__ == '__main__':
    main()