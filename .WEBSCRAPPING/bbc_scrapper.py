import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Target website
url = "https://www.bbc.com/news"

# Step 2: Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract headlines (usually in <h2> tags)
headlines = soup.find_all('h2')

# Step 4: Prepare CSV file
with open("bbc_headlines.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["No", "Headline"])  # header row

    # Step 5: Write each headline
    for i, headline in enumerate(headlines[:10], 1):  # limit to first 10
        writer.writerow([i, headline.get_text(strip=True)])

print(" Headlines saved to 'bbc_headlines.csv'")
