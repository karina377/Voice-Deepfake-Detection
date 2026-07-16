# SmartDetect AI – Voice Deepfake Detection System

1. Project Overview
2. Background and Motivation
3. Project Objectives
4. System Architecture
5. Repository Structure
6. Dataset Development
7. Deep Learning Models
8. Model Evaluation
9. Final Model Selection
10. Dashboard Deployment
11. Technologies Used
12. Installation
13. Google Drive Resources
14. Live Dashboard
15. Project Results
16. Future Work
17. Authors
18. Acknowledgments



# SmartDetect AI – Voice Deepfake Detection System

## Project Overview

**SmartDetect AI** is a deep learning-based system developed to detect AI-generated and manipulated voice recordings (voice deepfakes) through automatic audio analysis.

The project was carried out as a final-year capstone project in the Information Systems program in collaboration with the **Israel National Cyber Directorate**, addressing the growing cybersecurity threat posed by modern voice cloning technologies.

Recent advances in generative artificial intelligence have significantly improved the quality and accessibility of synthetic speech generation. As a result, voice deepfakes have become increasingly difficult to distinguish from authentic human speech, creating new risks in identity theft, financial fraud, social engineering attacks, misinformation campaigns, and unauthorized access to secure systems.

To address this challenge, this project presents a complete end-to-end deepfake detection framework covering the entire machine learning lifecycle—from dataset construction and model development to evaluation and deployment.

Unlike many existing studies that rely exclusively on public English datasets, this project also introduces a **custom Hebrew voice dataset** generated specifically for this research. Authentic Hebrew recordings were collected from Mozilla Common Voice and paired with AI-generated Hebrew deepfakes produced using the ElevenLabs API. These recordings were combined with carefully selected samples from the ASVspoof2021 DeepFake dataset to create a balanced dataset suitable for training and evaluating deep learning models.

Four state-of-the-art deep learning architectures were implemented and evaluated:

- WavLM
- Wav2Vec2
- AASIST
- RawNet3

Each model was trained and evaluated using identical datasets and evaluation procedures. Their performance was compared using multiple classification and computational metrics, including:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Error Rate
- Model Size
- Memory Consumption
- Inference Time

Following the evaluation phase, **WavLM** achieved the best overall balance between detection performance and computational efficiency and was therefore selected as the final deployment model.

To demonstrate the practical applicability of the selected model, a complete web-based application was developed using **Streamlit**. The dashboard enables users to upload audio recordings, perform real-time deepfake detection, review historical analyses, visualize statistical summaries, and explore model performance through an intuitive user interface.

This repository contains every stage of the project, including dataset preparation scripts, deep learning models, statistical analyses, evaluation reports, database implementation, and the final deployed dashboard.

# 2. Background and Motivation

The rapid advancement of generative artificial intelligence has transformed the field of synthetic speech generation. Modern voice cloning technologies are now capable of producing highly realistic speech that closely mimics the voice characteristics, pronunciation, and speaking style of real individuals.

While these technologies offer significant benefits in areas such as accessibility, content creation, virtual assistants, and entertainment, they also introduce serious cybersecurity risks. High-quality AI-generated speech can be exploited to impersonate individuals, bypass voice-based authentication systems, conduct social engineering attacks, spread misinformation, and facilitate financial fraud.

As voice synthesis technologies continue to improve, distinguishing between authentic and AI-generated speech has become increasingly difficult for human listeners. Consequently, automated deep learning-based detection systems have become essential for identifying manipulated audio recordings quickly and accurately.

Recognizing the growing importance of this challenge, the **Israel National Cyber Directorate** proposed the development of a system capable of detecting AI-generated voice recordings as part of this final-year capstone project.

The objective was not only to evaluate existing deep learning models, but also to develop a complete end-to-end solution that covers the entire machine learning lifecycle, including:

- Data collection
- Dataset preparation
- Generation of synthetic Hebrew deepfake recordings
- Model training and fine-tuning
- Performance evaluation
- Statistical analysis
- Deployment as an interactive web application

One of the major challenges encountered during the project was the limited availability of Hebrew datasets for voice deepfake detection. Most publicly available datasets are based on English speech and therefore do not adequately represent Hebrew pronunciation, phonetics, or linguistic characteristics.

To address this limitation, a dedicated Hebrew dataset was created specifically for this project. Authentic Hebrew recordings were collected from Mozilla Common Voice, while corresponding AI-generated recordings were created using the ElevenLabs speech synthesis platform. These recordings were combined with carefully selected samples from the ASVspoof2021 DeepFake dataset to produce a diverse and balanced dataset for model development.

The resulting system demonstrates how modern deep learning techniques can be applied to detect synthetic speech in real time while providing a practical deployment solution through an interactive dashboard.

# 3. Project Objectives

The primary objective of this project was to design, develop, evaluate, and deploy an artificial intelligence system capable of automatically distinguishing between authentic and AI-generated voice recordings.

The system was developed as a complete end-to-end solution that addresses every stage of the machine learning pipeline, from dataset preparation to real-time deployment.

To achieve this objective, the following goals were defined:

- Develop a reliable voice deepfake detection system using state-of-the-art deep learning models.
- Build a comprehensive dataset by combining public anti-spoofing datasets with a custom Hebrew dataset developed specifically for this project.
- Generate synthetic Hebrew deepfake recordings using the ElevenLabs API in order to overcome the limited availability of Hebrew voice spoofing datasets.
- Train and evaluate multiple deep learning architectures under identical experimental conditions to enable a fair comparison.
- Compare model performance using both classification metrics and computational efficiency measurements.
- Identify the most suitable model for deployment based on overall performance, robustness, and resource requirements.
- Develop an interactive web application that enables real-time analysis of uploaded audio recordings.
- Store prediction results in a local SQLite database to support historical analysis and statistical reporting.
- Provide users with intuitive visualizations and analytical summaries through an interactive dashboard.
- Demonstrate a practical deployment scenario for AI-based voice deepfake detection that can serve as a foundation for future cybersecurity applications.

The project extends beyond the development of a single classification model by presenting a complete deployment pipeline, including data preparation, model development, performance evaluation, statistical analysis, database integration, and an operational web-based interface.

The final outcome is an integrated AI-powered system capable of detecting voice deepfakes in real time while providing transparent prediction results, confidence scores, historical records, and statistical insights through an intuitive user interface.
# 4. System Architecture

The SmartDetect AI system was designed as a complete end-to-end machine learning pipeline that covers every stage required for AI-based voice deepfake detection.

The project consists of several interconnected modules, beginning with dataset preparation and ending with a fully deployed web application capable of performing real-time voice analysis.

The overall architecture is illustrated by the following workflow:

```
Data Collection
        │
        ▼
Dataset Preparation
        │
        ▼
Hebrew Deepfake Generation
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Statistical Analysis
        │
        ▼
Model Selection
        │
        ▼
Deployment (Streamlit Dashboard)
```

Each stage of the architecture is described below.

---

## Data Collection

The project combines multiple data sources in order to build a diverse dataset for training and evaluation.

The datasets include:

- ASVspoof2021 DeepFake (public anti-spoofing dataset)
- Mozilla Common Voice Hebrew
- AI-generated Hebrew recordings created using the ElevenLabs API

These datasets provide both authentic and synthetic speech samples for binary classification.

---

## Dataset Preparation

The collected recordings undergo several preprocessing steps before training.

The preparation pipeline includes:

- Dataset analysis
- Balanced selection of spoofing attack types
- Selection of authentic Hebrew recordings
- Generation of synthetic Hebrew recordings
- Audio normalization
- Train, validation, and test split

The final dataset combines public English recordings with custom Hebrew recordings while maintaining balanced class distributions.

---

## Deep Learning Models

Four deep learning architectures were implemented and evaluated:

- WavLM
- Wav2Vec2
- AASIST
- RawNet3

Each model was trained independently using the same dataset split and evaluation methodology to ensure a fair comparison.

---

## Model Evaluation

The trained models were evaluated using multiple classification and computational metrics.

Performance comparison included:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Error Rate
- Model Size
- Number of Parameters
- Memory Consumption
- Inference Time

Additional recording-level analyses were performed to investigate common classification errors and model robustness across different spoofing attack types.

---

## Model Selection

Following the evaluation phase, WavLM demonstrated the best overall trade-off between detection performance and computational efficiency.

Based on these results, WavLM was selected as the final deployment model.

---

## Deployment

The selected WavLM model was integrated into a Streamlit web application.

The deployed system provides:

- Audio upload
- Automatic preprocessing
- Real-time inference
- Confidence estimation
- History management
- Statistical analytics
- Project information page

The dashboard stores prediction results in a local SQLite database, enabling users to review previous analyses and monitor overall system performance through interactive visualizations.

---

## Repository Organization

To improve maintainability, the repository is divided into dedicated modules representing the different stages of the project:

- **data preparation** – Dataset construction and preprocessing.
- **models** – Training and evaluation of all deep learning models.
- **statistical summary** – Statistical analyses, evaluation tables, and comparison figures.
- **database** – SQLite database implementation and schema.
- **voice_dashboard** – Streamlit deployment application.

This modular structure allows every stage of the machine learning workflow to be reproduced independently while maintaining a clear separation between data preparation, model development, evaluation, and deployment.

