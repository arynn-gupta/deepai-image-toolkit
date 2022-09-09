import streamlit as st
import os
import requests

api_key = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"
resp = None


def save_uploadedfile(image_file, name="temp_image"):
    extension = "." + image_file.name.split(".")[-1]
    with open(os.path.join("temp", name + extension), "wb") as f:
        f.write(image_file.getbuffer())
    return 1


def render_download_btn(url, img_name):
    new_image = requests.get(url)
    extension = img_name.split(".")[-1]
    new_image_name = img_name
    new_image_path = os.path.join("temp", new_image_name)
    with open(new_image_path, "wb") as file:
        file.write(new_image.content)
    with open(new_image_path, "rb") as file:
        st.download_button(label="Download Image", data=file, file_name=new_image_name, mime="image/" + extension)


def render_content(api, page, style):
    image_file = st.file_uploader("", type=["png", "jpeg", "jpg"], key="page" + str(page) + "temp_image")
    if image_file is not None:
        save_uploadedfile(image_file)
        extension = "." + image_file.name.split(".")[-1]
        col1, col2 = st.columns(2)
        col1.header("Original")
        col1.image(image_file, use_column_width=True)
        col2.header(style)
        try:
            with col2:
                with st.spinner(""):
                    r = requests.post(
                        api,
                        files={"image": open("temp/" + "temp_image" + extension, "rb"),},
                        headers={"api-key": api_key},
                    )
                    resp = r.json()
                    st.image(resp["output_url"], use_column_width=True)
                    render_download_btn(resp["output_url"], style + "_" + image_file.name)
        except:
            st.write(resp)


def render_dual_content(api, page, name1="Image 1", name2="Image 2"):
    image_file_1 = st.file_uploader(name1, type=["png", "jpeg", "jpg"], key="page" + str(page) + "_temp_image_1")
    image_file_2 = st.file_uploader(name2, type=["png", "jpeg", "jpg"], key="page" + str(page) + "_temp_image_2")
    if image_file_1 is not None and image_file_2 is not None:
        save_uploadedfile(image_file_1, name="temp_image_1")
        save_uploadedfile(image_file_2, name="temp_image_2")
        extension1 = "." + image_file_1.name.split(".")[-1]
        extension2 = "." + image_file_2.name.split(".")[-1]
        col1, col2 = st.columns(2)
        col1.header(name1)
        col1.image(image_file_1, use_column_width=True)
        col2.header(name2)
        col2.image(image_file_2, use_column_width=True)
        try:
            with st.spinner(""):
                r = requests.post(
                    api,
                    files={
                        "image1": open("temp/" + "temp_image_1" + extension1, "rb"),
                        "image2": open("temp/" + "temp_image_2" + extension2, "rb"),
                    },
                    headers={"api-key": api_key},
                )
                resp = r.json()
                st.write(resp)
        except:
            st.write(resp)


def page1():
    st.markdown("# Deep AI Image Toolkit")
    st.markdown("")
    st.markdown("This is an A.I. image toolkit, that provides you with the following features :")


def page2():
    st.markdown("# Colorization")
    st.markdown(
        "`Colorize black and white images using the image colorization. Add color to old family photos and historic images, or bring an old film back to life with colorization.`"
    )
    render_content(style="Colorized", api="https://api.deepai.org/api/colorizer", page=2)


def page3():
    st.markdown("# Super Resolution")
    st.markdown(
        "`Blurry images are unfortunately common and are a problem for professionals and hobbyists alike. Super Resolution uses machine learning to clarify, sharpen, and upscale the photo without losing its content and defining characteristics.`"
    )
    render_content(style="Increased Resolution", api="https://api.deepai.org/api/torch-srgan", page=3)


def page4():
    st.markdown("# Text To Image")
    st.markdown(
        "`This is an AI image Generator. It creates an image from scratch from a text description. Text-to-image uses AI to understand your words and convert them to a unique image each time. Like magic.`"
    )
    with st.form("my_form"):
        prompt = st.text_area("Describe your image")
        submitted = st.form_submit_button("Submit")
        if submitted:
            try:
                with st.spinner(""):
                    r = requests.post(
                        "https://api.deepai.org/api/text2img", data={"text": prompt,}, headers={"api-key": api_key}
                    )
                    resp = r.json()
                    st.image(resp["output_url"], use_column_width=True)
                    render_download_btn(resp["output_url"], "Output.png")
            except:
                st.write(resp)


def page5():
    st.markdown("# Noise Reduction")
    st.markdown(
        "`This tool upscales images while reducing noise within the image. It gets its name from the anime-style art known as 'waifu' that it was largely trained on.`"
    )
    render_content(style="Reduced Noise", api="https://api.deepai.org/api/waifu2x", page=5)


def page6():
    st.markdown("# Toonify")
    st.markdown(
        "`Turn a photo of any face into a cartoon instantly with artificial intelligence. Toonify uses a convolutional neural network to quickly transform the photo into a cartoon.`"
    )
    render_content(style="Toonified", api="https://api.deepai.org/api/toonify", page=6)


def page7():
    st.markdown("# Nudity Detection")
    st.markdown("`Detects the likelihood that an image contains nudity and should be considered NSFW.`")
    render_content(style="Nudity Detection", api="https://api.deepai.org/api/nsfw-detector", page=7)


def page8():
    st.markdown("# Compare Images")
    st.markdown(
        "`It compares two images and returns a value that tells you how visually similar they are. The lower the the score, the more contextually similar the two images are with a score of '0' being identical.`"
    )
    render_dual_content(api="https://api.deepai.org/api/image-similarity", page=8)


def page9():
    st.markdown("# Dreamify Image")
    st.markdown(
        "`Exaggerates feature attributes or textures using information that the bvlc_googlenet model learned during training.`"
    )
    render_content(style="Dreamified", api="https://api.deepai.org/api/deepdream", page=9)


def page10():
    st.markdown("# Style Transfer")
    st.markdown("`Transfers the style from one image onto the content of another image.`")
    render_dual_content(
        name1="Ordinary Image", name2="Styled Image", api="https://api.deepai.org/api/neural-style", page=10
    )


def page11():
    st.markdown("# Fast Style Transfer")
    st.markdown("`Transfers the style from one image onto the content of another image.`")
    render_dual_content(
        name1="Ordinary Image", name2="Styled Image", api="https://api.deepai.org/api/fast-style-transfer", page=11
    )


def page12():
    st.markdown("# CNNMRF Style Transfer")
    st.markdown("`Transfers the style from one image onto the content of another image.`")
    render_dual_content(name1="Ordinary Image", name2="Styled Image", api="https://api.deepai.org/api/CNNMRF", page=12)


def page13():
    st.markdown("# Content Moderation")
    st.markdown(
        "`This tool analyzes images and videos to detect the presence of adult content, hate symbols, guns, and offensive words found amongst text within images.`"
    )
    render_content(style="Moderated Image", api="https://api.deepai.org/api/content-moderation", page=13)


# Styling
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def changePage(name):
    resp = None
    st.session_state["page_name"] = name
    page_names_to_funcs[name]()


page_names_to_funcs = {
    "page1": page1,
    "page2": page2,
    "page3": page3,
    "page4": page4,
    "page5": page5,
    "page6": page6,
    "page7": page7,
    "page8": page8,
    "page9": page9,
    "page10": page10,
    "page11": page11,
    "page12": page12,
    "page13": page13,
}

button1 = st.sidebar.button("About")
button2 = st.sidebar.button("Colorization")
button3 = st.sidebar.button("Super Resolution")
button4 = st.sidebar.button("Text To Image")
button5 = st.sidebar.button("Noise Reduction")
button6 = st.sidebar.button("Toonify")
button7 = st.sidebar.button("Nudity Detection")
button8 = st.sidebar.button("Compare Images")
button9 = st.sidebar.button("Dreamify Image")
button10 = st.sidebar.button("Style Transfer")
button11 = st.sidebar.button("Fast Style Transfer")
button12 = st.sidebar.button("CNNMRF Style Transfer")
button13 = st.sidebar.button("Content Moderation")
if button1:
    changePage("page1")
elif button2:
    changePage("page2")
elif button3:
    changePage("page3")
elif button4:
    changePage("page4")
elif button5:
    changePage("page5")
elif button6:
    changePage("page6")
elif button7:
    changePage("page7")
elif button8:
    changePage("page8")
elif button9:
    changePage("page9")
elif button10:
    changePage("page10")
elif button11:
    changePage("page11")
elif button12:
    changePage("page12")
elif button13:
    changePage("page13")
else:
    try:
        page_names_to_funcs[st.session_state.page_name]()
    except:
        page_names_to_funcs["page1"]()
