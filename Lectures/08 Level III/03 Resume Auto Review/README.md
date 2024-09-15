<img src="src/images/banner.png" alt="ResumeAI Banner" height="200px">

# ResumeAI: Resume Parser and Reviewer

ResumeAI is an advanced tool that leverages the power of Large Language Models (LLMs) to analyze and improve resumes. This Streamlit-based application allows users to upload their resumes, optionally provide a job description, and receive detailed analysis and improvement suggestions.

## Features

- **Resume Parsing**: Extracts text from PDF resumes and parses it into a structured format.
- **Resume Review**: Analyzes the parsed resume, considering an optional job description.
- **Section-by-Section Analysis**: Provides a detailed review of each section of the resume.
- **Improvement Suggestions**: Offers revision suggestions with impact levels for each section.
- **Interactive UI**: User-friendly interface with section navigation and side-by-side comparison of original and revised content.

## Installation

1. Clone the repository:

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   export OPENAI_API_KEY=<your_openai_api_key>
   export PYTHONPATH=$PYTHONPATH:$(pwd)
   streamlit run src/app.py --server.enableXsrfProtection false
   ```

2. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).

3. Upload your resume PDF file using the file uploader in the sidebar.

4. (Optional) Enter a job description in the text area provided.

5. Click the "Run Analysis" button to start the resume parsing and review process.

6. Navigate through different sections of your resume using the arrow buttons.

7. Review the original content, revised content, and improvement suggestions for each section.

## Project Structure

- `app.py`: Main Streamlit application file.
- `src/utils/pdf.py`: Contains functions for extracting text from PDF files.
- `src/utils/llm.py`: Includes functions for parsing resumes and reviewing them using LLMs.
- `resume_formatter.py`: Handles the formatting of resume content for display.
- `src/images/banner.png`: Banner image for the application.

## Dependencies

- Streamlit
- PyYAML
- (Other dependencies as listed in `requirements.txt`)
