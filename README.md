# Sunbird ALL - Assisted Language Learning (PoC)

## Overview
Sunbird ALL (Assisted Language Learning) is a Proof of Concept (PoC) application designed to facilitate language learning through speech recognition and transcription. This application allows users to record their speech, transcribe it into text, and receive feedback, supporting multiple languages such as English, Hindi, and Spanish.

The project consists of two main components:
1. **Frontend**: A Streamlit-based user interface for recording audio and displaying transcriptions.
2. **Backend**: A FastAPI-based server for processing audio files and performing speech-to-text conversion using the Vosk library.

## Features
- Record audio directly from the browser.
- Transcribe speech into text using Vosk ASR (Automatic Speech Recognition).
- Support for multiple languages (currently English, with placeholders for Hindi and Spanish).
- Dockerized setup for easy deployment.

## Project Structure
```
TEKDI/
├── app.py                # Streamlit frontend application
├── main.py               # FastAPI backend application
├── Dockerfile            # Docker configuration for the backend
├── docker-compose.yml    # Docker Compose configuration
├── model/                # Vosk ASR model files
└── __pycache__/          # Python cache files
```

## Prerequisites
- Python 3.9 or higher
- Docker and Docker Compose
- Internet connection (for initial setup)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Arjun618/DMP-25-Tekdi-POC.git
cd TEKDI
```

### 2. Install Dependencies
#### For Local Development:
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

#### For Dockerized Setup:
1. Build and start the Docker containers:
   ```bash
   docker-compose up --build
   ```

### 3. Run the Application
#### Local Development:
1. Start the backend server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
2. Start the frontend application:
   ```bash
   streamlit run app.py
   ```

#### Dockerized Setup:
1. Access the application at:
   - Frontend: `http://localhost:8501`
   - Backend: `http://localhost:8000`

## Usage
1. Open the frontend application in your browser.
2. Select a language from the dropdown menu.
3. Click the "Start Speaking" button to record your audio.
4. Wait for the transcription to appear on the screen.
5. View progress and insights in the "Dashboard" section (placeholder).

## Technical Details
### Backend (FastAPI)
- **Endpoint**: `/asr`
- **Functionality**: Accepts a WAV audio file, processes it using the Vosk ASR model, and returns the transcribed text.
- **Dependencies**: `fastapi`, `uvicorn`, `vosk`, `wave`

### Frontend (Streamlit)
- **Features**: Audio recording, language selection, and transcription display.
- **Dependencies**: `streamlit`, `requests`, `sounddevice`, `wave`

### Docker
- **Dockerfile**: Configures the backend server.
- **docker-compose.yml**: Orchestrates the backend service.

## How It Aligns with the Original Requirements
This implementation serves as a Proof of Concept (PoC) for the Assisted Language Learning (ALL) application. It demonstrates the following key functionalities:

1. **Speech-to-Text Conversion**:
   - The backend processes audio files and transcribes speech into text using the Vosk ASR library.
   - The frontend provides an interface for recording audio and displaying transcriptions.

2. **Multi-Language Support**:
   - The frontend allows users to select a language (English, Hindi, Spanish).
   - Currently, only the English Vosk model is integrated, but the structure supports adding models for other languages.

3. **User Interaction**:
   - The Streamlit-based frontend offers a simple and intuitive interface for users to interact with the application.

4. **Dockerized Deployment**:
   - The application is containerized, making it easy to deploy and run in different environments.

### Gaps in the Current PoC
While the PoC demonstrates the core functionality, it falls short in the following areas:
- **Dynamic Language Model Selection**: The backend currently uses a hardcoded English model. Dynamic model selection based on the user's language choice is not implemented.
- **User Authentication and Progress Tracking**: There is no mechanism to track individual user progress or provide personalized feedback.
- **Dashboard Insights**: The "Dashboard" section in the frontend is a placeholder and does not display meaningful insights or analytics.
- **Scalability**: The application is not optimized for handling multiple concurrent users.
- **Error Handling**: Basic error handling is implemented, but it needs to be more robust to handle edge cases.

## Future Scope
To fully meet the original requirements and goals, the following enhancements are recommended:

1. **Enhanced Multi-Language Support**:
   - Integrate additional Vosk models for Hindi, Spanish, and other languages.
   - Implement dynamic model selection in the backend based on the user's language choice.

2. **User Authentication and Personalization**:
   - Add user authentication to track individual progress.
   - Provide personalized feedback and learning recommendations based on user performance.

3. **Advanced Dashboard Features**:
   - Display detailed insights, such as transcription accuracy, learning progress, and areas for improvement.
   - Include visualizations like charts and graphs to make the data more engaging.

4. **Scalability and Performance**:
   - Optimize the backend for handling multiple concurrent users.
   - Consider using asynchronous processing for audio transcription to improve performance.

5. **Error Handling and Validation**:
   - Implement comprehensive error handling to manage invalid audio formats, missing models, and network issues.
   - Validate user inputs to ensure a smooth user experience.

6. **Production-Ready Deployment**:
   - Add support for deployment on cloud platforms like AWS, Azure, or Google Cloud.
   - Implement CI/CD pipelines for automated testing and deployment.

7. **Gamification and Engagement**:
   - Introduce gamification elements, such as badges and leaderboards, to motivate users.
   - Add interactive exercises and quizzes to enhance the learning experience.

## Future Enhancements
- Add support for additional languages by integrating more Vosk models.
- Implement user authentication and progress tracking.
- Enhance the dashboard with detailed insights and analytics.
- Improve error handling and scalability for production use.

## Troubleshooting
- **Audio Format Error**: Ensure the audio file is in WAV format, mono PCM, with a sample rate of 8000 or 16000 Hz.
- **Network Issues**: Verify that the backend server is running and accessible at `http://127.0.0.1:8000`.
- **Docker Issues**: Ensure Docker and Docker Compose are installed and running correctly.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [Vosk Speech Recognition Toolkit](https://alphacephei.com/vosk/)
- [Streamlit](https://streamlit.io/)
- [FastAPI](https://fastapi.tiangolo.com/)