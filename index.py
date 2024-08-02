import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO

# Upload Excel file
st.title('Instagram Profile Data Analysis')
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("### Displaying first few rows of the dataset")
    st.write(df.head())

    # Randomly select users
    n = st.slider('Number of random users to select', min_value=1, max_value=len(df), value=10)
    random_users = df.sample(n=n)

    st.write("### Randomly Selected Users")
    st.write(random_users)

    # Barplot of Followers vs Posts
    st.write("### Followers vs Posts")
    fig1, ax1 = plt.subplots()
    sns.barplot(data=random_users, x='Followers count', y='Posts count', ax=ax1)
    ax1.set_title('Followers vs Posts')
    st.pyplot(fig1)

    # Pie chart of Privacy Status
    st.write("### Privacy Status Distribution")
    fig2, ax2 = plt.subplots()
    df['Is private'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax2)
    ax2.set_ylabel('')
    st.pyplot(fig2)

    # Scatterplot of Followers vs Following with Posts count hue
    st.write("### Followers vs Following with Posts Count")
    fig3, ax3 = plt.subplots()
    sns.scatterplot(data=random_users, x='Followers count', y='Following count', hue='Posts count', ax=ax3)
    ax3.set_title('Followers vs Following with Posts Count')
    st.pyplot(fig3)

else:
    st.write("Please upload an Excel file to continue.")
