import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
import joblib  # Use this line to import joblib

# Load the trained RandomForest model
model = joblib.load('random_forest_model.joblib')

# Function to preprocess input data
def preprocess_input(input_data, preprocessor):
    # Create a DataFrame with user input
    user_input_df = pd.DataFrame(input_data, columns=numerical_features + categorical_features)

    # Preprocess user input using the pre-trained ColumnTransformer
    user_input_preprocessed = preprocessor.transform(user_input_df)

    return user_input_preprocessed

# Streamlit app
st.title('Revenue Prediction App')

# User input form
st.sidebar.header('User Input Features')

# Create input fields for each feature used during training
amount = st.sidebar.number_input('Amount (converted)')
age = st.sidebar.number_input('Age')
employees = st.sidebar.number_input('Employees')
opportunity_owner = st.sidebar.text_input('Opportunity Owner')
# Repeat for other categorical features

# Combine user input into a DataFrame
user_input = pd.DataFrame({
    'Amount (converted)': [amount],
    'Age': [age],
    'Employees': [employees],
    'Opportunity Owner': [opportunity_owner],
    # Include other categorical features with appropriate values
})

# Preprocess the user input using the pre-trained ColumnTransformer
user_input_preprocessed = preprocess_input(user_input, preprocessor)

# Make predictions
prediction = model.predict(user_input_preprocessed)

# Display prediction
st.write('Prediction:', prediction)
