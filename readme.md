# Project: Sleep Quality Prediction Analysis
This is a complete data science workflow focused on predictive modeling, built to validate core machine learning and data engineering proficiency.

## Project Overview

This project explores the relationship between various lifestyle and health metrics and an individual's sleep quality (a score on a 1–10 scale). The primary objective was to develop a robust machine learning pipeline capable of accurately predicting this score, while providing clear insights into the factors that influence sleep health.

## Methodology and Model Comparison

### Component	Technology / Concept	Significance

1. Data Preprocessing & Pipeline Engineering

Feature Engineering Pipeline: Engineered a robust Scikit-learn pipeline utilizing StandardScaler for numerical features and OneHotEncoder for categorical features.

Data Integrity: Implemented the pipeline within a Scikit-learn ColumnTransformer to ensure consistent data normalization and feature encoding, effectively preventing data leakage between training and test sets.

2. Baseline Model Establishment

Interpretable Baseline: Established a simple Linear Regression model as a baseline to benchmark performance.

Initial Performance: Achieved a strong initial performance with an R 
2
  score of 0.95, quantifying the minimal computational effort required for high-accuracy predictions.

3. Model Optimization & Refinement

Advanced Model Selection: Systematically optimized performance using a Random Forest Regressor to capture complex, non-linear relationships.

Hyperparameter Tuning: Employed GridSearchCV for exhaustive hyperparameter tuning, minimizing prediction error and achieving superior generalization.

Final Performance: Attained an optimized test performance with an R 
2
  score of 0.98, demonstrating expertise in model refinement and optimization.

4. Model Deployment Preparation

Model Serialization: Serialized the final, best-performing model to disk using the joblib library, creating a portable model artifact ready for production deployment.


## Feature Importance
<img src="assets/sleep_features.png">

## Sleep Quality by Occupation
<img src="assets/sleep_occupations.png">

## Comparison of the Relationship Between Sleep Duration and Quality
<img src="assets/sleep_relationship.png">




