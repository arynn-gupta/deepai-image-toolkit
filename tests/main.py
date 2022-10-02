import pydaisi as pyd
import urllib.request
deepai_image_toolkit = pyd.Daisi("arynn/DeepAI Image Toolkit")

try:
    prompt="ironman working as a chef, 4k, realistic, cinematic"
    images = (deepai_image_toolkit.stable_diffusion_daisi(prompt).value)
    for i, img in enumerate(images):
        img.save(f'output/stable_diffusion_daisi_{i}.jpg', 'JPEG')
except:
    print('Error in Stable Diffusion API')
try:
    prompt="shiba inu working as a chef, 4k, realistic, cinematic"
    img = (deepai_image_toolkit.text_to_image_daisi(prompt).value)
    img = urllib.request.urlopen(img).read()
    open('output/text_to_image_daisi.jpg', 'wb').write(img)
except:
    print('Error in Text to Image API')
try:
    img = (deepai_image_toolkit.generate_random_human_daisi().value)
    img.save('output/generate_random_human_daisi.jpg', 'JPEG')
except:
    print('Error in Random Human Generator API')
try:
    image = open("input/toonify_daisi.jpg", 'rb').read()
    img = (deepai_image_toolkit.toonify_daisi(image).value)
    img = urllib.request.urlopen(img).read()
    open('output/toonify_daisi.jpg', 'wb').write(img)
except:
    print('Error in Toonify API')
try:
    image1 = open("input/style_transfer_daisi_1.jpg", 'rb').read()
    image2 = open("input/style_transfer_daisi_2.jpg", 'rb').read()
    img = (deepai_image_toolkit.style_transfer_daisi(image1, image2).value)
    img = urllib.request.urlopen(img).read()
    open('output/style_transfer_daisi.jpg', 'wb').write(img)
except:
    print('Error in Style Transfer API')
try:
    image = open("input/dreamify_daisi.jpg", 'rb').read()
    img = (deepai_image_toolkit.dreamify_daisi(image).value)
    img = urllib.request.urlopen(img).read()
    open('output/dreamify_daisi.jpg', 'wb').write(img)
except:
    print('Error in Dreamify API')
try:
    image = open("input/colorization_daisi.jpg", 'rb').read()
    img = (deepai_image_toolkit.colorization_daisi(image).value)
    img = urllib.request.urlopen(img).read()
    open('output/colorization_daisi.jpg', 'wb').write(img)
except:
    print('Error in Colorization API')
try:
    image = open("input/noise_reduction_daisi.jpg", 'rb').read()
    img = (deepai_image_toolkit.noise_reduction_daisi(image).value)
    img = urllib.request.urlopen(img).read()
    open('output/noise_reduction_daisi.jpg', 'wb').write(img)
except:
    print('Error in Noise Reduction API')
try:
    image = open("input/super_resolution_daisi.jpg", 'rb').read()
    img = (deepai_image_toolkit.super_resolution_daisi(image).value)
    img = urllib.request.urlopen(img).read()
    open('output/super_resolution_daisi.jpg', 'wb').write(img)
except:
    print('Error in Super Resolution API')
try:
    image1 = open("input/compare_images_daisi_1.jpg", 'rb').read()
    image2 = open("input/compare_images_daisi_2.jpg", 'rb').read()
    output = (deepai_image_toolkit.compare_images_daisi(image1, image2).value)
    print(f"Match : {output}%")
except:
    print('Error in Compare Images API')
try:
    image = open("input/nudity_detection_daisi.jpg", 'rb').read()
    img = (deepai_image_toolkit.nudity_detection_daisi(image).value)
    img.save('output/nudity_detection_daisi.jpg', 'JPEG')
except:
    print('Error in Nudity Detection API')
try:
    image = open("input/background_removal_daisi.jpg", 'rb').read()
    img = (deepai_image_toolkit.background_removal_daisi(image).value)
    img.save('output/background_removal_daisi.png', 'PNG')
except:
    print('Error in Background removal API')
