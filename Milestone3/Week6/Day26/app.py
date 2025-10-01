import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.error import URLError


# --- Page Configuration ---
st.set_page_config(
    page_title="Titanic Data Analysis",
    page_icon="🚢",
    layout="wide"
)

# --- Data Loading ---
@st.cache_data
def load_data():
    """
    Loads the Titanic dataset from a public URL.
    This function is cached to improve performance.
    """
    url = "C:\\Infosys springboard\\Day26\\titanic.csv"
    data = pd.read_csv(url)
    return data

# --- Main Application ---
st.title("🚢 Titanic Dataset Analysis")
st.markdown("Explore the Titanic dataset with interactive filters and visualizations.")

# Load data and handle potential errors
try:
    df = load_data()
except (URLError, pd.errors.ParserError) as e:
    st.error(f"An error occurred while loading or parsing the data: {e}")
    st.stop()


# --- Sidebar for Filters and Customization ---
st.sidebar.header("Filter & Customize")

# Filter by passenger class
pclass_filter = st.sidebar.multiselect(
    "Select Passenger Class(es):",
    options=sorted(df["Pclass"].unique()),
    default=sorted(df["Pclass"].unique())
)

# Filter by survival status
survival_filter = st.sidebar.multiselect(
    "Select Survival Status:",
    options=[0, 1],
    format_func=lambda x: "Survived" if x == 1 else "Did not survive",
    default=[0, 1]
)

# Apply filters to the dataframe
filtered_df = df[df["Pclass"].isin(pclass_filter) & df["Survived"].isin(survival_filter)]

st.sidebar.markdown("---")

# --- Sidebar for Display Options ---
st.sidebar.header("Display Options")

# Show original or filtered data preview
if st.sidebar.checkbox("Show Data Preview", value=True):
    st.subheader("Data Preview")
    st.write(f"Showing {filtered_df.shape[0]} of {df.shape[0]} rows")
    st.dataframe(filtered_df.head())

# Show basic statistics for filtered or full data
if st.sidebar.checkbox("Show Summary Statistics", value=True):
    st.subheader("Summary Statistics")
    st.write(filtered_df.describe())

st.sidebar.markdown("---")


# --- Main Content: Visualizations ---
st.header("Visualizations")

# Create columns for layout
col1, col2 = st.columns(2)

# Plot 1: Survival Count
with col1:
    st.subheader("Survival Count")
    fig1, ax1 = plt.subplots()
    sns.countplot(x="Survived", data=filtered_df, ax=ax1, palette="viridis")
    ax1.set_xticklabels(["Did not survive", "Survived"])
    ax1.set_xlabel("Survival Status")
    ax1.set_ylabel("Number of Passengers")
    st.pyplot(fig1)

# Plot 2: Survival by Passenger Class
with col2:
    st.subheader("Survival by Passenger Class")
    fig3, ax3 = plt.subplots()
    # Create a more descriptive column for the legend
    plot_df = filtered_df.copy()
    plot_df["Status"] = plot_df["Survived"].map({0: "Did not survive", 1: "Survived"})
    sns.countplot(x="Pclass", hue="Status", data=plot_df, ax=ax3, palette="magma")
    ax3.set_xlabel("Passenger Class")
    ax3.set_ylabel("Number of Passengers")
    ax3.legend(title="Survival Status")
    st.pyplot(fig3)

st.markdown("---")

# Plot 3: Age Distribution (or other numerical column)
st.subheader("Numerical Data Distribution")
numerical_columns = df.select_dtypes(include=["float64", "int64"]).columns.to_list()
# Remove passenger ID as it's not a useful distribution
if 'PassengerId' in numerical_columns:
    numerical_columns.remove('PassengerId')

hist_col = st.selectbox(
    "Select column for histogram:",
    numerical_columns,
    index=numerical_columns.index("Age")
)
show_kde = st.checkbox("Show KDE plot", value=True)

fig2, ax2 = plt.subplots()
sns.histplot(filtered_df[hist_col].dropna(), kde=show_kde, bins=30, ax=ax2, color="teal")
ax2.set_xlabel(hist_col)
ax2.set_ylabel("Frequency")
ax2.set_title(f"Distribution of {hist_col}")
st.pyplot(fig2)

