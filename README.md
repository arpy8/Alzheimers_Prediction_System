# Alzheimer's Disease Prediction

## About Alzheimer's Disease
Alzheimer's disease (AD) is a progressive neurodegenerative disease. Though best known for its role in declining memory function, symptoms also include: difficulty thinking and reasoning, making judgements and decisions, and planning and performing familiar tasks. It may also cause alterations in personality and behavior. The cause of AD is not well understood. There is thought to be a significant hereditary component. For example, a variation of the APOE gene, APOE e4, increases risk of Alzheimer's disease.

## Purpose of the project
The purpose of this project proposal is to develop a machine learning model for the early prediction of Alzheimer's disease. Alzheimer's disease is a devastating neurodegenerative disorder that affects millions of individuals worldwide. Early detection is crucial for better patient care and the development of potential interventions. This project aims to leverage machine learning techniques to create a predictive model that can identify individuals at risk of Alzheimer's disease based on relevant data.

## Datasets
The ADNI dataset is a comprehensive collection of clinical, imaging, and genetic data from individuals with Alzheimer's disease. Using data provided by the ADNI Project, it is our goal to develop a computer model that assists in the diagnosis of the disease. We'll try multiple models recently popularized in machine learning (Logistic Regression, Random Forest, MLP). 

## Techniques
This project will engage a combination of machine learning techniques and data preprocessing methods to develop an accurate Alzheimer's disease prediction model:

### a. Data Preprocessing
- Data cleaning and preprocessing to handle missing values and outliers.
- Feature selection to identify the most relevant variables for prediction.

### b. Machine Learning Models
- Utilize various machine learning algorithms:
  - Logistic Regression
  - Random Forest
  - MLP Classifier
- Hyperparameter tuning and cross-validation to optimize model performance.

### c. Evaluation Metrics
- Employ appropriate evaluation metrics such as accuracy, precision, recall, F1-score, and area under the ROC curve (AUC) to assess the model's performance.
- Conduct a thorough analysis of false positives and false negatives to understand the model's strengths and weaknesses.

## Potential Impact
The potential impact of this project on the issue of Alzheimer's disease is significant:
- Early prediction of Alzheimer's disease can lead to timely interventions, potentially slowing down the progression of the disease.
- Accurate prediction models can aid in identifying suitable candidates for clinical trials and research studies.
- Providing a tool for early prediction can raise awareness about Alzheimer's disease and encourage individuals to seek early medical evaluation.

My project outlines the purpose, datasets, techniques, and potential impact of developing a machine learning model for Alzheimer's disease prediction. Early detection and intervention are crucial in addressing this pressing healthcare issue, and the proposed project aims to contribute significantly to this endeavor.

## Folder Overview
- Data  - Folder to the dataset collected and used for this project
- Model - Folder containing the final trained model

## Deployment
Final model is deployed on streamlit at : https://alzheimers-prediction.streamlit.app
