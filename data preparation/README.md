# Data Preparation

## Overview

This folder contains all scripts, notebooks, and metadata files used to prepare the final dataset for training and evaluating the deep learning models developed in this project.

The final dataset combines recordings from the public **ASVspoof2021 DF** dataset together with a custom Hebrew dataset created specifically for this project using authentic recordings and AI-generated speech.


# Data Preparation Workflow

## 1. Analysis of the ASVspoof2021 Dataset

The data preparation process began with the public **ASVspoof2021 DF Evaluation** dataset.

The script **`data.py`** was used to analyze the dataset and examine the distribution of recordings across the different spoofing attack types. During this analysis, a significant class imbalance was identified, with some attack types containing considerably more recordings than others.


## 2. Selection of a Balanced Public Dataset

The file **`labeling_data.csv`** contains the metadata describing all recordings available in the ASVspoof2021 DF Evaluation dataset.

Using this metadata, the script **`data_folder.py`** selected a balanced subset of recordings from the different spoofing attack types. This intermediate dataset ensured a more uniform distribution before combining it with additional datasets.



## 3. Selection of Authentic Hebrew Recordings

The script **`part_data_hebrew.py`** was used to select a subset of authentic Hebrew recordings from the Mozilla Common Voice dataset.

The number of selected recordings was chosen to match the desired dataset size and maintain consistency with the balanced public dataset.



## 4. Generation of Hebrew Deepfake Recordings

The notebook **`api_elevenlab.ipynb`** was used to generate AI-generated Hebrew speech using the ElevenLabs API.

Each authentic Hebrew recording was converted into a corresponding synthetic recording while preserving the original spoken content.

Metadata describing the generated recordings is stored in:

- **`elevenlabs_hebrew.csv`**



## 5. Final Dataset Construction

The notebook **`dataset_split.ipynb`** combines all prepared data sources into a single unified dataset, including:

- Balanced recordings from the ASVspoof2021 DF dataset
- Authentic Hebrew recordings
- AI-generated Hebrew recordings created using ElevenLabs

The resulting dataset is divided into **training**, **validation**, and **testing** subsets while preserving the class distribution.

Within each subset, spoof recordings are further organized according to their attack type:

- ElevenLabs Fake (custom Hebrew AI-generated recordings)
- Neural Vocoder – Autoregressive
- Neural Vocoder – Non-Autoregressive
- Traditional Vocoder
- Waveform Concatenation
- Unknown Attack Type

Authentic recordings are stored separately under the **Real** category.

The final dataset used throughout the project is available on Google Drive:

**Dataset:** `dataset_split`

**Google Drive Link:** https://drive.google.com/drive/folders/1p9mC1oFqkztd6VPfQ5rFUNLOULFIXrpf?usp=sharing



# Folder Contents

| File | Description |
|------|-------------|
| `data.py` | Analyzes the ASVspoof2021 DF dataset and examines the distribution of spoofing attack types. |
| `labeling_data.csv` | Metadata used for selecting recordings from the ASVspoof2021 DF dataset. |
| `data_folder.py` | Creates a balanced subset of recordings from different spoofing attack types. |
| `part_data_hebrew.py` | Selects authentic Hebrew recordings from Mozilla Common Voice. |
| `api_elevenlab.ipynb` | Generates AI-created Hebrew recordings using the ElevenLabs API. |
| `elevenlabs_hebrew.csv` | Metadata describing the generated Hebrew deepfake recordings. |
| `dataset_split.ipynb` | Combines all datasets and creates the final train, validation, and test splits. |
