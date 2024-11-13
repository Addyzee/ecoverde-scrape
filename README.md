# Ecco Verde Eco Product Scraper

This project scrapes eco-friendly product information from Ecco Verde, including details about product certifications, pricing, ingredients, and more.

## Requirements
- **Python Version**: 3.10.2
- **Dependencies**: Install from `requirements.txt`

## Spiders Overview
The following spiders are included in this project:

### 1. `certificates` Spider
Use this spider to scrape eco product certification URLs.

**Command**:
```bash
scrapy crawl certificates
```
#### Output:

Saves data to `certificates.csv`<br>
Sample output:
```
{"title": certificate_title, "url": certificate_url}
```
```
title,url
AIAB,https://www.ecco-verde.com/categories/aiab
```
### 2. products Spider
This spider collects detailed information on each product.

Command:
```
scrapy crawl products
```

#### Output:

Saves data to `product_details.csv`<br>
Sample output:
```json
{
  "name": product_name,
  "brand": product_brand,
  "image": product_image_link,
  "price": product_price,
  "certificate_representation": certificate_from_image,
  "content_by_ethos": content_by_ethos,
  "certificates": certificates,
  "packaging_type": packaging_type,
  "ingredients": ingredients,
  "rating": rating,
  "url": product_url
}
```

```csv
name,brand,image_link,features,price,certificate_reps,product_type,content_by_ethos,certificates,packaging_type,ingredients,rating,url
"Active Conditioner Concentrate, 200 ml",Biofficina Toscana,https://ec.nice-cdn.com/upload/image/product/large/default/19771_3265294b.256x256.jpg,"For damaged & dry hair,Nourishes your hair,Adds volume and leaves hair silky soft","€ 13,89","AIAB,Leaping Bunny,Nickel tested,Unisex,Vegan",Hair Care,"Nickel tested,     Unisex,     Vegan","AIAB,Leaping Bunny,Vegan - Uncertified ",Tube,"Aqua (Water),Behenamidopropyl Dimethylamine,Phaseolus vulgaris extract,Chamomilla Recutita (Matricaria) Flower Extract,Citrus Medica Limonum (Lemon) Peel Oil,Glycerin,Xanthan Gum,Limonene,Linalool,Sodium Dehydroacetate,Sodium benzoate","4.6",https://www.ecco-verde.com/biofficina-toscana/active-conditioner-concentrate
```
### 3. product_pages Spider
This spider retrieves all page links for products.<br>
Command:
```
scrapy crawl product_pages
```

#### Output:
Saves links to `product_pages.csv`

<br>

**To scrape all product details from multiple pages, you can update the `csv_path` variable in the CPSpider spider to point to `product_pages.csv`**



