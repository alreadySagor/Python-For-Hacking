import requests

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Page content : ")
        print(response.text[:500])
    else:
        print(f"Failed to retrieve the page. Status code : {response.status_code}")
scrape_website("http://example.com")