import streamlit as st
import os
from lib.utils import styling
from lib.utils import stable_diffusion_api, text_to_image_api, generate_random_human_api, toonify_api, style_transfer_api, dreamify_api, colorization_api, noise_reduction_api, super_resolution_api, compare_images_api, nudity_detection_api, background_removal

def stable_diffusion_daisi(prompt, samples=4, scale=7.5, steps=45, seed=1024):
    '''
    Returns an array of Pillow images.
    '''
    return stable_diffusion_api(prompt, samples, scale, steps, seed)

def text_to_image_daisi(prompt):
    '''
    Returns a URL with the generated image.
    '''
    return text_to_image_api(prompt)

def generate_random_human_daisi():
    '''
    Returns a Pillow image.
    '''
    return generate_random_human_api()

def toonify_daisi(image):
    '''
    Returns a URL with the generated image.
    '''
    return toonify_api(image)

def style_transfer_daisi(image1, image2):
    '''
    Returns a URL with the generated image.
    '''
    return style_transfer_api(image1, image2)

def dreamify_daisi(image):
    '''
    Returns a URL with the generated image.
    '''
    return dreamify_api(image)

def colorization_daisi(image):
    '''
    Returns a URL with the generated image.
    '''
    return colorization_api(image)

def noise_reduction_daisi(image):
    '''
    Returns a URL with the generated image.
    '''
    return noise_reduction_api(image)

def super_resolution_daisi(image):
    '''
    Returns a URL with the generated image.
    '''
    return super_resolution_api(image)

def compare_images_daisi(image1, image2):
    '''
    Returns image match percentage.
    '''
    return compare_images_api(image1, image2)

def nudity_detection_daisi(image):
    '''
    Returns a Pillow image.
    '''
    return nudity_detection_api(image)

def background_removal(image):
    '''
    Returns a Pillow image.
    '''
    return background_removal(image)

def main():
    styling()

    st.title("Deep AI Image Toolkit")
    st.markdown("Welcome to the free A.I. image toolkit, this open-source toolkit let's you use various artificial intelligence tools to manipulate your images. Some of these include :")

    st.subheader("Stable Diffusion")
    st.markdown(
        "Stable Diffusion is a state of the art text-to-image model that generates images from text. It uses AI to understand your words and convert them to a unique image each time. Like magic."
    )
    st.markdown("`Prompt : albert einstein shaking hands with ironman, realistic, cinematic, anamorphic, 4k`")
    col1,col2 = st.columns(2)
    col1.image(os.path.join("demo_images", "Stable Diffusion_1.png"), use_column_width=True)
    col2.image(os.path.join("demo_images", "Stable Diffusion_2.png"), use_column_width=True)
    col3,col4 = st.columns(2)
    col3.image(os.path.join("demo_images", "Stable Diffusion_3.png"), use_column_width=True)
    col4.image(os.path.join("demo_images", "Stable Diffusion_4.png"), use_column_width=True)

    st.subheader("Text To Image")
    st.markdown("This is an AI image Generator. It creates an image from scratch from a text description. It is much faster than Stable difussion but compromises with image quality.")
    st.markdown("`Prompt : Shiba inu in Space`")
    st.image(os.path.join("demo_images", "Text To Image.jpg"), use_column_width=True)

    st.subheader("Generate Random Human")
    st.markdown("This tool generates Non Existent AI Generated Humans.")
    st.image(os.path.join("demo_images", "Generate Random Human.jpg"), use_column_width=True)

    st.subheader("Toonify")
    st.markdown("Turn a photo of any face into a cartoon instantly with artificial intelligence. Toonify uses a convolutional neural network to quickly transform the photo into a cartoon.")
    col1, col2 = st.columns(2)
    col1.image(os.path.join("demo_images", "Toonify_1.jpg"), use_column_width=True)
    col2.image(os.path.join("demo_images", "Toonify_2.jpg"), use_column_width=True)

    st.subheader("Style Transfer")
    st.markdown("Transfers the style from one image onto the content of another image.")
    col1, col2, col3= st.columns(3)
    col1.markdown("`Original Image`")
    col1.image(os.path.join("demo_images", "Style Transfer_1.jpg"), use_column_width=True)
    col2.markdown("`Style Image`")
    col2.image(os.path.join("demo_images", "Style Transfer_2.jpg"), use_column_width=True)
    col3.markdown("`Stylized Image`")
    col3.image(os.path.join("demo_images", "Style Transfer_3.jpg"), use_column_width=True)

    st.subheader("Dreamify Image")
    st.markdown("Exaggerates feature attributes or textures using information that the bvlc_googlenet model learned during training.")
    col1, col2 = st.columns(2)
    col1.image(os.path.join("demo_images", "Dreamify Image_1.jpg"), use_column_width=True)
    col2.image(os.path.join("demo_images", "Dreamify Image_2.jpg"), use_column_width=True)

    st.subheader("Digital Colorization")
    st.markdown("Colorize black and white images using the image colorization. Add color to old family photos and historic images, or bring an old film back to life with colorization.")
    col1, col2 = st.columns(2)
    col1.image(os.path.join("demo_images", "Colorization_1.jpg"), use_column_width=True)
    col2.image(os.path.join("demo_images", "Colorization_2.jpg"), use_column_width=True)

    st.subheader("Waifu2x Noise Reduction")
    st.markdown("This tool upscales images while reducing noise within the image. It gets its name from the anime-style art known as 'waifu' that it was largely trained on.")
    col1, col2 = st.columns(2)
    col1.image(os.path.join("demo_images", "Noise Reduction_1.jpg"), use_column_width=True)
    col2.image(os.path.join("demo_images", "Noise Reduction_2.jpg"), use_column_width=True)

    st.subheader("Super Resolution")
    st.markdown("Blurry images are unfortunately common and are a problem for professionals and hobbyists alike. Super Resolution uses machine learning to clarify, sharpen, and upscale the photo without losing its content and defining characteristics.")
    col1, col2 = st.columns(2)
    col1.image(os.path.join("demo_images", "Super Resolution_1.jpg"), use_column_width=True)
    col2.image(os.path.join("demo_images", "Super Resolution_2.jpg"), use_column_width=True)

    st.subheader("Compare Images")
    st.markdown("It compares two images and returns a value that tells you how visually similar they are. The more the score, the more contextually similar the two images are with a score of '100' being identical.")
    col1, col2 = st.columns(2)
    col1.image(os.path.join("demo_images", "Compare Images_1.jpg"), use_column_width=True)
    col2.image(os.path.join("demo_images", "Compare Images_2.jpg"), use_column_width=True)
    st.header("Match : 58 %")

    st.subheader("Nudity Detection")
    st.markdown("Detects the likelihood that an image contains nudity and should be considered NSFW.")
    col1, col2 = st.columns(2)
    col1.image(os.path.join("demo_images", "Nudity Detection_1.jpg"), use_column_width=True)
    col2.image(os.path.join("demo_images", "Nudity Detection_2.jpg"), use_column_width=True)

    st.subheader("Image Editor")
    st.markdown("Easy-to-use Photo Editor to edit photos and add photo effects.")
    st.image(os.path.join("demo_images", "Image Editor.jpg"), use_column_width=True)


if __name__ == '__main__':
    main()