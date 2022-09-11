import numpy as np
import streamlit as st
import cv2
from  PIL import Image, ImageEnhance
from lib.utils import styling

def main():

    styling()
    st.title("Image Editor")

    menu = ['Filters','Image Corrections']
    op = st.sidebar.selectbox('Option', menu)

    if op == 'Filters':

        filters = st.sidebar.radio('Filters', ['Original','Grayscale', 'Sepia', 'Blur', 'Contour', 'Sketch'])
        img = st.file_uploader('', type=['jpg', 'png', 'jpeg'])

        if img is not None:
            image = Image.open(img)
     
            if filters == 'Grayscale':
                img_convert = np.array(image.convert('RGB'))
                gray_image = cv2.cvtColor(img_convert, cv2.COLOR_RGB2GRAY)
                st.image(gray_image, use_column_width=True)
                
            elif filters == 'Sepia':
                img_convert = np.array(image.convert('RGB'))
                img_convert = cv2.cvtColor(img_convert, cv2.COLOR_RGB2BGR)
                kernel = np.array([[0.272, 0.534, 0.131],
                                [0.349, 0.686, 0.168],
                                [0.393, 0.769, 0.189]])
                sepia_image = cv2.filter2D(img_convert, -1, kernel)
                st.image(sepia_image, channels='BGR', use_column_width=True)
            
            elif filters == 'Blur':
                img_convert = np.array(image.convert('RGB'))
                slide = st.sidebar.slider('Quantidade de Blur', 3, 81, 9, step=2)
                img_convert = cv2.cvtColor(img_convert, cv2.COLOR_RGB2BGR)
                blur_image = cv2.GaussianBlur(img_convert, (slide,slide), 0, 0)
                st.image(blur_image, channels='BGR', use_column_width=True) 
            
            elif filters == 'Contour':
                img_convert = np.array(image.convert('RGB'))
                img_convert = cv2.cvtColor(img_convert, cv2.COLOR_RGB2BGR)
                blur_image = cv2.GaussianBlur(img_convert, (11,11), 0)
                canny_image = cv2.Canny(blur_image, 100, 150)
                st.image(canny_image, use_column_width=True)

            elif filters == 'Sketch':
                img_convert = np.array(image.convert('RGB')) 
                gray_image = cv2.cvtColor(img_convert, cv2.COLOR_RGB2GRAY)
                inv_gray = 255 - gray_image
                blur_image = cv2.GaussianBlur(inv_gray, (25,25), 0, 0)
                sketch_image = cv2.divide(gray_image, 255 - blur_image, scale=256)
                st.image(sketch_image, use_column_width=True) 
            else: 
                st.image(image, use_column_width=True)

    if op == 'Image Corrections':

        MImage = st.sidebar.radio('Image enhancement', ['Original', 'Contrast', 'brightness', 'Sharpness'])
        img = st.file_uploader('', type=['jpg', 'png', 'jpeg'])
        
        if img is not None:
            image = Image.open(img)
            if MImage == 'Contrast':
                slide = st.sidebar.slider('Contrast', 0.0, 2.0, 1.0)
                enh = ImageEnhance.Contrast(image)
                contrast_image = enh.enhance(slide)
                st.image(contrast_image, use_column_width=True)
            
            elif MImage == 'brightness':
                slide = st.sidebar.slider('brightness', 0.0, 5.0, 1.0)
                enh = ImageEnhance.Brightness(image)
                brightness_image = enh.enhance(slide)
                st.image(brightness_image, use_column_width=True)

            elif MImage == 'Sharpness':
                slide = st.sidebar.slider('Sharpness', 0.0, 2.0, 1.0)
                enh = ImageEnhance.Sharpness(image)
                sharpness_image = enh.enhance(slide)
                st.image(sharpness_image, use_column_width=True)
            else: 
                st.image(image, use_column_width=True)

if __name__ == '__main__':
    main()