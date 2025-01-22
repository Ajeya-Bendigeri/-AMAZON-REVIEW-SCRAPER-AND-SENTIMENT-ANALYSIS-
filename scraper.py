import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.in/Apple-New-iPhone-12-128GB/dp/B08L5TNJHG/"

def scrape_reviews(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    reviews = []
    
    review_elements = soup.select(".a-section.review.aok-relative")  
    
    print(f"Found {len(review_elements)} review elements.")  
    
    for review in review_elements:
        title_element = review.select_one(".review-title-content span")
        text_element = review.select_one(".review-text-content span")

        title = title_element.text.strip() if title_element else "N/A" 
        text = text_element.text.strip() if text_element else "N/A"

        style_name = "128GB"  
        color = "Black"  
        verified_purchase = "Verified Purchase" in review.text

        reviews.append({
            "Review Title": title,
            "Review Text": text,
            "Style Name": style_name,
            "Colour": color,
            "Verified Purchase": verified_purchase
        })
    
    return reviews

scraped_data = scrape_reviews(url)

df = pd.DataFrame(scraped_data)
df.to_csv('iphone_reviews.csv', index=False)