name = 'quotes'
    # start_urls = [
    #     'https://quotes.toscrape.com/'
    # ]
    
    # def parse(self, response: Response):
        
    #     items = EcodataItem()
        
    #     quote_divs = response.css('div.quote')
    #     for quote_div in quote_divs:
    #         title = quote_div.css('span.text::text').get()
    #         author = quote_div.css('.author::text').get()
    #         tags = quote_div.css('.tag::text').extract()
            
    #         items['title'] = title
    #         items['author'] = author
    #         items['tags'] = tags
            
    #         yield items