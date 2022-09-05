import streamlit as st
import os
import requests

api_key = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def render_content(style,api):
	def save_uploadedfile(image_file):
		with open(os.path.join("temp",image_file.name),"wb") as f:
			f.write(image_file.getbuffer())
		return 1

	image_file = st.file_uploader("",type=['png','jpeg','jpg'])
	if image_file is not None:
	    save_uploadedfile(image_file)
	    col1, col2 = st.columns(2)
	    col1.header("Original")
	    col1.image(image_file, use_column_width=True)
	    col2.header(style)
	    with col2:
	    	with st.spinner(''):
		    	r = requests.post(
		    		api,
		    		files={
		    			'image': open("temp/"+image_file.name, 'rb'),
		    		},
		    		headers={'api-key': api_key}
		    	)
	    resp = r.json()
	    try:
	    	col2.image(resp['output_url'], use_column_width=True)
	    except:
	    	st.write(r.json())

def page1():
    st.markdown("# Deep AI Image Toolkit")
    st.markdown("")
    st.markdown("This is an A.I. image toolkit, that provides you with the following features :")

def page2():
	st.markdown("# Colorization")
	st.markdown("`Add color to old family photos and historic images, or bring an old film back to life with colorization.`")
	render_content(style="Colorized", api="https://api.deepai.org/api/colorizer")

def page3():
	st.markdown("# Super Resolution")
	st.markdown("`Super Resolution uses machine learning to clarify, sharpen, and upscale the photo without losing its content and defining characteristics.`")
	render_content(style="Increased Resolution", api="https://api.deepai.org/api/torch-srgan")

def page4():
	st.markdown("# Text To Image")
	st.markdown("`This is an AI image Generator. It creates an image from scratch from a text description.`")
	with st.form("my_form"):
		prompt = st.text_area("Describe your image")
		submitted = st.form_submit_button("Submit")
	if submitted:
		with st.spinner(''):
			r = requests.post(
				"https://api.deepai.org/api/text2img",
				data={
					'text': prompt,
				},
				headers={'api-key': api_key}
			)
		resp = r.json()
		try:
			col2.image(resp['output_url'], use_column_width=True)
		except:
			st.write(r.json())

page_names_to_funcs = {
    "Page 1": page1,
    "Page 2": page2,
    "Page 3": page3,
    "Page 4": page4,
}


button1 = st.sidebar.button("About")
button2 = st.sidebar.button("Colorization")
button3 = st.sidebar.button("Super Resolution")
button4 = st.sidebar.button("Text To Image")
if button1:
     st.session_state.page = "Page 1"
elif button2:
     st.session_state.page = "Page 2"
elif button3:
     st.session_state.page = "Page 3"
elif button4:
     st.session_state.page = "Page 4"

try :
	page_names_to_funcs[st.session_state.page]()
except :
	page_names_to_funcs["Page 1"]()