# 🕵️ Deepfake Image Forensic Analyzer

## 🌐 Live Demo

You can try the application here:

https://deepfake-image-forensics-cxk9nd6zxy6xsnflrewps6.streamlit.app/

---

## 📌 Overview

This project implements a lightweight **Deepfake Image Detection System** using classical **digital image forensics techniques**. The application analyzes uploaded images to detect potential **AI-generated or manipulated content** by examining hidden patterns in image data.

The system uses **Error Level Analysis (ELA)** and **Fast Fourier Transform (FFT)** to identify anomalies in compression artifacts and frequency patterns that are often present in AI-generated images.

The application is built using **Python and Streamlit**, providing an interactive web interface where users can securely log in and analyze images.

---

## 🔐 Authentication Layer

To ensure controlled access, the application includes a simple **Signup and Login system** implemented using Streamlit session state.

Features:

* User **signup and login**
* Session-based authentication
* Sidebar logout option
* Access control before using the analysis tool

Once logged in, users can access the **Deepfake Analyzer dashboard**.

---

## ⚠️ Problem Statement

With the rapid advancement of generative AI models, it has become easier to create highly realistic synthetic images known as **deepfakes**. These images can be used for:

* misinformation 📰
* identity fraud 🪪
* digital manipulation 🎭

Since deepfakes often appear visually authentic, detecting them requires analyzing subtle patterns hidden inside the image data.

This project provides a **forensic analysis tool** that helps identify suspicious image artifacts.

---

## 🧠 Detection Techniques

### 🔥 Error Level Analysis (ELA)

ELA detects inconsistencies in image compression.

Process:

1. The image is recompressed at a fixed JPEG quality.
2. The difference between the original and recompressed image is calculated.
3. Differences are amplified to highlight suspicious areas.

Regions with abnormal brightness in the ELA heatmap may indicate manipulation.

---

### 📊 Frequency Domain Analysis (FFT)

Fast Fourier Transform converts an image from the **spatial domain** (pixel space) to the **frequency domain**.

AI-generated images often introduce unusual frequency patterns such as:

* repeated textures
* abnormal high-frequency artifacts
* inconsistent spectral distributions

The FFT spectrum visualization helps detect these anomalies.

---

## 🎯 Detection Logic

The system computes two anomaly scores:

* **ELA Score** → measures compression inconsistencies
* **FFT Score** → measures abnormal frequency patterns

These scores are combined into a weighted anomaly score.

| Combined Score | Classification              |
| -------------- | --------------------------- |
| 0 – 10         | ✅ Authentic Image           |
| 11 – 15        | ⚠️ AI Manipulated Image     |
| > 15           | 🚨 Fully AI Generated Image |

---

## ✨ Features

* 🔐 User authentication (signup & login)
* 📤 Upload one or multiple images
* 🔥 Visualize ELA heatmaps
* 📊 Visualize FFT frequency spectrum
* 🤖 Automatic deepfake classification
* 📈 Confidence score display
* 🌐 Interactive Streamlit interface

---

## 🛠 Technologies Used

* Python
* Streamlit
* NumPy
* Pillow (PIL)
* Matplotlib

---

## 📂 Project Structure

```
Deepfake-Image-Forensics
│
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/Ganesh-645/Deepfake-Image-Forensics.git
```

Navigate to the project directory:

```
cd Deepfake-Image-Forensics
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit application:

```
streamlit run app.py
```

The application will automatically open in your browser.

---

## 🔎 Application Workflow

1️⃣ User signs up or logs in
2️⃣ Access the Deepfake Analyzer dashboard
3️⃣ Upload one or more images
4️⃣ System performs **ELA and FFT analysis**
5️⃣ Visualizations and prediction results are displayed

---

## ⚠️ Limitations

* Classical forensic techniques may not detect all advanced deepfakes.
* Very high compression may reduce detection accuracy.
* The authentication system is **session-based and intended for demonstration purposes**.

---

## 🚀 Future Improvements

Possible enhancements include:

* Deep learning based classifiers
* GAN artifact detection
* Dataset-trained thresholds
* Video deepfake detection
* Cloud-based user authentication

---

## 👨‍💻 Author

Ganesh

Hackathon Project – **Deepfake Image Forensics Detection**

