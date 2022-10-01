import streamlit as st
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
os.environ["HF_TOKEN"] = "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"

import requests
import random
import torch
from torch import autocast
import torchvision
from torchvision.io import read_image
from torchvision.utils import draw_bounding_boxes
from icons import *
from diffusers import StableDiffusionPipeline
from  PIL import Image
from rembg import remove

headers = {
    "api-key" : "quickstart-QUdJIGlzIGNvbWluZy4uLi4K",
    "X-Forwarded-For": ".".join(str(random.randint(0, 255)) for _ in range(4))
}

style='''
div.css-1gk2i2l.e17lx80j0 {
  width: 100%;
  height: 250px;
  display: flex;
  align-items: center;
  justify-content: center;
}

h1 span {
  color: #893aff;
}

h3 span {
  color: #06b48b;
}

li path {
  display: none;
}

li {
  padding: none;
}

li span {
  width: 100%;
  margin-right: 1.2rem;
  margin-bottom: 0.5rem;
  padding: 0.5rem 2rem;
  color: #b4b6be;
  border-radius: 0.5rem;
}

li span:before{
    margin-right: 8px; position: relative;  top: 2px; 
}

li span:hover {
  color: white;
  background-color: #313334;
}

a {
  background: none !important;
}

a.css-1m59598.e1fqkh3o6 span{
  color: white;
  background-color: #313334;
}
'''

def styling():
    st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)
    st.markdown('''<style>
        li:nth-child(1) span:before {  content: '''+info+'''; }
        li:nth-child(2) span:before {  content: '''+chat+'''; }
        li:nth-child(3) span:before {  content: '''+robot+'''; }
        li:nth-child(4) span:before {  content: '''+person+'''; }
        li:nth-child(5) span:before {  content: '''+emoji+'''; }
        li:nth-child(6) span:before {  content: '''+shuffle+'''; }
        li:nth-child(7) span:before {  content: '''+drizzle+'''; }
        li:nth-child(8) span:before {  content: '''+palette+'''; }
        li:nth-child(9) span:before {  content: '''+card_image+'''; }
        li:nth-child(10) span:before {  content: '''+badge_4k+'''; }
        li:nth-child(11) span:before {  content: '''+yin_yang+'''; }
        li:nth-child(12) span:before {  content: '''+person_bbox+'''; }
        li:nth-child(13) span:before {  content: '''+pencil+'''; }
    </style>''', unsafe_allow_html=True)

def api_bypass():
    global headers
    headers = {
        "api-key" : "quickstart-QUdJIGlzIGNvbWluZy4uLi4K",
        "X-Forwarded-For": ".".join(str(random.randint(0, 255)) for _ in range(4))
    }

def handle_error():
    api_bypass()
    st.error("Submit Again", icon="⚠️")

def save_uploadedfile(image_file, name="temp_image"):
    extension = "." + image_file.name.split(".")[-1]
    with open(os.path.join("temp", name + extension), "wb") as f:
        f.write(image_file.getbuffer())
    return 1

def render_content(style):
    with st.form("my_form"):
        image_file = st.file_uploader("", type=["png", "jpeg", "jpg"])
        submitted = st.form_submit_button("Submit")
        if submitted:
            if image_file is not None:
                save_uploadedfile(image_file)
                extension = "." + image_file.name.split(".")[-1]
                col1, col2 = st.columns(2)
                col1.header("Original")
                col1.image(image_file, use_column_width=True)
                col2.header(style)
                image_path = "temp/" + "temp_image" + extension
                try:
                    with col2:
                        with st.spinner(""):
                            if style=="Toonified":
                                img = toonify_api(image_path)
                            elif style=="Dreamified":
                                img = dreamify_api(image_path)
                            elif style=="Colorized":
                                img = colorization_api(image_path)
                            elif style=="Reduced Noise":
                                img = noise_reduction_api(image_path)
                            elif style=="Increased Resolution":
                                img = super_resolution_api(image_path)
                            elif style=="Nudity Detection":
                                img = nudity_detection_api(image_path)
                            st.image(img, use_column_width=True)
                except :
                    handle_error()


def render_dual_content(page, name1="Image 1", name2="Image 2"):
    with st.form("my_form"):
        image_file_1 = st.file_uploader(name1, type=["png", "jpeg", "jpg"])
        image_file_2 = st.file_uploader(name2, type=["png", "jpeg", "jpg"])
        submitted = st.form_submit_button("Submit")
        if submitted:
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
                image_path1 = "temp/" + "temp_image_1" + extension1
                image_path2 = "temp/" + "temp_image_2" + extension2
                try:
                    with st.spinner(""):
                        if page == "Compare Images":
                            match = compare_images_api(image_path1, image_path2)
                            st.header(f"Match : {match}%")
                        if page == "Style Transfer":
                            img = style_transfer_api(image_path1, image_path2)
                            st.header("Output :")
                            st.image(img, use_column_width=True)
                except:
                    handle_error()

def stable_diffusion_api(prompt, samples=4, scale=7.5, steps=45, seed=1024):
    model_id = "CompVis/stable-diffusion-v1-4"
    device = "cuda"
    value = os.getenv("HF_TOKEN")
    pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=value)
    pipe = pipe.to(device)
    generator = torch.Generator(device=device).manual_seed(seed)
    with autocast("cuda"):
        images_list = pipe( [prompt] * samples, num_inference_steps=steps, guidance_scale=scale, generator=generator)
    return images_list

def text_to_image_api(prompt):
    api="https://api.deepai.org/api/text2img"
    r = requests.post(
        api, data={"text": prompt}, headers=headers
    )
    resp = r.json()
    return resp["output_url"]

def generate_random_human_api():
    api="https://thispersondoesnotexist.com/image"
    resp = requests.get(api)
    return resp.content

def toonify_api(image_path):
    api="https://api.deepai.org/api/toonify"
    r = requests.post(
        api,
        files={"image": open(image_path, "rb"),},
        headers=headers,
    )
    resp = r.json()
    return resp["output_url"]

def style_transfer_api(image_path1, image_path2):
    api="https://api.deepai.org/api/neural-style"
    r = requests.post(
        api,
        files={
            "content": open(image_path1, "rb"),
            "style": open(image_path2, "rb"),
        },
        headers=headers,
    )
    resp = r.json()
    return resp["output_url"]

def dreamify_api(image_path):
    api="https://api.deepai.org/api/deepdream"
    r = requests.post(
        api,
        files={"image": open(image_path, "rb"),},
        headers=headers,
    )
    resp = r.json()
    return resp["output_url"]

def colorization_api(image_path):
    api="https://api.deepai.org/api/colorizer"
    r = requests.post(
        api,
        files={"image": open(image_path, "rb"),},
        headers=headers,
    )
    resp = r.json()
    return resp["output_url"]

def noise_reduction_api(image_path):
    api="https://api.deepai.org/api/waifu2x"
    r = requests.post(
        api,
        files={"image": open(image_path, "rb"),},
        headers=headers,
    )
    resp = r.json()
    return resp["output_url"]

def super_resolution_api(image_path):
    api="https://api.deepai.org/api/torch-srgan"
    r = requests.post(
        api,
        files={"image": open(image_path, "rb"),},
        headers=headers,
    )
    resp = r.json()
    return resp["output_url"]

def compare_images_api(image_path1, image_path2):
    api="https://api.deepai.org/api/image-similarity"
    r = requests.post(
        api,
        files={
            "image1": open(image_path1, "rb"),
            "image2": open(image_path2, "rb"),
        },
        headers=headers,
    )
    resp = r.json()
    if (resp["output"]["distance"]>=36):
        return 0
    else:
        return str(round(100-resp["output"]["distance"]*2.77777777778))

def nudity_detection_api(image_path):
    try:
        api="https://api.deepai.org/api/nsfw-detector"
        r = requests.post(
            api,
            files={"image": open(image_path, "rb"),},
            headers=headers,
        )
        resp = r.json()
        img = read_image(image_path)
        bbox=[]
        labels=[]
        for i in resp["output"]["detections"]:
            left, top, width, height = i["bounding_box"]
            bbox.append([left, top, left+width, top+height])
            labels.append(i["name"])
        bbox = torch.tensor(bbox, dtype=torch.int)
        img=draw_bounding_boxes(img, bbox,width=2,labels= labels,fill =True,font="font.ttf", font_size=int(height/9))
        img = torchvision.transforms.ToPILImage()(img)
        return img
    except Exception as e:
        st.write(e)

def background_removal(image_path):
    image = Image.open(image_path)
    output = remove(image)
    return output