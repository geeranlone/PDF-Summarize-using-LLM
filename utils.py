import streamlit as st
from pypdf import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback

def process_text(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    embeddings = HuggingFaceBgeEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    return knowledge_base

def summarizer(pdf):
    if pdf is not None:
        try:
            pdf_reader = PdfReader(pdf)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() or ""
            knowledge_base = process_text(text)
            
            query = "Summarize the content of the uploaded PDF file in approximately 3-5 sentences."
            if query:
                docs = knowledge_base.similarity_search(query)
                openai_model = "gpt-3.5-turbo-16k"
                llm = ChatOpenAI(model=openai_model, temperature=0.1)
                chain = load_qa_chain(llm, chain_type='stuff')
                
                with get_openai_callback() as cost:
                    response = chain.run(input_documents=docs, question=query)
                    print(cost)
                    return response
        except Exception as e:
            st.error(f"Error processing PDF file: {str(e)}")
            return None