import streamlit as st
from lib.utils import styling, render_dual_content

def main():
    styling()
        
    st.title("Style Transfer")
    st.markdown("Transfers the style from one image onto the content of another image.")
    render_dual_content(name1="Content", name2="Style", page="Style Transfer")

if __name__ == '__main__':
    main()