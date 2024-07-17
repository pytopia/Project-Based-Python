import streamlit as st
import requests

# Function to format URL to include "https://www."
def format_url(url):
    # Remove http:// or https:// if present
    if url.startswith('http://'):
        url = url[len('http://'):]
    elif url.startswith('https://'):
        url = url[len('https://'):]

    # Remove www. if present
    if url.startswith('www.'):
        url = url[len('www.'):]

    # Prepend https://www. to ensure consistency
    formatted_url = 'https://www.' + url
    return formatted_url


# Function to check website availability
def check_site_availability(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(url, timeout=5, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False


# Streamlit UI
def main():
    st.title("Website Availability Checker")

    # Session state to store the list of URLs
    if 'urls' not in st.session_state:
        st.session_state.urls = []

    new_url = st.text_input("Enter a URL to add to the list:", "")

    col1, col2 = st.columns(2)
    with col1:
        # Button to add the URL with formatted URL
        if st.button("Add URL"):
            formatted_url = format_url(new_url)
            if formatted_url not in st.session_state.urls and new_url != "":
                st.session_state.urls.append(formatted_url)
                st.success(f"Added {formatted_url} to the list")
    with col2:
        # Button to clear the list
        if st.button("Clear List"):
            st.session_state.urls.clear()

    # Button to check all URLs
    if st.button("Check All"):
        for idx, url in enumerate(st.session_state.urls):
            st.session_state[f"status_{idx}"] = check_site_availability(url)

    # Display the list of URLs with status emojis
    for idx, url in enumerate(st.session_state.urls):
        col1, col2 = st.columns([4,1])
        with col1:
            st.write(url)
        with col2:
            if f"status_{idx}" in st.session_state:
                st.write("✅" if st.session_state[f"status_{idx}"] else "❌")
            else:
                st.write("")

if __name__ == "__main__":
    main()
