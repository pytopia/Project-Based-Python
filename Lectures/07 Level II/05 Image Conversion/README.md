<img src="./images/banner.png" width="800">

# Image Conversion Tool

Welcome to our Image Conversion Tool project! This tool aims to simplify the process of converting images into various formats and sizes. Designed with ease of use in mind, it features a user-friendly interface built with Streamlit, allowing users to upload images, select their desired output format (e.g., JPG, PNG, TIFF), and resize options before downloading the converted file. This project is perfect for individuals looking to quickly adjust images for web use, presentations, or personal storage optimization.

## Features

- **User-Friendly Interface**: Built with Streamlit, the interface is intuitive, making it easy for users to navigate and perform conversions without prior technical knowledge.
- **Multiple Format Support**: Users can convert images to popular formats, including JPG, PNG, and TIFF.
- **Customizable Size Options**: Provides the ability to resize images according to specific dimensions, thus catering to various needs and platforms.
- **Batch Conversion**: Offers the capability to upload and convert multiple images at once, saving time and effort.
- **Preview**: Users can preview the image before and after conversion, ensuring the output meets their expectations.

## Project Structure

- `app.py`: The main Python script that utilizes Streamlit for the web interface, handling file uploads, conversion logic, and user interactions.
- `converters/`: A directory containing modules for different image conversion functionalities, such as format conversion and resizing.
- `requirements.txt`: Lists all the necessary Python packages required to run the application.
- `README.md`: Provides an overview of the project, including its purpose, features, and instructions on how to set it up and use it.

## Requirements

To run this project, you will need:

- Python 3.6 or higher
- Streamlit
- Pillow for image processing
- Jupyter (optional, for running the notebook)

You can install all necessary packages using:

```bash
pip install -r requirements.txt
```

## Learning Outcome

By engaging with this project, individuals will learn:

- How to manipulate and convert images using Python.
- The basics of creating interactive web applications with Streamlit.
- Implementing file upload and download functionality in web apps.
- Best practices for structuring Python projects for clarity and maintainability.

## Future Enhancements

While the current version of the Image Conversion Tool meets basic needs, we envision the following enhancements to extend its capabilities and user experience:

- Integration of advanced image processing features, such as filtering and color adjustments.
- Adding support for more image formats based on user feedback.
- Enhancing the batch processing feature to include parallel processing for faster conversions.
- Implementing user accounts and history tracking to allow users to revisit and download previous conversions.
- Increasing the robustness of error handling and input validation to ensure a seamless user experience.
