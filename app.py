import streamlit as st
import os
from utils import *
def main():
    st.set_page_config(page_title = "PDF Summarizer")
    
    st.title('PDF Sumarizing APP')
    st.write("Summerize your pdf files in just a few secounds")
    st.write("NOTE: The API of openAI has limited quota to use, If the app shows the error 'You exceeded your current quota' please check the code insted to judge my work.\n Thank You for your time and effort. ")
    st.divider()
    
    pdf = st.file_uploader('upload your PDF Document')
    submit = st.button('Generate Summary')
    
    os.environ["OPENAI_API_KEY"] = "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"
    
    if submit:
        response = summarizer(pdf)
        st.subheader('summary of File:')
        st.write(response)
           
if __name__ == '__main__':
    main()