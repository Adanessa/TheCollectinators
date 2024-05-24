import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://inara.cz/starfield/starsystem/14/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract all text from the parsed HTML
    all_text = soup.get_text(separator="\n", strip=True)
    
    # Print the extracted text
    print(all_text)
else:
    print("Failed to fetch the webpage:", response.status_code)
