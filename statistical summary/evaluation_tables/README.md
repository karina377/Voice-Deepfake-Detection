# Evaluation Tables

## Overview

This folder contains the summary tables used to compare the performance of the evaluated deep learning models.

The tables summarize the experimental setup, classification performance, and the final model selection process. These tables were used throughout the evaluation phase of the project and support the final decision regarding the deployed model.

---

## table_1_experiments_parameters.csv

This table summarizes the training configuration used for each evaluated model.

It includes:
- Model name
- Learning rate
- Batch size
- Number of training epochs
- Fine-tuning information

The table provides a concise overview of the experimental settings applied to each model and highlights any modifications performed during training (e.g., increasing the number of epochs for the AASIST model).

---

## table_2_classification_metrics.csv

This table presents the primary classification performance metrics obtained on the test dataset.

The reported metrics include:
- Precision
- Recall
- F1-Score
- ROC-AUC

These metrics enable a quantitative comparison of the classification capabilities of all evaluated models.

---

## table_3_model_ranking_selection.csv

This table summarizes the final ranking of the evaluated models.

For each model, the table presents:
- Final ranking
- Overall accuracy
- Main strengths
- Final deployment decision

The ranking reflects the overall evaluation process by considering both classification performance and practical deployment considerations. Based on this evaluation, WavLM was selected as the final model for deployment, while Wav2Vec2 was identified as a suitable candidate for future ensemble integration.
