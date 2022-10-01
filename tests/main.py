import pydaisi as pyd
deepai_image_toolkit = pyd.Daisi("arynn/DeepAI Image Toolkit")
prompt="mars colliding with jupiter, 4k, realistic, 3d render"
image_path = "image1.jpg"
image_path1 = "image1.jpg"
image_path2 = "image2.jpg"
image = open(image_path, 'rb')
image1 = open(image_path1, 'rb')
image2  = open(image_path2, 'rb')
print(deepai_image_toolkit.stable_diffusion_daisi(prompt).value)
print(deepai_image_toolkit.text_to_image_daisi(prompt).value)
print(deepai_image_toolkit.generate_random_human_daisi().value)
print(deepai_image_toolkit.toonify_daisi(image).value)
print(deepai_image_toolkit.style_transfer_daisi(image1, image2).value)
print(deepai_image_toolkit.dreamify_daisi(image).value)
print(deepai_image_toolkit.colorization_daisi(image).value)
print(deepai_image_toolkit.noise_reduction_daisi(image).value)
print(deepai_image_toolkit.super_resolution_daisi(image).value)
print(deepai_image_toolkit.compare_images_daisi(image1, image2).value)
print(deepai_image_toolkit.nudity_detection_daisi(image).value)
print(deepai_image_toolkit.background_removal(image).value)