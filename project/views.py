import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from django.shortcuts import render

# Function to scrape Myntra (static scraping)
def scrape_myntra():
    url = "https://www.myntra.com/formal-shoes/killer/killer-men-round-toe-lace-ups-formal-derby-shoes/31602544/buy"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    # Requesting the page
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    product_name = soup.find('h1', {'class': 'pdp-title'}).text.strip() if soup.find('h1', {'class': 'pdp-title'}) else 'Product Name Not Found'
    product_price = soup.find('span', {'class': 'pdp-price'}).text.strip() if soup.find('span', {'class': 'pdp-price'}) else 'Price Not Found'
    product_description = soup.find('div', {'class': 'pdp-description'}).text.strip() if soup.find('div', {'class': 'pdp-description'}) else 'Description Not Found'

    return [{'name': product_name, 'price': product_price, 'description': product_description}]

# Function to scrape Meesho (dynamic scraping using Selenium)
def scrape_meesho():
    url = "https://www.meesho.com"
    
    # Setup Selenium with ChromeDriver
    options = Options()
    options.headless = True  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    
    # Wait for the page to load
    driver.implicitly_wait(10)  # Adjust wait time as necessary
    
    # Scrape the product name, price, and description (adjust CSS selectors)
    try:
        product_name = driver.find_element(By.CSS_SELECTOR, '.product-title').text.strip()
        product_price = driver.find_element(By.CSS_SELECTOR, '.product-price').text.strip()
        product_description = driver.find_element(By.CSS_SELECTOR, '.product-description').text.strip()
    except:
        product_name = product_price = product_description = "Data not found"

    product_details = [{
        'name': product_name,
        'price': product_price,
        'description': product_description
    }]
    
    driver.quit()
    return product_details

# View to handle API choice and display recommendations
def control_panel(request):
    recommendations = []
    
    if request.method == 'POST':
        api_choice = request.POST.get('api_choice')
        
        if api_choice == 'myntra':
            recommendations = scrape_myntra()
        elif api_choice == 'meesho':
            recommendations = scrape_meesho()
    
    return render(request, 'project/control_panel.html', {'recommendations': recommendations})
