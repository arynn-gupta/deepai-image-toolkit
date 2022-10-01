import streamlit as st
from lib.utils import styling, render_dual_content

def main():
    styling()
        
    st.title("Compare Images")
    st.markdown(
        "It compares two images and returns a value that tells you how visually similar they are. The more the score, the more contextually similar the two images are with a score of '100' being identical."
    )
    render_dual_content(page="Compare Images")

if __name__ == '__main__':
    main()