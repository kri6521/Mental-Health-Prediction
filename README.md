# Mental-Health-Prediction

## Overview
This project aims to develop a Self-Analysis Mental Health Model to predict mental health conditions based on user-provided symptoms. The model is built using various machine learning techniques and includes interpretability features to enhance transparency.

## Dataset
The dataset used for this project is the **Mental Health in Tech Survey**, which includes responses from individuals about their mental health conditions, workplace environment, and demographic details. Data preprocessing steps have been applied to ensure data quality and improve model performance.

Link -: https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey

## Preprocessing Steps
1. **Handling Missing Values** - Missing data is imputed or removed.
2. **Encoding Categorical Variables** - Categorical features are converted into numerical representations using label encoding.
3. **Feature Scaling** - Standardization is applied to ensure uniformity across features.
4. **Feature Selection** - Irrelevant or redundant features are removed to optimize performance.
5. **Train-Test Split** - The dataset is split into training and testing subsets.

## Models Used
The following models have been implemented and evaluated:
- **Logistic Regression**
- **Random Forest Classifier**
- **Neural Network**

## Model Evaluation
Each model is evaluated using:
- **Accuracy**
- **Precision, Recall, and F1-score**
- **Confusion Matrix**
- **ROC-AUC Score**

## Model Explainability
To enhance interpretability, **Local Interpretable Model-agnostic Explanations (LIME)** is used to provide insights into individual predictions.

## Running the Web UI (Streamlit App)
To use the interactive web-based UI:
#### Run **streamlit run app.py** in the terminal.
- This will launch a web application where the user will get the output based on their input symptons.




