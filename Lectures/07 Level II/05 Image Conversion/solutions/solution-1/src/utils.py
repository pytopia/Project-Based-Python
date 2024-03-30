from io import BytesIO


def resize_image(image, width, height, keep_aspect_ratio):
    if keep_aspect_ratio:
        image.thumbnail((width, height))
    else:
        image = image.resize((width, height))
    return image


def convert_image_type(image, output_format):
    if output_format.lower() == "jpeg":
        output_format = "JPEG"
    elif output_format.lower() == "png":
        output_format = "PNG"
    buffer = BytesIO()
    image.save(buffer, format=output_format)
    return buffer
