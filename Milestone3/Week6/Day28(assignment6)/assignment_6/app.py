# app.py

import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
from sklearn.datasets import load_iris

# --- Page Configuration ---
st.set_page_config(
    page_title="Iris Species Predictor",
    page_icon="🌸",
    layout="centered"
)

# --- Load Model and Data ---
# Load the pre-trained model and target names
model = joblib.load('model.joblib')
target_names = joblib.load('target_names.joblib')

# Load the full Iris dataset for the exploration page
iris_data = load_iris()
df_iris = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
df_iris['species'] = [iris_data.target_names[i] for i in iris_data.target]


# --- Sidebar for Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page:", ["Prediction", "Data Exploration"])

# --- Prediction Page ---
if page == "Prediction":
    st.title("🌸 Iris Flower Species Predictor")
    st.markdown(
        "This app predicts the species of an Iris flower based on its sepal and petal measurements."
    )

    st.sidebar.header("Input Features")
    st.sidebar.markdown("Use the sliders to input the flower's measurements.")

    # Input widgets for user features in the sidebar
    sepal_length = st.sidebar.slider('Sepal Length (cm)', 4.0, 8.0, 5.4)
    sepal_width = st.sidebar.slider('Sepal Width (cm)', 2.0, 4.5, 3.4)
    petal_length = st.sidebar.slider('Petal Length (cm)', 1.0, 7.0, 1.6)
    petal_width = st.sidebar.slider('Petal Width (cm)', 0.1, 2.5, 0.4)

    # Store inputs into a DataFrame
    input_data = pd.DataFrame({
        'sepal length (cm)': [sepal_length],
        'sepal width (cm)': [sepal_width],
        'petal length (cm)': [petal_length],
        'petal width (cm)': [petal_width]
    })

    st.subheader("Your Input Measurements")
    st.write(input_data)

    # Prediction button
    if st.button("Predict Species", key='predict_button'):
        # Make prediction
        prediction_index = model.predict(input_data)[0]
        prediction_name = target_names[prediction_index]

        # Get prediction probabilities
        prediction_proba = model.predict_proba(input_data)

        # Display the prediction result
        st.subheader("Prediction Result")
        if prediction_name == 'setosa':
            st.success(f"The predicted species is **{prediction_name.title()}** 🌺")
        elif prediction_name == 'versicolor':
            st.info(f"The predicted species is **{prediction_name.title()}** 🌻")
        else: # virginica
            st.warning(f"The predicted species is **{prediction_name.title()}** 🌷")

        # Display prediction probabilities
        st.subheader("Prediction Probabilities")
        proba_df = pd.DataFrame(prediction_proba, columns=target_names)
        st.write(proba_df)


# --- Data Exploration Page ---
elif page == "Data Exploration":
    st.title("📊 Data Exploration")
    st.markdown("Explore the Iris dataset used to train the model.")

    # Show the full dataset
    st.subheader("Full Iris Dataset")
    st.dataframe(df_iris)

    st.markdown("---")

    # Layout with columns for visualizations
    col1, col2 = st.columns(2)

    with col1:
        # Histogram of features
        st.subheader("Feature Histograms")
        feature_to_plot = st.selectbox("Select a feature for histogram:", df_iris.columns[:-1])
        fig_hist = px.histogram(df_iris, x=feature_to_plot, color='species',
                                title=f"Histogram of {feature_to_plot}")
        st.plotly_chart(fig_hist, use_container_width=True)

    with col2:
        # Scatter plot of feature pairs
        st.subheader("Feature Scatter Plot")
        x_axis = st.selectbox("Select X-axis feature:", df_iris.columns[:-1], index=0)
        y_axis = st.selectbox("Select Y-axis feature:", df_iris.columns[:-1], index=1)
        fig_scatter = px.scatter(df_iris, x=x_axis, y=y_axis, color='species',
                                 title=f"Scatter Plot: {x_axis} vs {y_axis}")
        st.plotly_chart(fig_scatter, use_container_width=True)