# SmartDetect AI – Voice Deepfake Detection System
![Python](https://img.shields.io/badge/Python-3.11-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-success)
![License](https://img.shields.io/badge/License-Academic-lightgrey)

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

## Project Highlights

- End-to-end AI voice deepfake detection pipeline
- Custom Hebrew deepfake dataset generation
- Four deep learning models evaluated
- WavLM selected as the final deployment model
- Real-time Streamlit dashboard
- SQLite database integration
- Statistical evaluation and visual analytics
- Developed in collaboration with the Israel National Cyber Directorate

## Research Disclaimer

This project was developed as part of a final academic project in Information Systems in collaboration with the Israel National Cyber Directorate.

The repository is intended for research, educational, and demonstration purposes only. It is not designed or validated for production use or real-world security-critical deployments.

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
├── docs/
│
├── USER_GUIDE.md
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

## 5. Dataset Development

The project dataset was constructed by combining multiple data sources to create a diverse and balanced collection of authentic and AI-generated voice recordings.

The final dataset includes:

- **ASVspoof2021 DeepFake** – Public English anti-spoofing dataset.
- **Mozilla Common Voice** – Authentic Hebrew voice recordings.
- **ElevenLabs API** – AI-generated Hebrew deepfake recordings created specifically for this project.

To improve dataset quality, the public dataset was analyzed and balanced before being merged with the custom Hebrew recordings. The complete dataset was then divided into training, validation, and testing subsets while preserving the distribution of spoofing attack types.

Due to GitHub storage limitations, the complete dataset is hosted externally and can be downloaded using the link provided in the **Google Drive Resources** section.

For additional information regarding the dataset construction process, refer to the **data preparation** directory.


## 6. Deep Learning Models

Four state-of-the-art deep learning architectures were implemented and evaluated during this project to determine the most suitable model for voice deepfake detection.

The evaluated models include:

- **WavLM**
- **Wav2Vec2**
- **AASIST**
- **RawNet3**

Each model was trained and evaluated using the same dataset, preprocessing pipeline, and evaluation methodology to ensure a fair comparison.

Following the evaluation process, **WavLM** was selected as the final deployment model because it achieved the best overall balance between classification performance and computational efficiency.

Detailed information about the implementation, training process, and characteristics of each model is available in the **models** directory.


## 7. Model Evaluation

All evaluated models were tested using the same dataset split and identical evaluation methodology to ensure a fair and consistent comparison.

The evaluation considered both predictive performance and computational efficiency using multiple criteria, including:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Error Rate
- Model Size
- Number of Parameters
- Memory Usage
- Inference Time

In addition to the quantitative metrics, detailed recording-level analyses were performed to identify common failure cases and compare model performance across different spoofing attack types.

The complete evaluation results, statistical analyses, comparison tables, and visualizations are available in the **statistical summary** directory.


## 8. Dashboard Deployment

The selected **WavLM** model was deployed as an interactive web application using **Streamlit**, providing real-time voice deepfake detection through a simple and user-friendly interface.

The dashboard allows users to:

- Upload audio recordings for analysis.
- Receive real-time predictions.
- View confidence scores and risk levels.
- Review previous analyses through the History page.
- Explore statistical summaries through the Analytics page.
- Access project and model information through the About page.

To support these features, the application is integrated with a local **SQLite** database, which stores analysis results and provides historical data for the dashboard.

A complete description of the dashboard implementation and its components is available in the **voice_dashboard** directory.



## 9. Technologies Used

The project was developed using modern machine learning frameworks, speech processing libraries, and web technologies.

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Deep Learning | PyTorch |
| Transformer Models | Hugging Face Transformers |
| Audio Processing | Librosa, Torchaudio |
| Data Analysis | Pandas, NumPy |
| Evaluation | Scikit-learn |
| Visualization | Plotly, Matplotlib |
| Database | SQLite |
| Web Framework | Streamlit |
| Speech Generation | ElevenLabs API |
| Version Control | Git & GitHub |
| Development Environment | Google Colab, Visual Studio Code |

These technologies were used throughout the project for dataset preparation, model development, evaluation, deployment, and documentation.

## Known Limitations

- This repository presents an academic research prototype.
- The selected WavLM model was evaluated on the datasets described in this repository.
- Performance may vary on unseen datasets, languages, speakers, or newly emerging voice synthesis technologies.
- The system currently performs binary classification (Real / AI-Generated Voice).
- The dashboard is optimized for demonstration purposes and CPU inference.


## 10. Installation and Usage

The project can be executed locally by following the steps below.

### Clone the Repository

```bash
git clone https://github.com/karina377/Voice-Deepfake-Detection.git

cd Voice-Deepfake-Detection
```

### Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

### Download Required Resources

The complete dataset and the trained WavLM model are hosted externally due to GitHub file size limitations.

Download:

- Final prepared dataset
- Trained WavLM model

The download links are available in the **Google Drive Resources** section below.

### Launch the Dashboard

```bash
cd voice_dashboard

streamlit run app.py
```

Once the application starts, open the local Streamlit URL displayed in the terminal (typically `http://localhost:8501`).

### Supported Audio Formats

The dashboard supports the following audio formats:

- WAV (.wav)
- MP3 (.mp3)
- FLAC (.flac)
- OGG (.ogg)
- M4A (.m4a)

## Tested Environment

- Operating System: Windows / macOS / Linux
- Python: 3.11+
- PyTorch: 2.x
- Transformers: 5.x
- Streamlit: 1.x

## 11. Google Drive Resources

Due to GitHub file size limitations, several project resources are hosted externally on Google Drive.

The following resources are available for download:

| Resource | Description | Link |
|----------|-------------|------|
| Final Dataset | Complete dataset used for training, validation, and testing | **https://drive.google.com/drive/folders/1p9mC1oFqkztd6VPfQ5rFUNLOULFIXrpf?usp=sharing** |
| Trained WavLM Model | Final model used by the deployed dashboard | **https://drive.google.com/file/d/1fEh_y0MqQUDYNP7zRR8N3DKctvlC06Z5/view?usp=sharing** |

These resources are required for users who wish to reproduce the experiments or run the project locally.


## 12. Documentation

To keep the repository organized and easy to navigate, each major project module includes its own **README.md** file containing detailed documentation.

The available documentation includes:

| Directory | Documentation |
|-----------|---------------|
| **data preparation/** | Dataset construction, preprocessing pipeline, and Hebrew deepfake generation. |
| **models/** | Deep learning models, training process, and model descriptions. |
| **statistical summary/** | Statistical analyses, evaluation tables, visualizations, and recording-level analyses. |
| **database/** | Database schema, ERD, and SQLite implementation. |
| **voice_dashboard/** | Dashboard architecture, components, and deployment details. |

In addition, the repository includes a comprehensive **User Guide** (`USER_GUIDE.md` / `User Guide.pdf`) describing how to use the deployed dashboard.

This modular documentation structure allows readers to explore each stage of the project independently while keeping the main README concise and easy to follow.


## 13. Live Dashboard

A live version of the SmartDetect AI system is publicly available through Streamlit Community Cloud.

**Dashboard URL:**

https://voice-deepfake-detection-airrw9l4kv2pqobhb5akax.streamlit.app/

The online application allows users to:

- Upload an audio recording.
- Perform real-time voice deepfake detection.
- View confidence scores and risk levels.
- Access previous analyses through the History page.
- Explore statistical summaries through the Analytics page.
- Review project and model information through the About page.

> **Insert Dashboard Screenshot Here**

The online version provides the complete functionality of the deployed application without requiring any local installation.



## 14. Future Work

Although the developed system achieved strong performance, several improvements can further enhance its capabilities.

Possible future developments include:

- Expanding the dataset with additional authentic and AI-generated Hebrew recordings.
- Incorporating recordings from newer voice synthesis models and additional languages.
- Evaluating recently released speech foundation models for improved deepfake detection.
- Investigating ensemble learning approaches by combining multiple deep learning models.
- Extending the system to perform multi-class classification by identifying the specific spoofing technique used.
- Deploying the system as a cloud-based API for integration with external applications and cybersecurity platforms.
- Performing continuous model retraining using newly collected recordings to improve robustness against emerging deepfake technologies.

These improvements may further increase the accuracy, robustness, and practical applicability of the SmartDetect AI platform.


## 15. Authors

This project was developed as a final-year capstone project in the **Information Systems** program.

### Students

- **Karina Pisarenko**
- **Nofar Horada**

### Academic Supervisor

- **Dr. Keren Segal**

### Collaboration

This project was carried out in collaboration with the **Israel National Cyber Directorate** as part of the final-year capstone program.

### Institution

The Max Stern Yezreel Valley College, Israel
