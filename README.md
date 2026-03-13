# 🕵️ Deepfake Image Forensic Analyzer

## 📌 Overview

This project implements a lightweight **Deepfake Image Detection System** using classical **digital image forensics techniques**. The system analyzes uploaded images to identify potential **AI-generated or manipulated content** by examining hidden patterns in image data.

The application is built using **Python and Streamlit**, providing an interactive interface where users can upload images and instantly visualize forensic analysis results.

---

## ⚠️ Problem Statement

Recent advancements in generative AI have made it possible to create highly realistic synthetic images (deepfakes). These images can be misused for:

* misinformation 📰
* identity fraud 🪪
* digital manipulation 🎭

Since deepfakes often appear visually authentic, detecting them requires analyzing subtle patterns that are not visible to the human eye.

This project provides a **forensic analysis tool** that detects suspicious patterns within images using computational techniques.

---

## 🧠 Approach

The system combines two complementary forensic techniques to analyze images.

### 🔥 Error Level Analysis (ELA)

ELA detects inconsistencies in **image compression**.

When an image is saved in JPEG format, compression artifacts are distributed fairly evenly. If a portion of the image has been edited or generated separately, it may compress differently.

Steps performed:

1. Re-save the image using JPEG compression.
2. Compute the difference between the original and recompressed image.
3. Amplify the difference to create an **ELA heatmap** highlighting suspicious regions.

---

### 📊 Frequency Domain Analysis (FFT)

Fast Fourier Transform (FFT) converts the image from the **spatial domain (pixels)** to the **frequency domain (patterns)**.

AI-generated images sometimes introduce unusual patterns such as:

* repetitive textures
* abnormal frequency distributions
* unnatural high-frequency components

The **frequency spectrum visualization** helps detect these artifacts.

---

## 🎯 Detection Logic

The system computes two anomaly scores:

* **ELA Score** → measures compression inconsistencies
* **FFT Score** → measures abnormal frequency patterns

These scores are combined into a weighted anomaly score used to classify the image.

| Combined Score | Classification              |
| -------------- | --------------------------- |
| 0 – 10         | ✅ Authentic Image           |
| 11 – 15        | ⚠️ AI Manipulated Image     |
| > 15           | 🚨 Fully AI Generated Image |

---

## ✨ Features

* Upload **single or multiple images** 📤
* Visualize **ELA heatmaps** 🔥
* Visualize **FFT frequency spectrum** 📊
* Automatic **image classification** 🤖
* Displays **confidence score** 📈
* Interactive **Streamlit web interface** 🌐

---

## 🛠 Technologies Used

* **Python**
* **Streamlit**
* **NumPy**
* **Pillow (PIL)**
* **Matplotlib**

---

## 📂 Project Structure

```id="8pjymc"
deepfake-image-forensics
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```id="tsd7p6"
git clone https://github.com/yourusername/deepfake-image-forensics.git
```

Navigate to the project folder:

```id="iq7eqc"
cd deepfake-image-forensics
```

Install dependencies:

```id="1drd0a"
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit app:

```id="0o4t2k"
streamlit run app.py
```

The application will open automatically in your browser.

---

## 🔎 Example Workflow

1. Upload an image (JPG or PNG).
2. The system performs **ELA and FFT analysis**.
3. Visualizations are generated.
4. The system outputs a **prediction and confidence score**.

---

## ⚠️ Limitations

* Classical forensic methods may not detect all advanced deepfakes.
* Heavily compressed or post-processed images may reduce detection accuracy.
* This project is intended as a **research and educational prototype**.

---

## 🚀 Future Improvements

Possible improvements include:

* Integration of **deep learning models**
* Detection of **GAN-specific artifacts**
* Dataset-based threshold calibration
* Extension to **video deepfake detection**

---

## 👨‍💻 Author

Developed as part of a **Hackathon Project on Deepfake Image Forensics Detection**.
