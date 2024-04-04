# Web Scraping Collegesimply.com with Selenium

This repository contains Python scripts for scraping data from the Collegesimply.com website using Selenium. The data scraped includes college name, location, graduation rate, and enrollment number. The scraped data is then written into a CSV file for further analysis.

## Prerequisites

- Python 3
- Selenium
- Chrome WebDriver

Install Selenium using pip:

```bash
pip install selenium
```

Download Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your system's PATH.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/collegesimply-scraper.git
```

2. Navigate to the project directory:

```bash
cd collegesimply-scraper
```

3. Run the Python script:

```bash
python scraper.py
```

The script will initiate the web scraping process. It will loop through all the pages on Collegesimply.com, scrape the desired data, and store it in a CSV file named `colleges_data.csv`.

## Explanation

1. **Initializing Selenium**: Selenium is a powerful tool for automating web browsers. We use it to interact with the Collegesimply.com website and extract data from its pages.

2. **Looping Through Pages**: We create a loop to iterate through each page of the Collegesimply.com website. This ensures that we scrape data from all available pages, not just the first one.

3. **Scraping Data**: Using Selenium's find_element and find_elements methods, we locate the HTML elements containing the desired data (college name, location, graduation rate, and enrollment number) and extract their text.

4. **Writing to CSV**: After scraping the data, we write it to a CSV file named `colleges_data.csv` using Python's built-in CSV module. This file serves as the output of the web scraping process and can be used for further analysis.

## Conclusion

This repository provides a simple yet effective solution for scraping data from the Collegesimply.com website using Selenium. By following the instructions provided, you can easily run the scraper script and obtain valuable data for analysis. Feel free to customize the script according to your specific requirements or use it as a template for scraping other websites.
### website view

![image](https://github.com/FaeyO/webscrapping-collegesimply-website/assets/118575325/1413bfeb-1d92-4c92-bd2b-b51b5f8e2418)
