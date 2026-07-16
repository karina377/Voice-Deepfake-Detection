# Models

## Overview

This folder contains the deep learning models evaluated during the development of the AI Voice Deepfake Detection System.

Several state-of-the-art architectures were implemented, trained, and evaluated to compare their ability to distinguish between authentic and AI-generated speech.

Although multiple models were successfully trained and tested, the final deployed model selected for the system was **WavLM**, based on its superior classification performance, lowest error rate, and strong overall balance between accuracy and computational efficiency.

---

## Included Models

### WavLM (`WavLM_base.ipynb`)

WavLM is a self-supervised speech representation model developed by Microsoft. It is pre-trained on large-scale speech data and learns rich acoustic and contextual representations directly from raw audio.

Unlike traditional handcrafted feature extraction methods, WavLM captures detailed speech characteristics, speaker information, and subtle acoustic artifacts that are highly effective for detecting synthetic and manipulated voices.

In this project, WavLM achieved the highest overall performance and was selected as the final deployment model.

---

### Wav2Vec2 (`wav2vec2.ipynb`)

Wav2Vec2 is a transformer-based self-supervised speech model developed by Meta (Facebook AI).

The model learns meaningful speech representations directly from raw waveforms without requiring manually extracted audio features. It has been widely adopted for speech recognition and speech classification tasks.

During evaluation, Wav2Vec2 achieved performance very close to WavLM and demonstrated excellent generalization capabilities, making it a strong alternative model.

---

### AASIST (`aasist.ipynb`)

AASIST (Audio Anti-Spoofing using Integrated Spectro-Temporal Graph Attention Networks) is a neural architecture specifically designed for audio anti-spoofing.

Unlike general-purpose speech models, AASIST focuses on identifying spoofing artifacts by modeling both temporal and spectral relationships within speech signals using graph attention mechanisms.

The model produced good detection performance after fine-tuning, although its overall accuracy remained lower than WavLM and Wav2Vec2.

---

### RawNet3 (`model_rawnet3_style.ipynb`)

RawNet3 is an end-to-end convolutional neural network that processes raw audio waveforms directly without relying on pretrained speech representations.

The architecture extracts low-level acoustic features from the waveform and performs classification using convolutional feature extraction.

RawNet3 achieved the fastest inference speed and required significantly fewer parameters than the transformer-based models. However, its detection performance was substantially lower, making it less suitable for the final deployment.

---

## Model Evaluation

All models were trained and evaluated using the same dataset split and evaluation methodology to ensure a fair comparison.

The comparison considered:

- Classification accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Error rate
- Computational efficiency
- Memory consumption
- Model size
- Inference speed

---

## Final Model Selection

Based on the complete evaluation process, **WavLM** was selected as the final deployment model because it demonstrated:

- Highest classification accuracy
- Lowest error rate
- Excellent Precision, Recall, F1-score, and ROC-AUC
- Strong robustness across different spoofing attack types
- Best overall balance between detection performance and computational efficiency

The detailed evaluation results, comparison tables, and visualizations are available in the **statistical summary** folder.
