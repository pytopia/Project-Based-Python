# Fake News Detector

Fake News Detector is a Streamlit-based web application that uses web scraping and AI to analyze whether a given news headline or claim might be fake news. The app searches Google for relevant information, processes the search results, and uses OpenAI's language model to provide an assessment of the claim's credibility.

## Features

- User-friendly interface for inputting news headlines or claims
- Google search integration for gathering relevant information
- Text processing and context preparation from search results
- AI-powered analysis using OpenAI's GPT model
- Real-time feedback on the credibility of the input claim

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/fake-news-detector.git
   cd fake-news-detector
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Rename `example.env` to `.env`
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`)

3. Enter a news headline or claim in the text input field

4. Click the "Check" button to analyze the claim

5. Wait for the results to be displayed

## Project Structure

- `main.py`: Main Streamlit application
- `web_scraper.py`: Functions for web scraping and Google search
- `text_processor.py`: Text processing and context preparation functions
- `llm_interface.py`: OpenAI API interaction
- `requirements.txt`: List of required Python packages

## Dependencies

- streamlit
- requests
- beautifulsoup4
- openai
- markdownify

## Contributing

Contributions to improve the Fake News Detector are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## Disclaimer

This tool is for educational and research purposes only. It should not be used as the sole source for determining the credibility of news. Always cross-verify information from multiple reliable sources.
