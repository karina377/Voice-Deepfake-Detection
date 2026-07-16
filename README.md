# SmartDetect AI – Voice Deepfake Detection System

1. Project Overview
2. Background and Motivation
3. Project Objectives
4. System Architecture
5. Repository Structure
6. Dataset Development
7. Data Preparation Pipeline
8. Deep Learning Models
9. Model Evaluation
10. Statistical Analysis
11. Dashboard Deployment
12. Database
13. Technologies Used
14. Installation Guide
15. Running the Dashboard
16. Google Drive Resources
17. Live Dashboard
18. Repository Documentation
19. Project Results
20. Future Work
21. Authors
22. Acknowledgments


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

# 5. Repository Structure

The repository is organized into dedicated modules that represent the different stages of the project lifecycle, from dataset preparation to model deployment.

Each major directory contains its own **README.md** file providing detailed documentation of its contents, workflow, and generated outputs.

The overall repository structure is shown below.

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

## Repository Modules

### data preparation/

Contains all scripts, notebooks, and metadata used to construct the final dataset.

This module includes dataset analysis, balanced sample selection, Hebrew data generation using the ElevenLabs API, and creation of the final training, validation, and testing datasets.

---

### models/

Contains the implementation, training, fine-tuning, and evaluation of all deep learning models investigated throughout the project.

The evaluated architectures include:

- WavLM
- Wav2Vec2
- AASIST
- RawNet3

Following the evaluation phase, **WavLM** was selected as the final deployment model.

---

### statistical summary/

Contains all statistical analyses generated during the evaluation phase.

This module includes:

- Evaluation tables
- Performance comparison figures
- Recording-level analyses
- Statistical notebooks

The results presented in this folder were used to compare the evaluated models and support the final model selection.

---

### database/

Contains the SQLite database implementation together with the Entity-Relationship Diagram (ERD) and database creation scripts.

The database stores the prediction history generated by the deployed dashboard and supports the History and Analytics pages.

---

### voice_dashboard/

Contains the complete Streamlit application developed for the deployment stage of the project.

The dashboard integrates the trained WavLM model and provides an interactive interface for real-time voice deepfake detection, historical record management, and statistical visualization.

---

## Documentation

Each major directory contains its own **README.md** file describing:

- Folder purpose
- Workflow
- Generated files
- Outputs
- Technical implementation

This hierarchical documentation structure keeps the repository organized while allowing every module to be understood independently.

# 6. Dataset Development

A reliable and diverse dataset is one of the most critical components of any deep learning system. Since the performance of a classification model depends heavily on the quality and diversity of the training data, significant effort was invested in constructing a dataset suitable for voice deepfake detection.

Rather than relying solely on publicly available datasets, this project combines multiple data sources and introduces a custom Hebrew dataset developed specifically for this research.

The final dataset consists of authentic and AI-generated voice recordings collected from different sources, providing a balanced and diverse collection of speech samples for model training and evaluation.

---

## Public Anti-Spoofing Dataset

The primary public dataset used in this project is **ASVspoof2021 DeepFake (DF)**.

This dataset contains a large collection of English speech recordings, including both authentic recordings and AI-generated deepfake speech created using multiple voice synthesis and voice conversion techniques.

The ASVspoof2021 dataset was selected because it is one of the most widely used benchmarks for evaluating voice anti-spoofing systems and provides recordings generated using a variety of spoofing attacks.

However, the original dataset presents an imbalanced distribution of spoofing attack types. Some attack categories contain significantly more recordings than others, which may introduce bias during model training.

To address this issue, a balanced subset of recordings was created during the data preparation stage.

---

## Hebrew Voice Dataset

One of the major challenges encountered during this project was the limited availability of publicly accessible Hebrew datasets for voice deepfake detection.

Most existing anti-spoofing datasets are based on English speech and therefore do not adequately represent the phonetic and linguistic characteristics of the Hebrew language.

To overcome this limitation, authentic Hebrew recordings were collected from the **Mozilla Common Voice** project.

A subset of recordings was carefully selected to match the desired dataset size and to ensure compatibility with the public anti-spoofing data.

---

## Generation of Hebrew Deepfake Recordings

Since publicly available Hebrew deepfake datasets are extremely limited, synthetic Hebrew recordings were generated specifically for this project.

The **ElevenLabs API** was used to create AI-generated speech from the selected authentic Hebrew recordings.

Each authentic recording was converted into a corresponding synthetic version while preserving the spoken content, resulting in paired authentic and AI-generated Hebrew samples.

This process significantly expanded the available Hebrew training data and enabled the evaluation of modern deep learning models on Hebrew speech.

---

## Final Dataset

The final dataset combines three complementary data sources:

- Authentic English recordings from the ASVspoof2021 dataset.
- Authentic Hebrew recordings from Mozilla Common Voice.
- AI-generated Hebrew recordings created using the ElevenLabs API.

After collecting all recordings, the datasets were merged into a unified dataset and divided into **training**, **validation**, and **testing** subsets.

The split was performed while preserving the distribution of the different spoofing attack types to ensure a balanced and representative evaluation dataset.

This final dataset was used consistently throughout the project for training, validation, evaluation, and comparison of all deep learning models.

---

## Dataset Availability

Due to the size of the dataset, the complete collection of recordings is not stored directly in this GitHub repository.

The final prepared dataset can be downloaded from Google Drive using the link provided in the **Google Drive Resources** section of this repository.



# 7. Data Preparation Pipeline

The data preparation stage consisted of a multi-step pipeline designed to construct a balanced and representative dataset for training and evaluating the deep learning models.

Several Python scripts and Jupyter notebooks were developed to automate the preparation process, beginning with the analysis of the public datasets and ending with the creation of the final dataset used throughout the project.

The complete workflow is illustrated below.

```
ASVspoof2021 DeepFake Dataset
            │
            ▼
      data.py
(Dataset Analysis)
            │
            ▼
   labeling_data.csv
            │
            ▼
     data_folder.py
(Balanced Attack Selection)
            │
            ▼
 Mozilla Common Voice Hebrew
            │
            ▼
 part_data_hebrew.py
(Authentic Hebrew Selection)
            │
            ▼
 api_elevenlab.ipynb
(Hebrew Deepfake Generation)
            │
            ▼
 dataset_split.ipynb
(Merge & Dataset Split)
            │
            ▼
 Final Dataset
```

---

## Step 1 – Dataset Analysis

The preparation process began with the analysis of the **ASVspoof2021 DeepFake** dataset.

The notebook **data.py** was used to examine the distribution of the available recordings and spoofing attack types.

This analysis revealed that the original dataset was highly imbalanced, with some spoofing attack types containing substantially more recordings than others.

Understanding this distribution was essential before constructing the final training dataset.

---

## Step 2 – Balanced Selection of Public Recordings

The metadata describing the ASVspoof2021 recordings is stored in **labeling_data.csv**.

Using this metadata, the script **data_folder.py** created an intermediate balanced dataset by selecting a similar number of recordings from each spoofing attack type.

Balancing the attack categories reduced dataset bias and ensured that all evaluated models were exposed to a representative distribution of spoofing techniques during training.

---

## Step 3 – Selection of Authentic Hebrew Recordings

Authentic Hebrew speech recordings were obtained from the **Mozilla Common Voice** dataset.

The notebook **part_data_hebrew.py** selected a subset of recordings whose size matched the desired dataset configuration.

These recordings served as the authentic Hebrew component of the final dataset.

---

## Step 4 – Hebrew Deepfake Generation

To compensate for the limited availability of Hebrew deepfake datasets, synthetic Hebrew recordings were generated specifically for this project.

The notebook **api_elevenlab.ipynb** used the **ElevenLabs API** to generate AI-produced versions of the selected authentic Hebrew recordings.

Each generated recording preserved the original spoken content while replacing the voice with an AI-generated version, producing paired authentic and synthetic recordings suitable for supervised learning.

Metadata describing the generated recordings was stored in **elevenlabs_hebrew.csv**.

---

## Step 5 – Final Dataset Construction

The notebook **dataset_split.ipynb** combined all available data sources into a unified dataset.

The final dataset included:

- Balanced recordings from ASVspoof2021
- Authentic Hebrew recordings
- AI-generated Hebrew recordings

After merging all recordings, the dataset was divided into:

- Training set
- Validation set
- Test set

The split was performed while preserving both the class distribution and the distribution of spoofing attack types, ensuring a fair and consistent evaluation of all deep learning models.

---

## Final Output

The resulting dataset served as the single data source used throughout the project.

All evaluated models were trained, validated, and tested using this identical dataset, guaranteeing a fair comparison between architectures.

Because of its size, the complete dataset is hosted externally and can be downloaded using the Google Drive link provided later in this README.

# 8. Deep Learning Models

A central objective of this project was to identify the most suitable deep learning architecture for detecting AI-generated voice recordings.

Rather than relying on a single model, four state-of-the-art architectures were implemented, trained, and evaluated under identical experimental conditions. This comparative approach enabled a comprehensive assessment of different modeling strategies, ranging from self-supervised transformer-based models to end-to-end convolutional neural networks specifically designed for audio anti-spoofing.

All models were trained using the same dataset, identical train-validation-test splits, and the same evaluation methodology to ensure a fair comparison.

The evaluated architectures are presented below.

---

## WavLM

WavLM (Waveform Language Model), developed by Microsoft, is a self-supervised transformer-based speech representation model trained on large-scale unlabeled speech corpora.

Unlike traditional approaches that rely on manually engineered acoustic features, WavLM learns high-level speech representations directly from raw audio waveforms. These representations capture both linguistic and speaker-specific information while preserving subtle acoustic artifacts that are particularly useful for detecting synthetic speech.

Due to its strong contextual understanding of speech signals, WavLM demonstrated excellent robustness when distinguishing authentic recordings from AI-generated voices.

---

## Wav2Vec2

Wav2Vec2, developed by Meta AI, is another self-supervised transformer architecture designed for speech representation learning.

The model learns meaningful audio representations directly from raw waveforms without requiring manually extracted features such as MFCCs or spectrograms.

Originally developed for automatic speech recognition, Wav2Vec2 has also proven highly effective for various speech classification tasks, including spoofing detection.

Within this project, Wav2Vec2 achieved competitive performance and served as one of the strongest alternatives to WavLM.

---

## AASIST

AASIST (Audio Anti-Spoofing using Integrated Spectro-Temporal Graph Attention Networks) is a deep learning architecture developed specifically for voice anti-spoofing applications.

Unlike general-purpose speech models, AASIST focuses on identifying spoofing artifacts by jointly modeling temporal and spectral relationships within speech signals through graph attention mechanisms.

Because the architecture was specifically designed for anti-spoofing, it provided valuable insight into how task-specific models compare with large self-supervised speech models.

---

## RawNet3

RawNet3 is an end-to-end convolutional neural network that performs classification directly from raw audio waveforms.

Unlike transformer-based architectures that rely on large-scale pretraining, RawNet3 extracts acoustic representations directly during supervised training.

The model offers a lightweight architecture with relatively low computational requirements and fast inference speed, making it attractive for deployment scenarios where computational efficiency is important.

However, this simplicity may reduce its ability to capture complex speech characteristics compared to large transformer-based models.

---

## Model Comparison Strategy

To ensure a fair comparison, all models were evaluated under identical experimental conditions.

The comparison considered both predictive performance and computational efficiency.

The evaluated criteria included:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Classification Error Rate
- Number of Model Parameters
- Model Size
- Memory Consumption
- GPU Memory Usage
- Average Inference Time

In addition to these quantitative metrics, recording-level analyses were performed to identify common failure cases, evaluate robustness across different spoofing attack types, and compare the behavior of each architecture on difficult recordings.

The comprehensive evaluation presented in the following chapters served as the basis for selecting the final deployment model.
