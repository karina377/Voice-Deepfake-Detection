# Statistical Summary

This directory contains the complete statistical evaluation of all deep learning models developed and tested throughout the project.

The results presented in this folder were automatically generated from the evaluation notebooks (`final_model_comparison.ipynb` and `eda.ipynb`) after testing all models on the final test dataset.

The folder is organized into three main sections:

## Folder Structure

### evaluation_tables/

Contains the final summary tables used to compare the evaluated models.

These tables include:

- Training configuration and hyperparameters
- Classification performance metrics
- Final model ranking and deployment decision

These tables provide the quantitative comparison that supported the final model selection.

---

### model_recording_analysis/

Contains detailed recording-level analysis of model predictions.

This folder includes:

- Overall error summary for each model
- Errors grouped by attack type
- Recordings classified according to the number of models that failed
- Recordings misclassified by the majority of models
- Recordings misclassified by all models
- Model efficiency statistics
- Final combined summary of accuracy and efficiency

These analyses provide a deeper understanding of model behavior, common failure cases, robustness across attack types, and computational efficiency.

---

### final_comparison_plots/

Contains visual representations of the statistical results.

The figures included in this folder are generated directly from the evaluation tables and illustrate:

- Accuracy comparison
- Correct vs. misclassified recordings
- Classification metrics comparison
- Average inference time
- Number of model parameters

These plots provide an intuitive visual summary of the numerical evaluation presented in the tables.

---

## Analysis Workflow

The statistical analysis follows the workflow below:

1. All trained models are evaluated using the final test dataset.
2. Evaluation metrics are calculated automatically.
3. Summary tables are exported to the `evaluation_tables` folder.
4. Recording-level analyses are exported to the `model_recording_analysis` folder.
5. Visual comparison figures are generated and saved in the `final_comparison_plots` folder.

Together, these files provide the complete statistical analysis performed during the model evaluation phase of the project.
