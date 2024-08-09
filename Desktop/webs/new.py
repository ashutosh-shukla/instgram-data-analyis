import streamlit as st
import pandas as pd
import requests

# Function to fetch JSON data from the given URL
def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

# Main function to display data
def main():
    st.title("Instagram Data Viewer")

    # URL with JSON data
    url = "https://graph.facebook.com/v20.0/17841464683953284?fields=business_discovery.username(nature_world_cool){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count,media{id,caption,like_count,comments_count,timestamp,username,media_product_type,media_type,owner,permalink,media_url,children{media_url}}}&access_token=EAB0BwgX7iMsBO1cZBB82BZB7iXzzE0YjE3cKc7c74bNZCIUMZAc4q6qDZCDolhzQFVyvcuXMzwNZC4atUGqHC7nAeeqpZCz3oiiQzPMvAZAinpgIgp2q0im3BoSZAABFhqTL4fMNuiAzBuvfshG1IzGIUWY72zTbaTeDKIl6conWOZAJibpxHaqU1mR0HatZBvd9bH2ZCg1UMxqA6IiS3e0ChripoxCstwZDZD"

    # Fetch the data
    data = fetch_data(url)
    
    if data:
        # Display the data as a JSON object
        st.write("### Raw JSON Data")
        st.json(data)
        
        # Convert JSON data to a Pandas DataFrame
        if 'business_discovery' in data:
            business_discovery = data['business_discovery']
            # Flatten the JSON structure for display
            df = pd.json_normalize(business_discovery)
            st.write("### Data as Table")
            st.table(df)

if __name__ == "__main__":
    main()
