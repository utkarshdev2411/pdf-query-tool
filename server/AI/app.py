from fastapi import FastAPI, HTTPException
from langchain_community.document_loaders import PyMuPDFLoader
import pymupdf

app = FastAPI()

@app.get("/")
def read_root():
    print("Server is running")
    return {"message": "Server is running"}

@app.post("/pdf")
def read_pdf():
    pdf_path="sample.pdf"
    try:
        loader = PyMuPDFLoader(pdf_path)
        doc = loader.load()
        text = {}
        for i in range(len(doc)):
            text[i+1]=doc[i].page_content
        return {"message": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# To run the server, use the command: uvicorn app:app --reload