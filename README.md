# Personalize Content Search Chrome Extention


This project is a **Chrome Extension** that allows users to search for YouTube videos directly from the extension popup. It uses a **Flask backend** to fetch video results from YouTube using the **YouTube Data API v3** and displays them inside the extension.

## Features
- Search for YouTube videos from the Chrome extension popup
- Display top 10 relevant video results
- Embedded YouTube player inside the extension
- Backend powered by Flask and YouTube Data API

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript (Chrome Extension)
- **Backend:** Python (Flask), YouTube Data API
- **Hosting:** Local Flask Server

---

## Installation Guide

### **1️⃣ Get a YouTube API Key**
To fetch YouTube videos, you'll need an API key:
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project and enable **YouTube Data API v3**
3. Generate an API key and copy it

### **2️⃣ Clone the Repository**
```bash
$ git clone https://github.com/Vishal2053/Personalize-Content-Search-Chrome-Extention.git
$ cd Personalize-Content-Search-Chrome-Extention
```

### **3️⃣ Set Up Flask Backend**
1. Create a virtual environment:
   ```bash
   $ python -m venv venv
   $ source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   $ pip install -r requirements.txt
   ```
3. Create a **.env** file and add your API key:
   ```
   YOUTUBE_API_KEY=your_api_key_here
   ```
4. Run the Flask server:
   ```bash
   $ python app.py
   ```

### **4️⃣ Set Up the Chrome Extension**
1. Open Chrome and go to `chrome://extensions/`
2. Enable **Developer Mode**
3. Click **Load Unpacked**
4. Select the `extension` folder inside the project
5. Click on the extension icon and start searching!

---

## Project Structure
```
youtube-search-extension/
│── backend/
│   ├── app.py           # Flask API
│   ├── requirements.txt # Dependencies
│   ├── .env             # API Key (Not shared in repo)
│
│── extension/
│   ├── manifest.json    # Chrome Extension Configuration
│   ├── popup.html       # Extension UI
│   ├── popup.js         # JavaScript Logic
│   ├── styles.css       # Styling
│   ├── icon.png         # Extension Icon
│
│── README.md           # Project Documentation
```

---

## API Endpoints
| Method | Endpoint         | Description                  |
|--------|----------------|------------------------------|
| GET    | `/search?query=<your_query>` | Returns JSON list of YouTube videos |

Example Response:
```json
[
    {"title": "Machine Learning Basics", "url": "https://www.youtube.com/watch?v=abcd1234"},
    {"title": "Deep Learning Explained", "url": "https://www.youtube.com/watch?v=efgh5678"}
]
```

---

## License
This project is licensed under the **MIT License**.

Happy Coding! 🚀

