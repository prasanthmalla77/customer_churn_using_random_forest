# Customer Churn Prediction

Welcome to my Customer Churn Prediction project! This repository contains a comprehensive analysis of customer churn using machine learning techniques. The goal of this project is to predict which customers are likely to leave a service, based on their interactions and features.

## Project Overview

This project explores the Customer Churn dataset and demonstrates the application of various data preprocessing and machine learning techniques. The main steps include data cleaning, feature selection, model training, evaluation, and prediction.

## Table of Contents

- [Project Description](#project-description)
- [Dataset](#dataset)
- [Steps and Methodology](#steps-and-methodology)
- [Evaluation Metrics](#evaluation-metrics)
- [Code Walkthrough](#code-walkthrough)

## Project Description

The project involves analyzing customer data to predict churn using a Random Forest Classifier. Key objectives include:
- Preprocessing data to handle missing values and categorical variables.
- Training a Random Forest Classifier to model customer churn.
- Evaluating model performance using various metrics.
- Providing detailed documentation for each step to ensure reproducibility and understanding.

## Dataset

The dataset used in this project is the [Customer Churn dataset](https://github.com/prasanthmalla77/customer_churn_using_random_forest/blob/main/Customer-Churn.csv) which includes features related to customer demographics, services, and usage. 

## Steps and Methodology

1. **Data Preprocessing**:
   - Cleaned and transformed the dataset.
   - Handled missing values and non-numeric entries.
   - Encoded categorical variables.

2. **Feature and Target Selection**:
   - Separated features and target variable.

3. **Model Training**:
   - Utilized a Random Forest Classifier with 100 estimators.
   - Trained the model on the processed data.

4. **Evaluation**:
   - Assessed model performance using accuracy, classification reports, and confusion matrices.
   - Tested the model with individual instances to understand predictions and probabilities.

5. **Documentation**:
   - Added clear explanations and comments for each step to facilitate understanding for new users.

## Evaluation Metrics

The model's performance is evaluated using:
- **Accuracy**: Proportion of correct predictions.
- **Classification Report**: Precision, recall, F1-score, and support for each class.
- **Confusion Matrix**: Visualization of true vs. predicted values.

## Code Walkthrough

The repository contains the following key files:
- `customer_churn_analysis.ipynb`: Jupyter notebook with the complete analysis and code.
- `data/Customer-Churn.csv`: Dataset used for the analysis.
- `README.md`: Documentation for the project.

