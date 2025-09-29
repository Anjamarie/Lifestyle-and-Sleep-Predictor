README.md
Sleep Quality Prediction Analysis
Project Overview
This project explores the relationship between various lifestyle and health metrics and an individual's sleep quality. The primary objective is to develop a robust machine learning model capable of accurately predicting a "Quality of Sleep" score based on a variety of features, demonstrating a complete and thorough data science workflow.

Methodology and Analysis
The analysis was performed using a machine learning pipeline to ensure a streamlined and reproducible process. The key steps included:
* 		Data Preprocessing and Feature Engineering: The raw data was prepared for modeling by applying transformations to both numerical and categorical features. Numerical features were scaled using StandardScaler to normalize their ranges, while categorical features were converted into a numerical format using OneHotEncoder.
* 		Baseline Model Creation: A baseline was established using a simple Linear Regression model to provide a point of comparison for more complex algorithms.
* 		Model Optimization: The project's core predictive model is a Random Forest Regressor. To ensure optimal performance, GridSearchCV was used for comprehensive hyperparameter tuning, systematically exploring a grid of parameter values to identify the best-performing model configuration.
* 		Model Evaluation: The final, optimized model was evaluated on unseen test data using key performance metrics, including Mean Absolute Error (MAE) and the R-squared (R2) score.
* 		Predictive Application & Visualization: The project demonstrates the practical application of the model by saving it using joblib and using it to make a prediction on a new, unseen data point. Additionally, key relationships within the data were visualized through plots to gain a deeper understanding of the factors influencing sleep quality.

Key Findings
# Feature Importance  ![Bar chart showing the importance of different lifestyle features in predicting sleep quality](visualizations/Sleep_Features.png)
The comparison between the baseline Linear Regression model and the optimized Random Forest Regressor revealed significant insights into the predictive power of the features. The optimized model achieved superior performance, confirming the effectiveness of hyperparameter tuning. The project also included a feature importance analysis to highlight which specific metrics were most influential in predicting sleep quality.
The final result is a production-ready model that is both highly accurate and interpretable, providing a strong foundation for future research or application.
# Sleep Quality by Occupation ![Boxplot showing the different sleep qualities based on occupation](visualizations/Sleep_occupation_duration.png)

# Comparison of the Relationship Between Sleep Duration and Quality ![Scatterplot showing the relationship between sleep duration and quality of sleep](visualizations/Relationship_duration_quality.png)









