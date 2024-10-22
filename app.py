import subprocess
import sys
import os
import streamlit as st
from utils import summarizer

# Ensure that required dependencies are installed
def ensure_dependencies():
    required_packages = ['pypdf', 'langchain', 'faiss-cpu', 'huggingface-hub']
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install dependencies if not already installed
ensure_dependencies()

# Function to install any additional requirements from a requirements.txt file
def install_requirements():
    requirements_file = "requirements.txt"
    if os.path.isfile(requirements_file):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        except subprocess.CalledProcessError as e:
            st.error(f"Failed to install requirements: {e}")
    else:
        st.warning(f"No {requirements_file} found.")

# Call the function to install requirements
install_requirements()

# Main function to handle PDF summarization
def main():
    st.set_page_config(page_title="PDF Summarization Tool")

    # Application Title and Instructions
    st.title('PDF Summarization Application')
    st.write("Upload a PDF file to generate a concise summary using AI-based techniques. Please note, OpenAI's API quota might limit functionality at times.")
    st.markdown("**Note**: If you see an error stating 'You exceeded your current quota', kindly review the logic behind the app to understand its functionality. Thank you!")

    # Divider for UI clarity
    st.divider()

    # File uploader for PDF
    pdf_file = st.file_uploader('Choose your PDF file', type="pdf")
    generate_summary = st.button('Generate Summary')

    # Set OpenAI API key
    os.environ["OPENAI_API_KEY"] = "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"

    # If the user clicks on the "Generate Summary" button
    if generate_summary and pdf_file is not None:
        try:
            summary = summarizer(pdf_file)
            st.subheader('Generated Summary:')
            st.write(summary)
        except Exception as e:
            st.error(f"An error occurred while summarizing the file: {e}")
    elif generate_summary:
        st.warning("Please upload a PDF file to summarize.")

# Run the application
if __name__ == "__main__":
    main()
