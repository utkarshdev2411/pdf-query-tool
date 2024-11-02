# AI Planet

AI Planet is a web application that allows users to interact with an AI-powered chatbot and upload PDF files for processing. The application is built using React for the frontend and FastAPI for the backend.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)


## Features

- **Chatbot**: Interact with an AI-powered chatbot that answers your questions.
- **PDF Upload**: Upload PDF files for processing and extracting metadata and content.
- **Real-time Communication**: Seamless communication between the frontend and backend.

## Installation

### Prerequisites

- Node.js (v14 or higher)
- Python (v3.8 or higher)
- [pip](https://pip.pypa.io/en/stable/)

### Frontend

1. Navigate to the `frontend` directory:
    ```sh
    cd frontend
    ```

2. Install the dependencies:
    ```sh
    npm install
    ```

3. Start the development server:
    ```sh
    npm run dev
    ```

### Backend

1. Navigate to the `server/AI` directory:
    ```sh
    cd server/AI
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Start the FastAPI server:
    ```sh
    uvicorn app:app --reload
    ```

## Usage

1. Open your browser and navigate to `http://localhost:5173/` to access the frontend.
2. Use the chat interface to interact with the AI chatbot.
3. Upload PDF files using the upload button in the navigation bar.

## Project Structure

## API Endpoints

### PDF Upload Endpoint

- **URL**: `http://127.0.0.1:8000/pdf`
- **Method**: `POST`
- **Request Body**: `multipart/form-data`
- **Response**:
    ```json
    {
        "message": "Processing completed"
    }
    ```

### Chat Endpoint

- **URL**: `http://127.0.0.1:8000/chat`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "user_question": "Your question here"
    }
    ```
- **Response**:
    ```json
    {
        "answer": "AI's response"
    }
    ```





