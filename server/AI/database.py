import sqlite3

def init_db():
    conn = sqlite3.connect('pdf_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pdf_metadata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            file_path TEXT,
            page INTEGER,
            total_pages INTEGER,
            format TEXT,
            title TEXT,
            author TEXT,
            subject TEXT,
            keywords TEXT,
            creator TEXT,
            producer TEXT,
            creationDate TEXT,
            modDate TEXT,
            trapped TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_metadata(metadata_dict):
    conn = sqlite3.connect('pdf_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pdf_metadata (
            source, file_path, page, total_pages, format, title, author, subject, keywords, creator, producer, creationDate, modDate, trapped
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        metadata_dict["source"], metadata_dict["file_path"], metadata_dict["page"], metadata_dict["total_pages"],
        metadata_dict["format"], metadata_dict["title"], metadata_dict["author"], metadata_dict["subject"],
        metadata_dict["keywords"], metadata_dict["creator"], metadata_dict["producer"], metadata_dict["creationDate"],
        metadata_dict["modDate"], metadata_dict["trapped"]
    ))
    conn.commit()
    conn.close()