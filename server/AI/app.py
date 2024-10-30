import logging
from fastapi import FastAPI, HTTPException
from langchain_community.document_loaders import PyMuPDFLoader
from database import init_db, insert_metadata
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import google.generativeai as genai
from dotenv import load_dotenv 
import json

import getpass
import os
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()
    logger.info("Database initialized")

@app.get("/")
def read_root():
    logger.info("Server is running")
    return {"message": "Server is running"}

@app.post("/pdf")
def read_pdf():
    pdf_path = "sample.pdf"
    try:
        logger.info("Starting PDF processing")
        loader = PyMuPDFLoader(pdf_path)
        doc = loader.load()
        logger.info("PDF loaded successfully")
        
        metadata = doc[0].metadata
        metadata_dict = {
            "source": pdf_path,
            "file_path": pdf_path,
            "page": 0,
            "total_pages": len(doc),
            "format": metadata.get("format", ""),
            "title": metadata.get("title", ""),
            "author": metadata.get("author", ""),
            "subject": metadata.get("subject", ""),
            "keywords": metadata.get("keywords", ""),
            "creator": metadata.get("creator", ""),
            "producer": metadata.get("producer", ""),
            "creationDate": metadata.get("creationDate", ""),
            "modDate": metadata.get("modDate", ""),
            "trapped": metadata.get("trapped", "")
        }
        
        insert_metadata(metadata_dict)
        logger.info("Metadata inserted into the database")
        
        text = {"metadata": metadata_dict}
        text_db=""
        for i in range(len(doc)):
            text[i + 1] = doc[i].page_content
            text_db+=doc[i].page_content
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
        chunks = text_splitter.split_text(text_db)
        logger.info("Text split into chunks")
        
        vector_store = FAISS.from_texts(chunks, embeddings)
        vector_store.save_local("faiss_index")
        logger.info("Vector store created and saved locally")
        
        return {"message": "Processing completed"}
    except Exception as e:
        logger.error(f"Error during PDF processing: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# To run the server, use the command: uvicorn app:app --reload