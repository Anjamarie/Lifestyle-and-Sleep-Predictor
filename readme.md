# Project: Sleep Quality Prediction Analysis
This is a complete data science workflow focused on predictive modeling, built to validate core machine learning and data engineering proficiency.

## Project Overview

This project explores the relationship between various lifestyle and health metrics and an individual's sleep quality (a score on a 1–10 scale). The primary objective was to develop a robust machine learning pipeline capable of accurately predicting this score, while providing clear insights into the factors that influence sleep health.
## Research Questions

To what extent do lifestyle factors (Physical Activity, Stress Levels) reliably predict subjective sleep quality?

Does the relationship between sleep duration and quality vary significantly across different occupational cohorts?

Which specific features serve as the most potent predictors of sleep hygiene?


## Conclusion and Limitations
Based on the findings and high $R^2$ they suggest that Sleep Quality is determined by the measurable behaviors such as Stress, Sleep Duration, and Physical Activity. Sleep Duration and Stress Level held the most significant weight in feature importance, suggesting that targeting thest areas will show the highest improvement of Sleep Quality. By utilizing a Random Forest over a Linear Baseline, I captured a 3% performance gain, identifying subtle non-linear thresholds where sleep quality drops sharply once stress exceeds a specific level. 

The primary limitation is the subjectivity of "Sleep Quality" scores. Incorporating objective biometrics such as REM cycles from wearable devices to cross-validate the self-reporting of sleep quality. Additionally, including a wider range on occupations and labor sector would help improve the external validity and generalizability. This analysis provides only a small glimpse at the participants' sleep quality. Adding a longitudinal tracking approach over a longer span of time would add more insight into how someone's lifestyle directly causes shifts in quality of sleep. 


## Methodology & Model Comparison

### Component	Technology / Concept Significance

#### 1. Data Engineering & Pipeline Design

Leakage Prevention: Utilized ColumnTransformer within a Pipeline to ensure that preprocessing parameters (mean/variance for StandardScaler) were fit strictly on training folds, preserving the integrity of the unseen test set.

Encoding Strategy: Implemented OneHotEncoder for categorical variables (e.g., Occupation) to prevent the model from assuming an unintended ordinal relationship between non-numeric categories.

#### 2. Baseline Model Establishment
Established a Linear Regression baseline. Achieving an $R^2$ of 0.95 suggested that the underlying relationships in the Sleep Health dataset are largely linear, providing a high-confidence benchmark for further non-linear experimentation.

#### 3. Model Optimization & Refinement

Advanced Model Selection: Systematically optimized performance using a Random Forest Regressor to capture complex, non-linear relationships.

Hyperparameter Tuning: Employed GridSearchCV for exhaustive hyperparameter tuning, minimizing prediction error and achieving superior generalization.

Final Performance: Attained an optimized test performance with an $R^2$ score of 0.98, demonstrating expertise in model refinement and optimization.

#### 4. Model Deployment Preparation

Model Serialization: Serialized the final, best-performing model to disk using the joblib library, creating a portable model artifact ready for production deployment.

## Statistical Interpretation
Primary Predictors: The model identified Sleep Duration and Stress Level as the most significant drivers of sleep quality.
## Feature Importance
<img src="assets/sleep_features.png">

Non-Linear Gains: Moving from Linear Regression to a Random Forest increased accuracy by 3%, suggesting subtle non-linear interactions between Sleep Duration and Sleep Quality that traditional linear models may overlook. 
## Comparison of the Relationship Between Sleep Duration and Quality
<img src="assets/sleep_relationship.png">

Generalizability: Applied GridSearchCV with 5-fold cross-validation to ensure the model generalizes across different demographic subsets within the data.

## Sleep Quality by Occupation
<img src="assets/sleep_occupations.png">





