# SmartDetect AI – Voice Deepfake Detection System

1. Project Overview
2. Background
3. Repository Structure
4. Dataset
5. Deep Learning Models
6. Model Evaluation
7. Dashboard
8. Technologies Used
9. Installation
10. Google Drive Resources
11. Live Dashboard
12. Documentation
13. Future Work
14. Authors
15. Acknowledgments

# SmartDetect AI – Voice Deepfake Detection System

## Project Overview

SmartDetect AI is an end-to-end deep learning system developed to automatically detect AI-generated (deepfake) voice recordings through real-time audio analysis.

The project was developed as a final-year capstone project in the Information Systems program in collaboration with the **Israel National Cyber Directorate**, addressing the growing cybersecurity challenges posed by modern voice cloning technologies.

The system covers the complete machine learning lifecycle, including dataset development, model training, performance evaluation, statistical analysis, and deployment through an interactive Streamlit dashboard.

Four state-of-the-art deep learning architectures were implemented and evaluated:

- WavLM
- Wav2Vec2
- AASIST
- RawNet3

Following a comprehensive evaluation process, **WavLM** was selected as the final deployment model due to its superior balance between classification performance and computational efficiency.

This repository contains all project components, including dataset preparation, model development, statistical analyses, database implementation, deployment, and user documentation.


## Background

Recent advances in generative artificial intelligence have significantly improved the quality of synthetic speech generation. Modern voice cloning technologies are capable of producing highly realistic speech that closely resembles authentic human voices, making it increasingly difficult to distinguish between genuine and AI-generated recordings.

While these technologies have many legitimate applications, they also introduce serious cybersecurity risks, including identity theft, social engineering attacks, financial fraud, misinformation, and unauthorized access to voice-based authentication systems.

To address these challenges, this project was developed in collaboration with the **Israel National Cyber Directorate** with the objective of creating an automated AI-based system capable of detecting voice deepfakes.

One of the main challenges of the project was the limited availability of Hebrew voice deepfake datasets. To overcome this limitation, a custom Hebrew dataset was developed by combining authentic recordings from Mozilla Common Voice with AI-generated Hebrew recordings created using the ElevenLabs API.

The resulting system demonstrates a complete end-to-end solution for AI voice deepfake detection, from dataset construction and model evaluation to deployment as a real-time web application.

## 3. Repository Structure

The repository is organized into modular components that represent the different stages of the project, from dataset preparation to model deployment.

```
Voice-Deepfake-Detection
│
├── data preparation/
├── models/
├── statistical summary/
├── database/
├── voice_dashboard/
│
├── USER_GUIDE.md
├── User Guide.pdf
├── README.md
└── requirements.txt
```

| Directory | Description |
|------------|-------------|
| **data preparation/** | Dataset construction, preprocessing pipeline, and Hebrew deepfake generation. |
| **models/** | Implementation, training, and evaluation of the deep learning models. |
| **statistical summary/** | Statistical analyses, evaluation tables, performance visualizations, and comparison results. |
| **database/** | SQLite database implementation, ERD, and database creation scripts. |
| **voice_dashboard/** | Streamlit application used for real-time deployment of the selected model. |

Each major directory contains its own **README.md** file with detailed documentation describing its purpose, workflow, and generated outputs.



## 4. System Architecture

SmartDetect AI follows an end-to-end machine learning pipeline that covers every stage required for AI voice deepfake detection, from dataset construction to real-time deployment.

The overall system architecture is illustrated below.

> **Insert System Architecture Diagram Here**

The system consists of the following stages:

1. **Dataset Development** – Collection and preparation of public and custom Hebrew datasets.
2. **Data Preparation** – Dataset balancing, preprocessing, Hebrew deepfake generation, and train/validation/test splitting.
3. **Model Training** – Training and fine-tuning of four deep learning architectures.
4. **Model Evaluation** – Comparison of model performance using classification and computational metrics.
5. **Model Selection** – Selection of the most suitable model based on overall evaluation results.
6. **Deployment** – Integration of the selected WavLM model into an interactive Streamlit dashboard.
7. **Database Integration** – Storage of prediction results in a local SQLite database for history management and analytics.

This modular architecture enables each stage of the project to be developed, evaluated, and maintained independently while forming a complete end-to-end AI solution.

For additional implementation details, refer to the README files in the corresponding project directories.
