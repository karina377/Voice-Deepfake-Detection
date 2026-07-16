# Voice Dashboard

## Overview

This folder contains the Streamlit dashboard developed as the deployment component of the AI Voice Deepfake Detection System.

The dashboard provides an interactive web-based interface that enables users to upload an audio recording and receive an immediate prediction indicating whether the recording is authentic or AI-generated (deepfake).

The deployed application is based on the **WavLM** deep learning model, which was selected after evaluating multiple state-of-the-art architectures due to its superior classification performance and overall computational efficiency.

---

## Main Features

The dashboard provides the following functionality:

- Upload audio recordings for analysis.
- Automatic audio preprocessing.
- Real-time deepfake detection using the trained WavLM model.
- Confidence score calculation.
- Risk level estimation.
- Display of recording information, including processing time and audio duration.
- History page for reviewing previous analyses.
- Analytics page with statistical summaries and visualizations.
- About page containing project information, model performance, and system configuration.

---

## Model Used

The dashboard uses the final trained **WavLM** model.

The evaluated models include:

- WavLM (Selected for deployment)
- Wav2Vec2
- AASIST
- RawNet3

Following the evaluation phase, WavLM was selected as the final deployment model because it achieved the best overall balance between classification performance, robustness, and computational efficiency.

---

## Dashboard Workflow

The dashboard performs the following operations after an audio recording is uploaded:

1. Upload audio recording.
2. Audio preprocessing.
3. Loading the trained WavLM model.
4. Feature extraction.
5. Audio classification.
6. Confidence score calculation.
7. Display of prediction and analysis results.
8. Saving the analysis results to the SQLite database.

---

## Project Structure

The dashboard is organized into several modules, each responsible for a different part of the application.

### app.py

The main entry point of the Streamlit application.

It initializes the dashboard, loads the required resources, and manages the overall application workflow.

---

### pages/

Contains the individual dashboard pages presented to the user, including:

- Audio Analysis
- Analytics
- History
- About

Each page is implemented separately to improve readability and maintainability.

---

### components/

Contains reusable user interface components shared across multiple dashboard pages.

Examples include:

- KPI cards
- Charts
- Layout components
- Status indicators
- User interface elements

---

### assets/

Contains static resources used throughout the dashboard, such as:

- Images
- Icons
- Project logo

These resources improve the visual appearance of the application.

---

### css/

Contains the custom CSS stylesheet used to define the dashboard layout, colors, typography, and overall visual design.

---

### models/

Contains the trained WavLM model and the inference code used to perform real-time deepfake detection.

---

### utils/

Contains helper modules responsible for:

- Audio preprocessing
- Database operations
- Utility functions
- Shared application logic

These modules are reused across different dashboard pages.

---

### database/

Contains the local SQLite database used by the dashboard.

The database stores the results of every analyzed recording and provides the data displayed in the History and Analytics pages.

---

## Technologies Used

The dashboard was developed using:

- Python
- Streamlit
- PyTorch
- Hugging Face Transformers
- Librosa
- SQLite
- Pandas
- Plotly

---

## Purpose

The dashboard represents the deployment stage of the project.

It demonstrates how the selected deep learning model can be integrated into an intuitive web application capable of performing real-time AI voice deepfake detection.

The application enables users to analyze audio recordings without requiring technical knowledge while providing clear predictions, confidence scores, historical records, and statistical insights.
