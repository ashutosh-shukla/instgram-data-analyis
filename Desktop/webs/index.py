from bs4 import BeautifulSoup
import requests

username = 'ashu19_06_'
url = f'https://www.instagram.com/{username}/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
profile_picture_url = soup.find('meta', property='og:image')['content']
