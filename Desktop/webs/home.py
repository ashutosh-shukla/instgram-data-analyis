import pandas as pd
import streamlit as st
from io import BytesIO
import requests
from PIL import Image
from bs4 import BeautifulSoup

# Function to scrape Instagram profile picture URL
def get_instagram_profile_picture(username):
    url = f'https://www.instagram.com/{username}/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    meta_tag = soup.find('meta', property='og:image')
    if meta_tag:
        return meta_tag['content']
    return None

# Load data
df = pd.read_excel('file.xlsx')

# Display profiles in rows with 3 columns
num_columns = 3
num_profiles = len(df)

for i in range(0, num_profiles, num_columns):
    cols = st.columns(num_columns)
    for j in range(num_columns):
        if i + j < num_profiles:
            profile = df.iloc[i + j]
            with cols[j]:
                # Get the Instagram profile picture URL
                profile_picture_url = get_instagram_profile_picture(profile['Username'])
                
                if profile_picture_url:
                    try:
                        # Add headers to mimic a browser request
                        headers = {'User-Agent': 'Mozilla/5.0'}
                        response = requests.get(profile_picture_url, headers=headers)
                        response.raise_for_status()  # Raise an error for bad HTTP responses
                        
                        # Check if the content type is an image
                        if 'image' in response.headers.get('Content-Type', ''):
                            img = Image.open(BytesIO(response.content))
                            st.image(img, use_column_width=True)
                        else:
                            st.write(f"URL does not point to an image: {profile_picture_url}")
                    except Exception as e:
                        st.write(f"Error loading image for {profile['Username']}: {e}")
                else:
                    st.write(f"Could not retrieve profile picture for {profile['Username']}")
                
                st.markdown(f"**{profile['Username']}**")
                st.markdown(f"**Followers:** {profile['Followers count']}")
                st.markdown(f"**Following:** {profile['Following count']}")
                st.markdown(f"**Posts:** {profile['Posts count']}")
                st.markdown(f"**Bio:** {profile['Biography']}")
                st.markdown(f"[Visit Profile](https://www.instagram.com/{profile['Username']})", unsafe_allow_html=True)
