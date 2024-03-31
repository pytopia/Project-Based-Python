# Website Availability Checker Solution

This is the implementation of the Website Availability Checker, a Streamlit-based web application designed to monitor the status of websites. Users can add URLs to a list, and the application checks if those sites are accessible, displaying each site's status with intuitive emojis.

## Features

- **URL Management**: Users can dynamically add and remove URLs to/from their monitoring list.
- **Batch Availability Check**: Provides a "Check All" feature to verify the availability of all listed websites at once.
- **Status Display**: Indicates the availability of each website with a "✅" for accessible sites and a "❌" for inaccessible ones.
- **Clean URL Formatting**: Automatically formats user-entered URLs to include "https://www.", ensuring consistency in requests.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.6 or higher
- Streamlit
- Requests library

You can install the required Python packages using pip:

```bash
pip install streamlit requests
```

### Running the Application

1. Clone the repository or download the source code.
2. Navigate to the directory containing the application.
3. Run the application using Streamlit:

```bash
streamlit run app.py
```

4. The Streamlit interface should open in your default web browser, where you can start using the application.

## Implementation Details

- **Streamlit UI**: The application leverages Streamlit for an interactive user interface, allowing users to easily add, remove, and check URLs.
- **Requests for Checking Availability**: Utilizes Python's `requests` library to send HTTP GET requests to each website, determining their availability based on the response.
- **URL Formatting**: Includes a function to properly format URLs by adding "https://www." to user inputs, ensuring successful HTTP requests.

## Considerations

- **Sequential Checks**: To maintain stability within the Streamlit UI, website availability checks are performed sequentially. While Python's threading could be used for concurrent checks, it may cause issues with Streamlit's re-execution model upon each interaction.

## Future Enhancements

- **Asynchronous URL Checks**: Explore methods for implementing non-blocking URL checks that are compatible with Streamlit's execution model.
- **Persistent Storage**: Integrate a storage solution for persisting the list of URLs across sessions.
- **Improved URL Validation**: Enhance the URL formatting and validation logic to handle a wider range of user inputs.

