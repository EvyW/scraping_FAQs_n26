# Match n26 FAQs from different languages

This program matches the FAQs from n26 webpage in all its different languages. This is built in python using the scrapy library, a library known for being a web scraping framework that brings the advantage of low CPU and memory usage (see other [advantages](https://www.analyticsvidhya.com/blog/2020/04/5-popular-python-libraries-web-scraping/)).

Important notes:
- The main program that crawls, scraps and extract the data is [n26_match_faqs.py](https://github.com/EvyW/scraping_faqs_n26/blob/master/n26_link_faqs/spiders/n26_match_faqs.py)
- The resulting product (csv file) is [n26_matched_faqs.csv](https://github.com/EvyW/scraping_faqs_n26/blob/master/n26_matched_faqs.csv)
- For the execution, run the following in your terminal:

```
scrapy crawl n26_match_faqs

```
