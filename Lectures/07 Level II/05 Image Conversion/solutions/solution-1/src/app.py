from io import BytesIO

import streamlit as st
from PIL import Image
from src.utils import convert_image_type, resize_image


def main():
    st.title(':zap: Image Processing App')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is None:
        return

    image = Image.open(uploaded_file)
    st.image(image, caption='Resized Image')
    process_type = st.radio("Select the process type", ["Resize", "Type Conversion"])

    if process_type == "Resize":
        keep_aspect_ratio = st.checkbox("Keep aspect ratio", value=True)
        col1, col2 = st.columns(2)

        if keep_aspect_ratio:
            width = col1.number_input("Width", value=image.width)
            # Calculate the new height to maintain the aspect ratio
            aspect_ratio = image.width / image.height
            height = int(width / aspect_ratio)
            # Display the calculated height, but don't allow user input
            height = col2.number_input("Height", value=height, disabled=True)
        else:
            width = col1.number_input("Width", value=image.width)
            height = col2.number_input("Height", value=image.height)

        if st.button("Resize Image"):
            resized_image = resize_image(image, width, height, keep_aspect_ratio)
            st.image(resized_image, caption='Resized Image')
            result_buffer = BytesIO()
            resized_image.save(result_buffer, format="PNG")
            st.download_button(
                label="Download Image",
                data=result_buffer.getvalue(),
                file_name="resized_image.png",
                mime="image/png"  # This can remain as is for resizing since we're saving as PNG
            )

    elif process_type == "Type Conversion":
        output_format = st.selectbox("Select output format", ["JPEG", "PNG"])
        # Dynamically set the MIME type based on the selected output format
        mime_type = f"image/{output_format.lower()}"
        if st.button("Convert Image Type"):
            converted_buffer = convert_image_type(image, output_format)
            st.image(image, caption=f'Image Converted to {output_format}')
            st.download_button(
                label="Download Image",
                data=converted_buffer.getvalue(),
                file_name=f"converted_image.{output_format.lower()}",
                mime=mime_type
            )


if __name__ == "__main__":
    main()
