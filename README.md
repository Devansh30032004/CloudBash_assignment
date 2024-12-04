# Myntra & Meesho Recommendation Scraper

This project is designed to scrape and display product recommendations from Myntra and Meesho using Python and Django. The scraper fetches product data from both websites and dynamically displays it on a web interface, allowing the user to choose between Myntra and Meesho APIs to view recommendations.

## Features

- **Scrape Myntra**: Fetches product details such as name, price, and images from Myntra.
- **Scrape Meesho**: Fetches product details such as name, price, and images from Meesho.
- **Dynamic Control Panel**: A Django-based interface allows the user to choose between Myntra and Meesho APIs and fetch respective recommendations.
- **Web Scraping**: Uses BeautifulSoup to parse HTML and extract relevant data.
- **HTML & CSS Styling**: Display recommendations in a user-friendly, responsive layout similar to the original websites.

## Requirements

To get started with this project, you’ll need the following software:

- Python 3.x
- Django 5.1.x
- BeautifulSoup4
- Requests

## Installation

Follow the steps below to set up the project on your local machine:

1. **Clone the repository**:
   - Clone the project repository from GitHub and navigate into the project directory.

2. **Install the required dependencies**:
   - Install all necessary Python dependencies by using the `requirements.txt` file provided in the project.

3. **Set up the Django project**:
   - Apply database migrations to set up the necessary tables and schema for the project.

4. **Run the server**:
   - Start the Django development server, which will allow you to view and interact with the project in a local environment.

5. **Access the Control Panel**:
   - Open a web browser and visit the control panel at `http://127.0.0.1:8000/`.
   - Here, you can choose between Myntra and Meesho to fetch product recommendations and see them displayed on the page.

## How It Works

### 1. **Control Panel**:
   - Users can select which API (Myntra or Meesho) they want to fetch recommendations from.
   - Upon selection, a form is submitted to the Django backend, which processes the request and scrapes data from the corresponding website.

### 2. **Web Scraping**:
   - **Myntra Scraping**: Scrapes the Myntra website to extract product details such as name, price, and image URLs.
   - **Meesho Scraping**: Scrapes the Meesho website for the same type of product details.

   The scraping is done using the **BeautifulSoup** library in Python. The HTML of each page is parsed, and product data is extracted dynamically.

### 3. **Displaying Recommendations**:
   - After fetching the data, it is displayed in a responsive and user-friendly layout, similar to Myntra or Meesho's design.
   - Each product recommendation includes its name, price, and image, presented within a neat UI using HTML and CSS.

## Project Structure

The project has the following directory structure:

- **project**: The main Django application folder.
  - `views.py`: Contains the logic to handle API selection and web scraping.
  - `urls.py`: Maps URLs to views.
  - **templates/**: Contains HTML files.
    - `control_panel.html`: The control panel interface for selecting Myntra or Meesho.
  - **static/**: Contains static files (CSS and JS).
    - **css/**: Contains CSS styles.
    - **js/**: Contains JavaScript files for front-end interactivity.
   
# Image of Home Page
https://drive.google.com/file/d/1TaD3O4D1cgJZqc00VruNylurDEyo1nSd/view?usp=sharing

## Contributions

Feel free to fork the repository and create a pull request. Contributions are welcome for improving the scraping methods, UI/UX, and adding more features.

If you have any suggestions, bug reports, or new feature requests, please feel free to open an issue on GitHub.

## License

This project is licensed under the MIT License.


