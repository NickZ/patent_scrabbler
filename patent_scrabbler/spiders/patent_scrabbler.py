# -*- coding: utf-8 -*-
import scrapy
from patent_scrabbler.items import PatentScrabblerItem

class PatentScrabblerSpider(scrapy.Spider):
    name = "patent_scrabbler"
    allowed_domains = ["google.com"]
    google_patents_url = "https://patents.google.com/patent/"
    start_urls = []
    def __init__(self, inputfile='', *args, **kwargs):
        super(PatentScrabblerSpider, self).__init__(*args, **kwargs)
        if inputfile == '':
            raise Exception("Need an input file!")
        self.inputfile = inputfile
        for line in open(inputfile):
            line = line.strip()
            if line.find("US") == -1 and line.find("WO") == -1:
                line = "US" + line
            line = self.google_patents_url + line
            self.start_urls.append(line)


    def parse(self, response):
        item = PatentScrabblerItem()
        #Use number without codes instead of the citation patent number.
        #item['patent_number'] = response.xpath('//meta[@name="citation_patent_number"]/@content').extract().pop().strip()
        item['patent_number'] = response.xpath('//meta[@itemprop="numberWithoutCodes"]/@content').extract().pop().strip()
        item['title'] = response.xpath('//meta[@name="DC.title"]/@content').extract().pop().strip()
        item['priority_date'] = response.xpath('//time[@itemprop="priorityDate"]/text()').extract().pop().strip()
        item['filing_date'] = response.xpath('//time[@itemprop="filingDate"]/text()').extract().pop().strip()
        item['publish_date'] = response.xpath('//time[@itemprop="publicationDate"]/text()').extract().pop().strip()
        forward_references = response.xpath('//tr[@itemprop="forwardReferences"]/td/a/@href').extract()
        item['num_forward_refs'] = len(forward_references)
        assignee = response.xpath('//dd[@itemprop="assigneeCurrent"]/text()').extract()
        assignee_string = ""
        for i in assignee:
            if len(assignee_string) < 1:
                assignee_string = i.strip()
            else:
                assignee_string = assignee_string + '; ' + i.strip()
        item['current_assignee'] = assignee_string
        item['abstract'] = response.xpath('//meta[@name="description"]/@content').extract().pop().strip()
        item['url'] = response.url
        return item
