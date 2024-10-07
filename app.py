import subprocess
import sys

def install_requirements():
    try:
        # Check if the requirements file exists
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except Exception as e:
        print(f"Error installing requirements: {str(e)}")

# Call the function to install requirements
install_requirements()

import streamlit as st
import os
from utils import *

def main():
    st.set_page_config(page_title = "PDF Summarizer")
    
    st.title('PDF Summarizing APP')
    st.write("Summarize your pdf files in just a few seconds")
    st.write("NOTE: The API of OpenAI has limited quota to use. If the app shows the error 'You exceeded your current quota', please check the code instead to judge my work.\nThank you for your time and effort.")
    st.divider()
    
    pdf = st.file_uploader('Upload your PDF Document')
    submit = st.button('Generate Summary')
    
    os.environ["OPENAI_API_KEY"] = "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"    
    if submit:
        response = summarizer(pdf)
        st.subheader('Summary of File:')
        st.write(response)
           
if __name__ == '__main__':
    main()
