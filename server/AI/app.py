from fastapi import FastAPI, HTTPException
from langchain_community.document_loaders import PyMuPDFLoader
from database import init_db, insert_metadata

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def read_root():
    print("Server is running")
    return {"message": "Server is running"}

@app.post("/pdf")
def read_pdf():
    pdf_path = "sample.pdf"
    try:
        loader = PyMuPDFLoader(pdf_path)
        doc = loader.load()
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
        
        text = {"metadata": metadata_dict}
        for i in range(len(doc)):
            text[i + 1] = doc[i].page_content
        
        return {"message": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# To run the server, use the command: uvicorn app:app --reload