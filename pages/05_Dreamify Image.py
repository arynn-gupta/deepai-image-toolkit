import streamlit as st
from lib.utils import styling, render_content

def main():
    styling()
        
    st.title("Dreamify Image")
    st.markdown(
        "Exaggerates feature attributes or textures using information that the bvlc_googlenet model learned during training."
    )
    render_content(style="Dreamified")

if __name__ == '__main__':
    main()