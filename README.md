# 🌿 Mental Health Prediction

## 📝 Overview  
This project aims to develop a **Self-Analysis Mental Health Model** to predict mental health conditions based on user-provided symptoms. Built using **machine and deep learning techniques**, the model emphasizes **accuracy, interpretability, and efficiency**.  

---

## 📊 Dataset  
The dataset used is the **Mental Health in Tech Survey**, which includes responses related to mental health conditions, workplace environments, and demographic details.  

🔗 **Dataset Link:** [Kaggle - Mental Health in Tech Survey](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey)  

---

## 🔧 Data Preprocessing  
To ensure high data quality, the following preprocessing steps were applied:  

- ✅ **Handling Missing Values** – Imputed or removed missing data.  
- ✅ **Encoding Categorical Variables** – Used label encoding for categorical features.  
- ✅ **Feature Scaling** – Standardized numerical features for consistency.  
- ✅ **Feature Selection** – Removed irrelevant/redundant features.  
- ✅ **Train-Test Split** – Divided the dataset into training and testing sets.  

---

## 🤖 Models Used For Testing 
The following models were trained and evaluated:  

- 🔹 **Logistic Regression** (Final Model) ✅  
- 🔹 Random Forest Classifier  
- 🔹 Neural Network  

📌 **Why Logistic Regression?**  
- Balanced accuracy and interpretability.  
- Suitable for binary classification tasks.  

---

## 📈 Model Evaluation  
Each model was assessed using:  

- 📌 **Accuracy** – Overall performance.  
- 📌 **Precision, Recall, & F1-score** – Performance on positive/negative cases.  
- 📌 **Confusion Matrix** – Breakdown of correct vs. incorrect predictions.  
- 📌 **ROC-AUC Score** – Classification effectiveness.  

---

## 🧐 Model Explainability  
To enhance transparency, **Local Interpretable Model-agnostic Explanations (LIME)** was used to interpret predictions, helping users understand model decisions.  

---

## 📄 Report on LLM Experimentation  
🔗 Click **[Here](https://docs.google.com/document/d/1DXcLIiOPVwPwLUHLI4pOqboWF2w5g5ksls4l15v-1PQ/edit?usp=sharing)** to view the detailed report.  

---

## 🌐 Running the Web UI (Streamlit App)  
To use the interactive web UI, run the following command in the terminal:  

```bash
streamlit run Mental-Health-Prediction/blob/main/mental_health_ui/app.py
```
---

## 🎬 Video Demonstration  

📽 **Watch the demo:** [Click Here](https://drive.google.com/file/d/1-XVn7GmRxqxC1-NOO9ZGYV7ia7xYVcfe/view?usp=drivesdk)  

_(Apologies for the watermark! 🙃)_  
