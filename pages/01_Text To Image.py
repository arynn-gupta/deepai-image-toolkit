import streamlit as st
from lib.utils import styling, text_to_image_api, handle_error

def main():
    styling()
        
    st.title("Text To Image")
    st.markdown(
        "This is an AI image Generator. It creates an image from scratch from a text description. It is much faster than Stable difussion but compromises with image quality."
    )
    with st.form("my_form"):
        prompt = st.text_area("Describe your image")
        submitted = st.form_submit_button("Submit")
        if submitted:
            try:
                with st.spinner(""):
                    resp = text_to_image_api(prompt)
                    st.image(resp, use_column_width=True)
            except :
                handle_error()

if __name__ == '__main__':
    main()