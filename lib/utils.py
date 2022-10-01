import streamlit as st
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
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

def handle_error(resp, type="post"):
    if( type=="post"):
        try :
            if "Sign up" in resp["status"] :
                api_bypass()
                st.error("Submit Again", icon="⚠️")
        except:
            st.error("Tool is currently unavailable.", icon="⚠️")
            # dev output
            # st.error(resp, icon="⚠️")
    else:
        st.error("Tool is currently unavailable.", icon="⚠️")
        # dev output
        # st.error(resp.content, icon="⚠️")

def save_uploadedfile(image_file, name="temp_image"):
    extension = "." + image_file.name.split(".")[-1]
    with open(os.path.join("temp", name + extension), "wb") as f:
        f.write(image_file.getbuffer())
    return 1

def render_content(api, style):
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
                try:
                    with col2:
                        with st.spinner(""):
                            r = requests.post(
                                api,
                                files={"image": open("temp/" + "temp_image" + extension, "rb"),},
                                headers=headers,
                            )
                            resp = r.json()
                            if style=="Nudity Detection":
                                img = read_image("temp/" + "temp_image" + extension)
                                bbox=[]
                                labels=[]
                                for i in resp["output"]["detections"]:
                                    left, top, width, height = i["bounding_box"]
                                    bbox.append([left, top, left+width, top+height])
                                    labels.append(i["name"])
                                bbox = torch.tensor(bbox, dtype=torch.int)
                                img=draw_bounding_boxes(img, bbox,width=2,labels= labels,fill =True,font="font.ttf", font_size=int(height/9))
                                img = torchvision.transforms.ToPILImage()(img)
                                st.image(img, use_column_width=True)
                            else:
                                st.image(resp["output_url"], use_column_width=True)
                except :
                    handle_error(resp)


def render_dual_content(api, page, name1="Image 1", name2="Image 2"):
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
                try:
                    with st.spinner(""):
                        if page == "Compare Images":
                            r = requests.post(
                                api,
                                files={
                                    "image1": open("temp/" + "temp_image_1" + extension1, "rb"),
                                    "image2": open("temp/" + "temp_image_2" + extension2, "rb"),
                                },
                                headers=headers,
                            )
                            resp = r.json()
                            if (resp["output"]["distance"]>=36):
                                st.header("Match : 0%")
                            else:
                                st.header("Match : " + str(round(100-resp["output"]["distance"]*2.77777777778)) + " %")
                        if page == "Style Transfer":
                            r = requests.post(
                                api,
                                files={
                                    "content": open("temp/" + "temp_image_1" + extension1, "rb"),
                                    "style": open("temp/" + "temp_image_2" + extension2, "rb"),
                                },
                                headers=headers,
                            )
                            resp = r.json()
                            st.header("Output :")
                            st.image(resp["output_url"], use_column_width=True)
                except:
                    handle_error(resp)

def render_form(label, api):
    with st.form("my_form"):
        prompt = st.text_area(label)
        submitted = st.form_submit_button("Submit")
        if submitted:
            try:
                with st.spinner(""):
                    r = requests.post(
                        api, data={"text": prompt}, headers=headers
                    )
                    resp = r.json()
                    st.image(resp["output_url"], use_column_width=True)
            except :
                handle_error(resp)

def render_generator_btn(label, api):
    with st.form("my_form"):
        submitted = st.form_submit_button(label)
        if submitted:
            try:
                with st.spinner(""):
                    resp = requests.get(api)
                    st.image(resp.content, use_column_width=True)
            except:
                handle_error(resp)


def stable_dffusion(label):
    with torch.no_grad():
        torch.cuda.empty_cache()
    model_id = "CompVis/stable-diffusion-v1-4"
    device = "cuda"
    value = os.getenv("HF_TOKEN")
    pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=value)
    pipe = pipe.to(device)
    
    samples = st.sidebar.number_input("Number of images", value=4)
    scale = st.sidebar.number_input("Guidance", value=7.5)
    steps = st.sidebar.number_input("Steps", value=45)
    seed = st.sidebar.number_input("Seed", value=1024)
    
    with st.form("my_form"):
        prompt = st.text_area(label)
        submitted = st.form_submit_button("Submit")
        if submitted:
            try:
                with st.spinner(""):
                        generator = torch.Generator(device=device).manual_seed(seed)
                        with autocast("cuda"):
                            images_list = pipe( [prompt] * samples, num_inference_steps=steps, guidance_scale=scale, generator=generator)
                        for image in images_list["sample"]:
                            st.image(image)
            except Exception as e:
                st.text(e)