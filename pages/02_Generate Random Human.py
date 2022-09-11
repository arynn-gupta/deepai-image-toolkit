import streamlit as st
from lib.utils import render_generator_btn, styling

def main():
    styling()
        
    st.title("Generate Random Human")
    st.markdown("Some Non Existent AI Generated Humans.")
    render_generator_btn(api="https://thispersondoesnotexist.com/image", label="Generate a Human")

if __name__ == '__main__':
    main()