import streamlit as st
from lib.utils import styling, stable_diffusion_api, handle_error

def main():
    styling()
        
    st.title("Stable Diffusion")
    st.markdown(
        "Stable Diffusion is a state of the art text-to-image model that generates images from text. It uses AI to understand your words and convert them to a unique image each time. Like magic."
    )
    st.caption("For faster results use our Text to Image tool.")
    with st.form("my_form"):
        prompt = st.text_area("Describe your image")   
        col1,col2 =st.columns(2)    
        samples = col1.number_input("Number of images", value=4)
        scale = col1.number_input("Guidance", value=7.5)
        steps = col2.number_input("Steps", value=45)
        seed = col2.number_input("Seed", value=1024)
        submitted = st.form_submit_button("Submit")
        if submitted:
            try:
                with st.spinner(""):
                        images_list = stable_diffusion_api(prompt, samples, scale, steps, seed)
                        for image in images_list:
                            st.image(image)
            except :
                handle_error()
    

if __name__ == '__main__':
    main()