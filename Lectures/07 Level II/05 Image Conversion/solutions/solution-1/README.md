# Image Processing App

This Streamlit-based Image Processing App allows users to easily upload, resize, and convert the types of their images through a simple and intuitive web interface. Whether you need to adjust the size of your images for faster web performance or convert them between different formats for compatibility reasons, this app has got you covered.

## Features

- **Image Upload**: Users can upload images in JPEG, JPG, and PNG formats.
- **Resize Images**: Customize the dimensions of your images. You can specify the width and height directly or maintain the original aspect ratio.
- **Type Conversion**: Convert your images between popular formats (JPEG and PNG).
- **Download**: After processing, the modified images can be directly downloaded from the app.

## Getting Started

### Prerequisites

Before you can run the app, make sure you have Python installed on your machine. The app is built with Python and utilizes the Streamlit framework, along with the Pillow library for image processing tasks.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
2. **Navigate to the app directory**:
   ```bash
   cd your-repo-name
   ```
3. **Install the required Python packages**:
   - It's recommended to create a virtual environment before installing the dependencies.
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

With the environment set up and dependencies installed, you can run the app using the following command:

```bash
streamlit run image_processing_app.py
```

This will start the Streamlit server, and your default web browser should automatically open to the app's URL (typically `http://localhost:8501`).

## How to Use

1. **Upload an Image**: Click on the "Choose an image..." button to upload your image file.
2. **Select Process Type**: Choose whether you want to resize your image or convert its type.
3. **Specify Options**:
   - For resizing, enter the desired width and height, or check "Keep aspect ratio" and specify only the width.
   - For type conversion, select the desired output format from the dropdown menu.
4. **Process and Download**: Click the appropriate button to process your image. Once processed, a "Download Image" button will appear, allowing you to save the modified image to your device.

## Future Enhancements

- Support for additional image formats.
- Advanced image processing features, such as filters and color adjustments.
- Batch processing capability to handle multiple images simultaneously.
