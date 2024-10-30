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
import os

# Load environment variables from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize embeddings model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

@app.on_event("startup")
def on_startup():
    # Initialize the database on startup
    init_db()
    logger.info("Database initialized")

@app.get("/")
def read_root():
    # Root endpoint to check if the server is running
    logger.info("Server is running")
    return {"message": "Server is running"}

def process_pdf(pdf_path: str):
    # Process the PDF file and store its metadata and content
    logger.info("Starting PDF processing")
    
    # Load the PDF document
    loader = PyMuPDFLoader(pdf_path)
    doc = loader.load()
    logger.info("PDF loaded successfully")
    
    # Extract metadata from the first page of the document
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
    
    # Insert metadata into the database
    insert_metadata(metadata_dict)
    logger.info("Metadata inserted into the database")
    
    # Convert metadata to JSON string
    metadata_json = json.dumps(metadata_dict)
    
    # Concatenate metadata and page contents
    text_content = metadata_json + "\n"
    for i in range(len(doc)):
        text_content += doc[i].page_content + "\n"
    logger.info("PDF content concatenated")
    
    # Split the text content into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text_content)
    logger.info("Text split into chunks")
    
    # Create and save the vector store
    vector_store = FAISS.from_texts(chunks, embeddings)
    vector_store.save_local("faiss_index")
    logger.info("Vector store created and saved locally")
    
    return {"message": "Processing completed"}

@app.post("/pdf")
def read_pdf():
    # Endpoint to process a PDF file
    pdf_path = "sample.pdf"
    try:
        return process_pdf(pdf_path)
    except Exception as e:
        logger.error(f"Error during PDF processing: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# To run the server, use the command: uvicorn app:app --reload