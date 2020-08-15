# -*- coding: utf-8 -*-
import scrapy


class n26MatchFaqsSpider(scrapy.Spider):
    name = 'n26_match_faqs'
    start_urls = ['https://support.n26.com/de-at/konto-und-personliche-informationen',
                    'https://support.n26.com/en-at/account-and-personal-details',
                    'https://support.n26.com/de-de/konto-und-personliche-informationen',
                    'https://support.n26.com/en-de/account-and-personal-details',
                    'https://support.n26.com/es-es/cuenta-e-informacion-personal',
                    'https://support.n26.com/en-es/account-and-personal-details',
                    'https://support.n26.com/en-eu/account-and-personal-details',
                    'https://support.n26.com/fr-fr/compte-et-informations-personnelles',
                    'https://support.n26.com/en-fr/account-and-personal-details',
                    'https://support.n26.com/it-it/conto-e-informazioni-personali',
                    'https://support.n26.com/en-it/account-and-personal-details',
                    'https://support.n26.com/en-us/account-personal-details',
                    'https://support.n26.com/en-gb/account-and-personal-details',
                    ]

    def parse(self, response):
        print('[parse] url:', response.url)

        # extract all links from page
        all_links = response.xpath('*//a/@href').extract()

        # iterate over links
        for link in all_links:
            print('[+] link:', link)
            full_link = response.urljoin(link)
            yield scrapy.http.Request(url=full_link, callback=self.parse_page)

    def parse_page(self, response):
        #Extract data using xpath
        faq = response.selector.xpath('//h1/text()').extract()
        row_data=zip(faq)

        #Making extracted data row wise
        for item in row_data:
            #create a dictionary to store the scraped info
            scraped_info = {
                #key:value
                'page':response.url,
                'faq' : item[0], #item[0] means product in the list and so on, index tells what value to assign
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
