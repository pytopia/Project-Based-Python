import streamlit as st
from PyPDF2 import PdfReader
from llm_interface import call_llm
from prompts import RESUME_YAML_SCHEMA, LLM_YAML_PARSE_PROMPT, RESUME_REVIEW_PROMPT, JOB_DESCRIPTION_REVIEW_PROMPT, REVIEW_OUTPUT_SCHEMA
import yaml

import re

from yaml.loader import SafeLoader

class CustomSafeLoader(SafeLoader):
    def __init__(self, stream):
        super(CustomSafeLoader, self).__init__(stream)
        self.add_implicit_resolver(
            u'tag:yaml.org,2002:str',
            re.compile(u'^(?:(?!:).)*$', re.X),
            list(u'-0123456789')
        )

def extract_yaml(content):
    # Define the pattern to match YAML content
    pattern = r'```yaml\s*(.*?)\s*```'

    # Search for the pattern in the content
    match = re.search(pattern, content, re.DOTALL)

    if match:
        # If the pattern is found, return the content between the delimiters
        return match.group(1).strip()
    else:
        # If no delimiters are found, return the entire content
        return content.strip()


def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    resume_text = ""
    for page in reader.pages:
        resume_text += page.extract_text()
    return resume_text

st.title("Resume Parser and Reviewer")

# File uploader
uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

# Job description input
job_description = st.text_area("Enter job description (optional)")

# Run button
if st.button("Run Analysis", use_container_width=True):
    if uploaded_file is not None:
        # Extract text from PDF
        resume_text = extract_text_from_pdf(uploaded_file)

        # Parse resume
        parse_prompt = LLM_YAML_PARSE_PROMPT.format(resume_schema=RESUME_YAML_SCHEMA, resume_text=resume_text)
        resume_yaml = call_llm(parse_prompt)
        resume_yaml = extract_yaml(resume_yaml)
        # Review resume
        review_prompt = RESUME_REVIEW_PROMPT.format(resume_data=resume_yaml, review_output_schema=REVIEW_OUTPUT_SCHEMA)
        review_response = call_llm(review_prompt)
        review_response = extract_yaml(review_response)

        # Job description review (if provided)
        if job_description:
            job_review_prompt = JOB_DESCRIPTION_REVIEW_PROMPT.format(resume_data=resume_yaml, job_description=job_description, review_output_schema=REVIEW_OUTPUT_SCHEMA)
            job_review_response = call_llm(job_review_prompt)
        else:
            job_review_response = None

        # Parse YAML data
        resume_data = yaml.load(resume_yaml, Loader=CustomSafeLoader)
        review_data = yaml.load(review_response, Loader=CustomSafeLoader)

        # Store data in session state
        st.session_state.resume_data = resume_data
        st.session_state.review_data = review_data
        st.session_state.current_section = 0
        st.session_state.sections = list(resume_data.keys())

        # Display raw data in expanders
        with st.expander("Raw Resume Data"):
            st.code(resume_yaml)
        with st.expander("Raw Review Data"):
            st.code(review_response)
        if job_review_response:
            with st.expander("Raw Job Description Review"):
                st.code(job_review_response)

# Display parsed and reviewed data
if 'resume_data' in st.session_state and 'review_data' in st.session_state:
    st.header("Resume Analysis")

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Previous", use_container_width=True) and st.session_state.current_section > 0:
            st.session_state.current_section -= 1
    with col2:
        if st.button("➡️ Next", use_container_width=True) and st.session_state.current_section < len(st.session_state.sections) - 1:
            st.session_state.current_section += 1

    current_section = st.session_state.sections[st.session_state.current_section]
    st.subheader(current_section.replace("_", " ").title())

    # Display original and revised data
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Original**")
        st.write(st.session_state.resume_data[current_section])
    with col2:
        st.markdown("**Revised**")
        st.write(st.session_state.review_data[current_section])

else:
    st.info("Please upload a resume and run the analysis to view results.")
