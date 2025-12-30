# Datahut Data Science Assignment

## Objective
The objective of this assignment is to scrape structured product data from the
Nike India website for the Women’s Footwear category and store it in a clean CSV
format for further analysis.

## Website
[Nike India – Women’s Shoes](https://www.nike.com/in/w/womens-shoes-5e1x6zy7ok)

## Tools & Technologies
- Python 3.11
- Selenium
- Pandas
- WebDriver Manager

## Scraping Approach
The Nike website loads product information dynamically using JavaScript.
Because of this, traditional HTTP requests cannot retrieve the complete product
data.

Selenium was used to automate a real browser session. The script scrolls the page
multiple times to trigger dynamic loading of product cards. Once all products are
loaded, relevant details are extracted from each product card and stored in a
structured format.

## Data Extracted
For each product, the following attributes were collected (where available):
- **Product URL**
- **Product Name**
- **Brand**
- **Sale Price**
- **MRP**

## Price Fields (MRP & Sale Price)
Nike does not consistently display the MRP for all products. In many cases,
only a single price is shown on the product listing page.

For such products, the MRP field is stored as empty (`NaN`) to accurately reflect
the source data. This behavior is documented as a limitation of the website.

## Data Cleaning
- Duplicate products were removed using the product URL.
- Rows with missing product name were dropped.
- Price values were cleaned by removing currency symbols and commas.

## Challenges Faced
- Product data loads dynamically and requires scrolling.
- Some products do not display MRP if they are not discounted.
- Website structure may change over time.

## Limitations
- The script scrolls a fixed number of times, so products loaded beyond that
  point may not be captured.
- Some product prices may be unavailable on the website.

## How to Run
1. Install Python 3.11
2. Install required libraries:
   pip install selenium pandas webdriver-manager
3. Run the script:
   python scraper.py
4. The output dataset will be saved as dataset.csv

   ```bash
   pip install selenium pandas webdriver-manager
