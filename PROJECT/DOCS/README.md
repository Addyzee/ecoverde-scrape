# Certificate and Product Scraper

## Project Overview

This project is designed to scrape and collect information from a website(https://www.ecco-verde.com/) that offers eco-friendly products and their associated certifications. It is part of a larger project to create a repository for product sustainability certifications. The project consists of multiple spiders, each responsible for scraping different types of data from the website. These spiders work together to gather information about certificates, product details, and additional product pages. The collected data is then exported into CSV files for easy access and analysis.
![ecoverde page](/site-screenshot.png)

## How It Works

The project is divided into different spiders, each performing a specific task:

### 1. **Certificate Spider (certificates)**

This spider visits the website's certificate page and collects the URLs for different types of certifications available for products. It also captures the titles of each certificate.

**What it Scrapes**:

- Certificate names
- URLs for certificate pages

**Output**:

- A list of certificates with their names and URLs.
- csv link: [certificates.csv](/ecodata/certificates.csv)

---

### 2. **Product Links Spider (cproducts)**

This spider gathers product links from each certificate page. It reads URLs from a previously generated CSV file containing certificates and extracts product links from those pages.

**What it Scrapes**:

- Product names
- URLs for product detail pages

**Output**:

- A CSV file containing product names and their corresponding URLs.
- csv link: [product_links.csv](/ecodata/product_links.csv)

---

### 3. **Product Page Links Spider (product_pages)**

This spider helps to collect links to additional product pages on paginated product lists. It also generates URLs for all pages related to a product, making it possible to scrape even more products.

**What it Scrapes**:

- Paginated product pages

**Output**:

- A CSV file containing URLs for all paginated product pages.

---

### 4. **Product Details Spider (products)**

This spider collects detailed information about each product, including its name, price, brand, ingredients, features, ratings, and more. It uses the product URLs from the previous steps to visit each product page and scrape the required details.

**What it Scrapes**:

- Product name
- Brand
- Price
- Ingredients
- Features
- Certificates
- Packaging type
- Ratings

**Output**:

- A CSV file containing detailed product information, including the name, features, price, ingredients, certificates, and ratings.
- csv link: [product_details.csv](/ecodata/product_details.csv)

---

## Summary of Output

After running the spiders, you will have several CSV files containing:

- **Certificate Links**: Information about available certificates and their URLs.
- **Product Links**: URLs to product detail pages from certificate pages.
- **Product Page Links**: Links to additional product pages from paginated lists.
- **Product Details**: Detailed product information like name, brand, price, ingredients, and certifications.

## Use Case

This project was created for a demonstration of EcoLoop, a market platform for eco-friendly products. The scraped data can be used to populate the platform with product information and certifications, making it easier for users to find sustainable products.
