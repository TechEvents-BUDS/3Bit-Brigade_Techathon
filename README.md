# 🌱 Plant Disease Detector — Techathon 2024 🚀

Welcome to our project submission for **Techathon 2024**, proudly presented by **Team 3 Bit Brigade**!  

---

## 💡 About the Project

Plants are essential to life on Earth, yet they often suffer from various diseases that impact their growth and yield. Our project aims to help farmers and gardeners detect plant diseases early by analyzing images and providing an instant health status.  

This tool uses deep learning (MobileNetV2) to classify plant images as **Healthy** or **Diseased**, and overlays descriptive advice on the image to guide plant care.

---

## 🏆 Event Context

This project was developed and presented at **Techathon 2024**, organized by the **Bahria University Developers Society (BUDS)**. BUDS is known for promoting innovation through events like "Code in the Dark" and continues to inspire students to bridge the gap between academia and industry.

---

## ⚙️ Features

- 📸 **Image Classification**: Uses a pre-trained MobileNetV2 model to classify plant images.
- 🟢 **Health Status Prediction**: Identifies whether the plant is healthy or diseased.
- 📝 **Care Recommendations**: Displays actionable care tips on the image.
- 🎨 **Dynamic Visual Overlay**: Combines the image with a clear, easy-to-read label and description.

---

## 🚀 Tech Stack

- **TensorFlow & Keras** — for deep learning and image classification.
- **PIL (Python Imaging Library)** — for image processing and annotation.
- **Matplotlib** — to display final output images.
- **NumPy** — for numerical operations and image array processing.

---

## 🗺️ How It Works

1️⃣ **Upload an Image**  
Provide an image of a plant leaf (recommended: 224x224 pixels).

2️⃣ **Classification**  
The model predicts whether the plant is healthy or diseased.

3️⃣ **Display Result**  
The image is shown with a label ("Healthy" or "Diseased") and a description box suggesting further care.

---

## 🏃‍♂️ Getting Started

### 🔧 Requirements

- Python 3.x
- TensorFlow
- NumPy
- Pillow (PIL)
- Matplotlib

Install dependencies:

```bash
pip install tensorflow numpy pillow matplotlib

