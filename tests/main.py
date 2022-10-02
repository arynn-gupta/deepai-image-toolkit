import pydaisi as pyd
deepai_image_toolkit = pyd.Daisi("arynn/DeepAI Image Toolkit")
prompt="mars colliding with jupiter, 4k, realistic, 3d render"
image_path = "image1.jpg"
image_path1 = "image1.jpg"
image_path2 = "image2.jpg"
image = open(image_path, 'rb').read()
image1 = open(image_path1, 'rb').read()
image2  = open(image_path2, 'rb').read()
try:
    print(deepai_image_toolkit.stable_diffusion_daisi(prompt).value)
except:
    print('Error in Stable Diffusion API')
try:
    print(deepai_image_toolkit.text_to_image_daisi(prompt).value)
except:
    print('Error in Text to Image API')
try:
    print(deepai_image_toolkit.generate_random_human_daisi().value)
except:
    print('Error in Random Human Generator API')
try:
    print(deepai_image_toolkit.toonify_daisi(image).value)
except:
    print('Error in Toonify API')
try:
    print(deepai_image_toolkit.style_transfer_daisi(image1, image2).value)
except:
    print('Error in Style Transfer API')
try:
    print(deepai_image_toolkit.dreamify_daisi(image).value)
except:
    print('Error in Dreamify API')
try:
    print(deepai_image_toolkit.colorization_daisi(image).value)
except:
    print('Error in Colorization API')
try:
    print(deepai_image_toolkit.noise_reduction_daisi(image).value)
except:
    print('Error in Noise Reduction API')
try:
    print(deepai_image_toolkit.super_resolution_daisi(image).value)
except:
    print('Error in Super Resolution API')
try:
    print(deepai_image_toolkit.compare_images_daisi(image1, image2).value)
except:
    print('Error in Compare Images API')
try:
    print(deepai_image_toolkit.nudity_detection_daisi(image).value)
except:
    print('Error in Nudity Detection API')
try:
  print(deepai_image_toolkit.background_removal_daisi(image).value)
except:
    print('Error in Background removal API')