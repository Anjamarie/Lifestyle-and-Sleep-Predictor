import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- 1. Load the Saved Model, Features, and Mappings ---
try:
    model = joblib.load('movie_revenue_model.pkl')
    model_features = joblib.load('model_features.pkl')
except FileNotFoundError:
    st.error("Model or features not found. Please re-run your training notebook to save them.")
    st.stop()

# --- 2. Build the User Interface ---
st.title('🎬 Movie Revenue Predictor')
st.write("Enter the movie's details to predict its potential revenue.")

# Identify the genre columns the model was trained on
genre_cols = [col for col in model_features if col.startswith('genre_')]
display_genres = sorted([col.replace('genre_', '') for col in genre_cols]) # Sort for better UI

with st.sidebar:
    st.header("Movie Features")
    budget = st.number_input('Budget (in USD)', min_value=10000, max_value=400000000, value=50000000, step=1000000)
    runtime = st.number_input('Runtime (in minutes)', min_value=60, max_value=240, value=120)
    selected_genres = st.multiselect('Select Genres', options=display_genres)
    release_year = st.number_input('Release Year', min_value=1980, max_value=2025, value=2023)
    release_month = st.slider('Release Month', 1, 12, 6)
    release_dayofweek = st.slider('Release Day of Week (0=Monday, 6=Sunday)', 0, 6, 4)
    # NOTE: For a full app, you would add inputs for director, cast, etc.
    # We are simplifying here by using average values for those features.

# --- 3. Prepare Input for Prediction ---
# Create a DataFrame with all the feature columns and default values of 0
input_data = {col: [0] for col in model_features}
input_df = pd.DataFrame(input_data)

# Update the DataFrame with the user's direct inputs
input_df['budget'] = budget
input_df['runtime'] = runtime
input_df['release_year'] = release_year
input_df['release_month'] = release_month
input_df['release_dayofweek'] = release_dayofweek

# Set the selected genre columns to 1
for genre in selected_genres:
    genre_column_name = f'genre_{genre}'
    if genre_column_name in input_df.columns:
        input_df[genre_column_name] = 1
        
# For other engineered features (like mean revenues), we'll use placeholder values.
# In a real-world scenario, you would have a more complex way to handle new directors/actors.
for col in model_features:
    if col.startswith('mean_') and col not in input_df.columns:
        # A simple placeholder: use an average value or 0
        input_df[col] = 0

# --- 4. Make a Prediction ---
if st.sidebar.button('Predict Revenue'):
    prediction = model.predict(input_df)
    st.subheader('Predicted Revenue:')
    st.success(f'${prediction[0]:,.2f}')