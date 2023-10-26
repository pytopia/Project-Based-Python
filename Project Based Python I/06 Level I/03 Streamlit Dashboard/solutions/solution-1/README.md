# Password Generator Dashboard

## Project Overview
The 'Password Generator Dashboard' is an interactive web application built with Python and Streamlit. It allows users to generate different types of passwords quickly, either randomly, as a memorable sequence of words, or as a pin code, based on their preferences.

## Project Structure
The project has the following structure:

- `password_generators.py`: A Python module containing the password generators classes; `RandomPasswordGenerator`, `MemorablePasswordGenerator`, and `PinCodeGenerator`.
- `app.py`: A Python script using Streamlit to create a web app interface for the password generators.
- `README.md`: Documentation for the project solution. You are currently reading this!

## Getting Started

Follow the instructions below to set up this project on your local machine.

### Prerequisites

- Python 3.6 or later
- Streamlit
- NLTK (Natural Language Toolkit)

To install NLTK, use pip:

```bash
pip install nltk
```

After installing NLTK, you need to download the 'words' corpus. Run Python and type these commands:

```python
import nltk
nltk.download('words')
```

Then install Streamlit using pip:

```bash
pip install streamlit
```

You can install all the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

After following the installation steps, you can run the Streamlit web app as follows:

```sh
streamlit run app.py
```

This will open a web page in your default browser running on your localhost.
