import streamlit as st
import numpy as np
from PIL import Image, ImageChops, ImageEnhance
import io
import matplotlib.pyplot as plt

# -------------------------
# ELA COMPUTATION
# -------------------------
@st.cache_data
def compute_ela(image, quality=90):
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG", quality=quality)
    buffer.seek(0)
    compressed = Image.open(buffer)

    ela = ImageChops.difference(image.convert("RGB"), compressed.convert("RGB"))
    extrema = ela.getextrema()
    max_diff = max(ex[1] for ex in extrema) if extrema else 0

    scale = 255.0 / max_diff if max_diff != 0 else 1.0
    ela = ImageEnhance.Brightness(ela).enhance(scale)

    # Take one channel as grayscale-like ELA map
    ela_array = np.array(ela)[..., 0]

    return ela_array

# -------------------------
# FFT COMPUTATION
# -------------------------
@st.cache_data
def compute_fft(image):
    gray = np.array(image.convert("L"))
    f = np.fft.fft2(gray)
    fshift = np.fft.fftshift(f)
    magnitude = 20 * np.log(np.abs(fshift) + 1)
    return magnitude

# -------------------------
# ANOMALY SCORING
# -------------------------
def ela_score(ela_img):
    score = np.mean(ela_img) / 255.0 * 80
    return float(score)


def fft_score(spectrum):
    mean = np.mean(spectrum)
    std = np.std(spectrum)
    threshold = mean + std
    ratio = np.sum(spectrum > threshold) / spectrum.size
    score = ratio * 100
    return float(score)

# -------------------------
# STREAMLIT UI
# -------------------------
st.title("🕵️ Deepfake Image Forensic Analyzer")
st.write(
    "Upload one or more images to analyze compression artifacts (ELA) and frequency patterns (FFT) "
    "to detect potential AI-generated or manipulated images."
)

# accept_multiple_files=True returns a list of UploadedFile objects [web:66]
uploaded_files = st.file_uploader(
    "Upload JPG / PNG Image(s)",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True,
)

if uploaded_files:
    # Process each uploaded image independently
    for idx, uploaded in enumerate(uploaded_files, start=1):
        st.markdown(f"---")
        st.subheader(f"Image {idx}: {uploaded.name}")

        # Load and show original
        image = Image.open(uploaded).convert("RGB")
        st.image(image, caption="Uploaded Image", width=500)

        col1, col2 = st.columns(2)

        # ELA
        with col1:
            st.subheader("🔥 Error Level Analysis")
            ela_img = compute_ela(image)
            st.image(
                ela_img,
                caption="Bright areas show compression differences",
                width=300,
            )

        # FFT
        with col2:
            st.subheader("📊 Frequency Spectrum")
            spectrum = compute_fft(image)
            fig, ax = plt.subplots(figsize=(4, 4))
            ax.imshow(spectrum, cmap="gray")
            ax.axis("off")
            st.pyplot(fig)

        # -------------------------
        # SCORE CALCULATION
        # -------------------------
        ela_s = ela_score(ela_img)
        fft_s = fft_score(spectrum)
        combined = ela_s * 0.4 + fft_s * 0.6

        # -------------------------
        # THRESHOLD RULE (MAM)
        # -------------------------
        if combined <= 10:
            prediction = "Authentic Image"
            confidence = 95 - combined
            st.success(f"Prediction: {prediction}")
        elif 11 <= combined <= 15:
            prediction = "AI Manipulated Image"
            confidence = 75 + combined
            st.warning(f"Prediction: {prediction}")
        else:
            prediction = "Fully AI Generated Image"
            confidence = min(90 + combined / 5, 99)
            st.error(f"Prediction: {prediction}")

        st.subheader("Detection Details")
        st.write(f"ELA Score: {ela_s:.2f}")
        st.write(f"FFT Score: {fft_s:.2f}")
        st.write(f"Combined Score: {combined:.2f}")
        st.write(f"Confidence: {confidence:.1f}%")
else:
    st.info("Upload one or more images to start analysis.")
