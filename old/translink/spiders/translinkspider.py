# -*- coding: utf-8 -*-
import scrapy

import json, os, sys

pdf_links_file = "tmp/pdf_links.json"
if os.path.exists(pdf_links_file):
  pdf_links = json.loads(open(pdf_links_file).read())
else:
  sys.exit(1)

print "Info: Loaded (" + str(len(pdf_links))  + ") potential pdf links"

class TranslinkspiderSpider(scrapy.Spider):
    name = "translinkspider"
    allowed_domains = ["translink.co.uk"]
    start_urls = tuple(pdf_links)

    def parse(self, response):
        url_sublink = response.xpath('//a/@href').extract()[0]
        url_sublink = url_sublink.split('/')[2:]
        url_sublink = '/'.join(url_sublink)
        url = response.urljoin(url_sublink)
        yield scrapy.Request(url, callback=self.save_pdf)

    def save_pdf(self, response):
        filename = response.url.split('/')[-1]
        with open('tmp/' + filename, "wb") as f:
            f.write(response.body)
