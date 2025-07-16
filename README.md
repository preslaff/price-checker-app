# Shmeker Price Checker

Your smart companion for instantly verifying dual-currency price tags using your smartphone's camera. This application solves a common problem for consumers in Bulgaria by checking if the price in Euro (EUR) on a label is a fair conversion from the price in Bulgarian Lev (BGN), based on the official fixed rate.

### *for DEMO open https://shmeker.cdsv.dev with your smartphone*


## ✨ Features

*   **Live Camera Access**: Uses your smartphone's camera directly in the browser for a seamless experience.
*   **AI-Powered OCR**: Leverages the Google Cloud Vision API to accurately recognize numbers from real-world labels.
*   **Automatic Price Verification**: Intelligently identifies the BGN and EUR prices, calculates the expected conversion, and flags any unfair rounding.
*   **Visual Feedback**: Draws red rectangles around the detected prices on the captured image, so you know exactly what the app is seeing.
*   **Smart Proximity Detection**: Warns you if you are too far from the price tag for an accurate reading and prompts you to move closer.
*   **Seamless Workflow**: A "Scan Again" button provides a fluid, continuous loop for checking multiple items without reloading the page.
*   **Bilingual UI**: Fully translated interface for a native user experience.

## 🛠️ Tech Stack

This project is a full-stack web application combining a modern JavaScript frontend with a powerful Python backend and a robust production deployment architecture.

#### Frontend
*   **HTML5 & CSS3**: For structure and styling.
*   **Vanilla JavaScript (ES6+)**: For all client-side logic, interactivity, and API communication.
*   **`navigator.mediaDevices` API**: For accessing the live camera stream.
*   **HTML Canvas API**: For drawing the bounding box overlays on the captured image.

#### Backend & Deployment
*   **Python 3**: The core language for the backend API.
*   **Flask**: A lightweight micro-framework for building the API endpoint.
*   **Google Cloud Vision API**: The AI service providing powerful OCR capabilities.
*   **Gunicorn**: A production-grade WSGI server to run the Flask application.
*   **Nginx**: A high-performance reverse proxy to manage traffic and serve the application.
*   **Systemd**: To manage the backend and frontend processes as persistent services on Linux.
*   **Let's Encrypt & Certbot**: For free, automated SSL/TLS certificates, enabling secure HTTPS.
*   **DigitalOcean**: The cloud platform hosting the application.

## 🚀 Local Development Setup

To run this application on your local machine for development, follow these steps.

#### Prerequisites
*   [Git](https://git-scm.com/)
*   [Python 3.8+](https://www.python.org/downloads/)
*   A Google Cloud Platform account with the Vision API and billing enabled.

#### 1. Clone the Repository
```bash
git clone https://github.com/your-username/shmeker-price-checker.git
cd shmeker-price-checker
```

#### 2. Backend Setup
The backend requires a Python virtual environment and its own dependencies.

```bash
# Navigate to the backend directory
cd backend

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate
# On Windows: venv\Scripts\activate

# Install the required Python packages
pip install -r requirements.txt 
# (Or: pip install flask gunicorn pillow google-cloud-vision flask-cors)

# Place your Google Cloud credentials
# IMPORTANT: Copy your downloaded JSON key file into this directory
# and rename it to 'gcp_credentials.json'.
# This file is intentionally ignored by .gitignore and should never be committed.

# Run the backend server
flask run
# The backend will be running on http://127.0.0.1:5000```

#### 3. Frontend Setup
The frontend is served by a simple Python HTTP server.

```bash
# Open a NEW, SEPARATE terminal window
# Navigate to the frontend directory
cd frontend

# Run the server (can be done with or without the virtual environment)
python server.py
# The frontend will be running on http(s)://localhost:8000
```

#### 4. Access the Application
Open your web browser and navigate to the frontend URL (e.g., `https://localhost:8000` if you are using the HTTPS version of `server.py`). The application should be fully functional.


## 🔮 Future Ideas

*   **Support More Currencies**: Extend the app to handle other currency pairs by integrating a real-time exchange rate API.
*   **Scan History**: Allow users to see a history of their past scans.
*   **Improve OCR**: For very difficult labels, implement a custom-trained machine learning model (e.g., a fine-tuned CRNN or YOLO model) to replace the generic OCR.
*   **Progressive Web App (PWA)**: Add a service worker and manifest file to allow users to "install" the app to their home screen for a more native feel.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.