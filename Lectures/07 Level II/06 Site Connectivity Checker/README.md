<img src="./images/banner.png" width="800"/>

# Website Availability Checker

The Website Availability Checker is a Streamlit-based web application designed to help users monitor the availability of various websites. Users can add URLs to a list, and the application will check if those sites are accessible online (returning a status of "up" or "down"). This tool is particularly useful for website administrators, developers, and anyone interested in the status of specific web pages.

## Features

- **URL Management**: Users can add or remove URLs from their monitoring list.
- **Availability Check**: The application checks the availability of each website and displays the result with intuitive emojis.
- **Streamlit UI**: A user-friendly interface built with Streamlit for easy interaction.

## Technical Details

- **URL Formatting**: The application formats URLs to include "https://www." prefix, ensuring consistency in how URLs are processed.
- **Availability Check**: Uses Python's `requests` library to send a GET request to each website and check the response status.
- **Streamlit Framework**: Leverages Streamlit to create an interactive web application without the need for complex web development.

## Project Setup

To get started with this project, you will need to have Python installed on your machine. Additionally, the project depends on the following Python packages:

- `streamlit`
- `requests`

You can install these packages using pip:

```bash
pip install streamlit requests
```

To run the application, navigate to the project directory in your terminal and execute:

```bash
streamlit run app.py
```

## Considerations for Threading

While Python's threading module can be used to enhance the performance of scripts by checking multiple URLs concurrently, it may introduce complications when integrated with Streamlit's UI components. Streamlit's execution model, which re-runs the script upon each interaction, can lead to unexpected behavior with asynchronous operations like threading. Therefore, this project uses a simple loop to check the URLs sequentially to maintain UI stability and ensure a consistent user experience.

## Future Enhancements

- **Asynchronous Checks**: Investigate alternative approaches to implement non-blocking, concurrent checks without compromising the Streamlit UI.
- **Persistent URL Storage**: Implement a method to save the list of URLs, possibly using a database or local file storage, so that the list persists between sessions.
- **Advanced URL Validation**: Enhance the URL formatting function to handle a broader range of input variations and validate URLs before attempting to check their availability.
