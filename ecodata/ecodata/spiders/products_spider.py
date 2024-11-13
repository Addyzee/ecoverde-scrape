import scrapy
from scrapy.http import Response

import csv
import os


class CertificateSpider(scrapy.Spider):
    """
    Get certificate page urls
    """

    name = "certificates"
    start_urls = ["https://www.ecco-verde.com/categories/certificates-labels"]
    custom_settings = {
        "DOWNLOAD_DELAY": 2,
        "RETRY_TIMES": 5,
        "USER_AGENT": "Mozilla/5.0 ...",
    }

    def parse(self, response):
        urls = response.css(".b-list a").xpath("@href").getall()
        titles = response.css(".b-category__title::text").extract()
        for i in range(len(titles)):
            yield {"title": titles[i], "url": response.urljoin(urls[i])}


class CPSpider(scrapy.Spider):
    """
    CP stands for Certificate Products
    Spider for getting links for products in certificate pages
    """

    name = "cproducts"
    custom_settings = {
        "DOWNLOAD_DELAY": 2,
        "RETRY_TIMES": 5,
        "USER_AGENT": "Mozilla/5.0 ...",
        "FEED_FORMAT": "csv",  # Output format
        "FEED_URI": "product_links.csv",  # Output file path
        "FEED_EXPORT_ENCODING": "utf-8",
    }

    @staticmethod
    def get_start_urls():
        urls = []
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(base_dir, "CERTIFICATES.csv") # alternatively, use all product pages csv to go through all the products
        with open(csv_path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 1:  # if the row contains both name and URL
                    urls.append(
                        row[1].strip()
                    )  
            return urls[:2]

    start_urls = get_start_urls()

    def parse(self, response):
        title = response.css('h1::text').extract_first()
        names = [name for name in response.css(".productCard__link::text").extract() if name!=' ']
        urls = response.css(".productCard__link").xpath("@href").extract()
        for i in range(len(urls)):
            yield {"certificate":title,
                   "name":names[i].strip(),
                   "url": response.urljoin(urls[i])}

class CPPagedSpider(scrapy.Spider):
    """
    CP stands for Certificate Products
    Paged means that this will be used to get links to the paginated pages within product pages 
    Spider for getting all links to other product pages in certificate product paginated pages
    """

    name = "product_pages"
    custom_settings = {
        "DOWNLOAD_DELAY": 2,
        "RETRY_TIMES": 5,
        "USER_AGENT": "Mozilla/5.0 ...",
        "FEED_FORMAT": "csv",  
        "FEED_URI": "all_product_pages.csv",  
        "FEED_EXPORT_ENCODING": "utf-8",
    }

    @staticmethod
    def get_start_urls():
        urls = []
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(base_dir, "CERTIFICATES.csv")
        with open(csv_path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 1:  # if the row contains both name and URL
                    urls.append(
                        row[1].strip()
                    )  
            return urls[:2]

    start_urls = get_start_urls()

    def parse(self, response):
        title = response.css('h1::text').extract_first()
        
        yield {"page":f"{title}_1",
                "url":response.url} 
        
        last_page = response.css(".pagination__list .pagination__item button::text").re_first(r'\d+$')
        
        if last_page:
            last_page = int(last_page)
            page_links = [f"{response.url}?page={page}#catalog-navbar" for page in range(2,last_page+1)]

            for i in range(len(page_links)):         
                yield {"page":f"{title}_{i+2}",
                    "url":page_links[i]}
                    


class ProductDetailsSpider(scrapy.Spider):
    name = "products"
    custom_settings = {
        "DOWNLOAD_DELAY": 2,
        "RETRY_TIMES": 5,
        "USER_AGENT": "Mozilla/5.0 ...",
        "FEED_FORMAT": "csv",  # Output format
        "FEED_URI": "product_details.csv",  # Output file path
        "FEED_EXPORT_ENCODING": "utf-8",
    }
    
    @staticmethod
    def get_start_urls():
        urls = []
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(base_dir, "PRODUCT_LINKS.csv")
        with open(csv_path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 1:  # if the row contains both name and URL
                    urls.append(row[2].strip())  
            return urls[1:]
        
    start_urls = get_start_urls()
    
    def parse(self, response):
        name = response.css("h1.p-heading::text").getall()
        name = " ".join(name).strip()
        image_link = response.css(".product__image").xpath("@src").getall()
        price = response.css(".p-price__retail::text").get(default="").replace("&nbsp;", " ").strip()
        features = response.css(".p-summary__list li::text").getall()
        features = [feature.strip() for feature in features]
        certificate_reps = response.css(".p-certificates__item span::text").getall()
        product_type = response.xpath("//tr[th[contains(text(), 'Product Type:')]]/td/text()").get(default="").strip()
        brand = response.xpath("//tr[th[contains(text(), 'Brand:')]]/td/a/text()").get(default="").strip()
        content_by_ethos = response.xpath("//tr[th[contains(text(), 'Content by Ethos')]]/td/text()").get(default="").strip()
        certificates = response.xpath("//tr[th[contains(text(), 'Certficates:')]]/td/a/text()").getall()
        packaging_type = response.xpath("//tr[th[contains(text(), 'Packaging Type:')]]/td/text()").get(default="").strip()
        ingredients = response.css("div.product-ingredients.inci ul li::text").getall()
        ingredients = [ingredient.strip() for ingredient in ingredients]
        rating = response.css("div.reviews__header__summary div.stars.large span strong::text").get()
        rating = rating.strip() if rating else None


        
        yield {
            "name": name,
            "brand": brand,
            "image_link": image_link,
            "features": features,
            "price": price,
            "certificate_reps": certificate_reps,
            "product_type": product_type,
            "content_by_ethos": content_by_ethos,
            "certificates": certificates,
            "packaging_type": packaging_type,
            "ingredients": ingredients,
            "rating":rating,
            "url":response.url
            
        }