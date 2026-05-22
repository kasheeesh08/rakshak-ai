# 🚨 Rakshak AI

Rakshak AI is a real-time AI-powered emergency detection and response system built using FastAPI, React, Whisper AI, and NLP pipelines.

The system listens to emergency voice input, transcribes speech into text, detects the emergency type, extracts severity and location, displays results on a live dashboard, and sends SMS alerts using Twilio.

---

# 🔥 Features

## ✅ Real-Time Voice Recording
- Record emergency voice input directly from the browser
- Audio processed instantly using backend AI pipeline

## ✅ Speech-to-Text using Whisper
- OpenAI Whisper model used for emergency transcription
- Supports Hinglish / mixed Hindi-English speech to some extent

## ✅ Emergency Classification
Detects emergency categories such as:
- Fire Emergency
- Road Accident
- Medical Emergency
- Violence / Threat situations

## ✅ Severity Detection
Classifies emergency intensity:
- Low
- Medium
- High
- Critical

## ✅ Location Extraction
Extracts location names from spoken emergency text.

Examples:
- "Fire near CST station"
- "Accident at Bandra"

## ✅ Live Emergency Dashboard
Frontend displays:
- Transcription
- Emergency type
- Severity level
- Detected location
- Emergency map visualization

## ✅ Dynamic Map Rendering
Uses OpenStreetMap + Leaflet.js for location visualization.

## ✅ SMS Emergency Alerts
Automatically sends SMS alerts using Twilio API.

---

# 🛠️ Tech Stack

## Frontend
- React.js
- Axios
- Leaflet.js
- React-Leaflet
- CSS

## Backend
- FastAPI
- Python

## AI / NLP
- OpenAI Whisper
- HuggingFace Transformers
- Custom NLP preprocessing
- Keyword-based hybrid classifier

## APIs / Services
- Twilio SMS API
- OpenStreetMap Nominatim API

---

# 📂 Project Structure

```bash
rakshak-ai/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── services/
│   │   ├── main.py
│   │
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/rakshak-ai.git
```

---

## 2️⃣ Backend Setup

```bash
cd rakshak-ai/backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

## 3️⃣ Frontend Setup

Open new terminal:

```bash
cd rakshak-ai/frontend
```

Install packages:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

Frontend runs on:

```bash
http://localhost:5173
```

---

# 📲 Twilio SMS Setup

Create a Twilio account:
https://www.twilio.com/

Add credentials inside:

```bash
backend/app/services/sms_service.py
```

```python
ACCOUNT_SID = "YOUR_ACCOUNT_SID"

AUTH_TOKEN = "YOUR_AUTH_TOKEN"

TWILIO_PHONE = "YOUR_TWILIO_PHONE"

TARGET_PHONE = "YOUR_PHONE_NUMBER"
```

---

# 🚀 How It Works

1. User records emergency voice input
2. Audio sent to FastAPI backend
3. Whisper transcribes speech
4. NLP pipeline classifies emergency
5. Severity + location extracted
6. Frontend dashboard updates live
7. SMS alert sent using Twilio
8. Emergency location displayed on map

---

# 📌 Current Limitations

- Multilingual support is experimental
- Location extraction is partially keyword-based
- Accuracy depends on audio quality
- Whisper running on CPU may be slower on low-end systems
- Internet required for SMS and map APIs

---

# 💡 Future Improvements

- Real-time streaming transcription
- Better multilingual support
- Hospital / police recommendation system
- WebSocket live updates
- Offline lightweight speech models
- Database logging
- Admin monitoring dashboard

---
# 📸 System Demonstrations

---

# 🚨 Road Accident Detection — Thane Station

![Dashboard](images/dashboard-main.png)

The AI system detects a road accident emergency, extracts the location from speech input, classifies severity level, and visualizes the emergency location dynamically on the map.

---

# 🚒 Fire Emergency Detection

![Fire Emergency](images/fire-emergency.png)

Rakshak AI can also detect fire-related emergencies from voice input and display real-time emergency information including severity and extracted location.

---

# 🗺️ Emergency Map Visualization

![Map Visualization](images/sms.png)

The dashboard dynamically renders emergency locations using OpenStreetMap and Leaflet.js for quick visual understanding of incident areas.

---

# 🔄 Complete Emergency Workflow

![Complete Workflow](images/complete-workflow.png)

This workflow explains the end-to-end processing pipeline from voice input to AI emergency classification, location extraction, dashboard visualization, and SMS alert delivery.

---

# 🧠 NLP + SMS + Frontend Pipeline

![Pipeline Workflow](images/sms testing.png)

This diagram explains the NLP pipeline, frontend-backend communication flow, and automated Twilio SMS integration used in Rakshak AI.

---

# 📲 Live SMS Alert Demonstration

<table>
<tr>

<td align="center">

### 🚨 Emergency Dashboard

<img src="images/dashboard-main.png" width="500"/>

</td>

<td align="center">

### 📲 SMS Alert Received

<img src="images/sms-alert.jpg" width="260"/>

</td>

</tr>
</table>

The detected emergency information is automatically converted into an SMS alert and sent using Twilio API with emergency type, location, and severity details.
