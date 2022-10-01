import streamlit as st
from lib.utils import styling, generate_random_human_api, handle_error

def main():
    styling()
        
    st.title("Generate Random Human")
    st.markdown("Some Non Existent AI Generated Humans.")
    with st.form("my_form"):
        submitted = st.form_submit_button("Generate a Human")
        if submitted:
            try:
                with st.spinner(""):
                    resp = generate_random_human_api()
                    st.image(resp, use_column_width=True)
            except:
                handle_error()

if __name__ == '__main__':
    main()