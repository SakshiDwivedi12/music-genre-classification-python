# 🎵 Music Genre Classification System

An intelligent desktop application that automatically identifies the genre of any musical audio file (.wav) using Signal Processing and Machine Learning.



## 🚀 Overview
This project uses **Mel-frequency cepstrum coefficients (MFCC)** to extract unique acoustic signatures from audio signals. It then employs a **K-Nearest Neighbors (KNN)** classifier with a customized distance metric (Log-Likelihood) to predict the genre among 10 different categories (Blues, Classical, Country, Disco, Hip-hop, Jazz, Metal, Pop, Reggae, Rock).

## ✨ Key Features
* **Feature Extraction:** Advanced digital signal processing using the `python_speech_features` library.
* **Custom ML Logic:** Implementation of KNN from scratch with matrix-based distance calculations.
* **Graphical Interface:** Built with `Tkinter` for a seamless user experience.
* **Serialization:** Uses `pickle` for efficient loading of the pre-trained feature dataset (`my.dat`).

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** NumPy, SciPy, Pandas, python_speech_features
* **GUI:** Tkinter

## 📋 Installation & Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/SakshiDwivedi12/music-genre-classification-python.git]

2. Navigate to the project directory:
   ```bash
   cd Desktop/musicmaven/project
