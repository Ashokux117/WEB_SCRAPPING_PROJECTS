# **BBC News Web Scraper**

This project scrapes the latest news headlines from the **BBC News website** and saves them into a CSV file.

## **How it Works**

1. The script sends a request to the BBC News homepage using the `requests` library.
2. It parses the HTML using `BeautifulSoup`.
3. It extracts all the `<h2>` tags (which usually contain headlines).
4. It saves the top 10 headlines into a file named  **`bbc_headlines.csv`** .

### **Requirements**

Make sure you have Python 3 installed, then install the required libraries:

open terminal

pip install -r requirements.txt

**How to Run**

1. Clone this repository:
   git clone https://github.com/Ashokux117/web_scraping_bbc.git
2. Navigate to the project folder:
   cd web_scraping_bbc.
3. Run the Python script:

   python bbc_scraper.py
4. ##### After running, check the file **`bbc_headlines.csv`** — it will contain the scraped headlines.

   Here’s how your project folder should look:
5. Folder Structure (Recommended)

   web-scraping-bbc/
   │
   ├── bbc_scraper.py          ← your Python scraping code
   ├── bbc_headlines.csv       ← output file (auto-generated)
   ├── requirements.txt         ← list of Python libraries used
   └── README.md               ← project description file
