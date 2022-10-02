import streamlit as st
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
os.environ["HF_TOKEN"] = "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"

import requests
import random
import torch
from torch import autocast
import torchvision
from torchvision import transforms
from torchvision.utils import draw_bounding_boxes
from icons import *
from diffusers import StableDiffusionPipeline
from  PIL import Image
import io
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

def render_content(style):
    with st.form("my_form"):
        image_file = st.file_uploader("", type=["png", "jpeg", "jpg"])
        submitted = st.form_submit_button("Submit")
        if submitted:
            if image_file is not None:
                col1, col2 = st.columns(2)
                col1.header("Original")
                col1.image(image_file, use_column_width=True)
                col2.header(style)
                try:
                    with col2:
                        with st.spinner(""):
                            if style=="Toonified":
                                img = toonify_api(image_file)
                            elif style=="Dreamified":
                                img = dreamify_api(image_file)
                            elif style=="Colorized":
                                img = colorization_api(image_file)
                            elif style=="Reduced Noise":
                                img = noise_reduction_api(image_file)
                            elif style=="Increased Resolution":
                                img = super_resolution_api(image_file)
                            elif style=="Nudity Detection":
                                img = nudity_detection_api(image_file)
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
                col1, col2 = st.columns(2)
                col1.header(name1)
                col1.image(image_file_1, use_column_width=True)
                col2.header(name2)
                col2.image(image_file_2, use_column_width=True)
                try:
                    with st.spinner(""):
                        if page == "Compare Images":
                            match = compare_images_api(image_file_1, image_file_2)
                            st.header(f"Match : {match}%")
                        if page == "Style Transfer":
                            img = style_transfer_api(image_file_1, image_file_2)
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
    return images_list["sample"]

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

def toonify_api(image):
    api="https://api.deepai.org/api/toonify"
    r = requests.post(
        api,
        files={"image": image,},
        headers=headers,
    )
    resp = r.json()
    return resp["output_url"]

def style_transfer_api(image1, image2):
    api="https://api.deepai.org/api/neural-style"
    r = requests.post(
        api,
        files={
            "content": image1,
            "style": image2,
        },
        headers=headers,
    )
    resp = r.json()
    return resp["output_url"]

def dreamify_api(image):
    api="https://api.deepai.org/api/deepdream"
    r = requests.post(
        api,
        files={"image": image,},
        headers=headers,
    )
    resp = r.json()
    return resp["output_url"]

def colorization_api(image):
    api="https://api.deepai.org/api/colorizer"
    r = requests.post(
        api,
        files={"image": image,},
        headers=headers,
    )
    resp = r.json()
    return resp["output_url"]

def noise_reduction_api(image):
    api="https://api.deepai.org/api/waifu2x"
    r = requests.post(
        api,
        files={"image": image,},
        headers=headers,
    )
    resp = r.json()
    return resp["output_url"]

def super_resolution_api(image):
    api="https://api.deepai.org/api/torch-srgan"
    r = requests.post(
        api,
        files={"image": image,},
        headers=headers,
    )
    resp = r.json()
    return resp["output_url"]

def compare_images_api(image1, image2):
    api="https://api.deepai.org/api/image-similarity"
    r = requests.post(
        api,
        files={
            "image1": image1,
            "image2": image2,
        },
        headers=headers,
    )
    resp = r.json()
    if (resp["output"]["distance"]>=36):
        return 0
    else:
        return str(round(100-resp["output"]["distance"]*2.77777777778))

def nudity_detection_api(image):
    api="https://api.deepai.org/api/nsfw-detector"
    r = requests.post(
        api,
        files={"image": image,},
        headers=headers,
    )
    resp = r.json()
    try:
        img = Image.open(image)
    except:
        img = Image.open(io.BytesIO(image))
    transform = torchvision.transforms.Compose([transforms.PILToTensor()])
    img = transform(img)
    bbox=[]
    labels=[]
    font_height=20
    for i in resp["output"]["detections"]:
        left, top, width, height = i["bounding_box"]
        bbox.append([left, top, left+width, top+height])
        labels.append(i["name"])
        font_height=height
    bbox = torch.tensor(bbox, dtype=torch.int)
    img = draw_bounding_boxes(img, bbox,width=2,labels= labels,fill =True,font="font.ttf", font_size=int(font_height/9))
    img = torchvision.transforms.ToPILImage('RGB')(img)
    return img

def background_removal_api(image):
    try:
        img = Image.open(image)
    except:
        img = image
    output = remove(img)
    return output