#PATENT SCRABBLER

The stupid patent scraper.

Takes in a list of patent numbers, scrapes Google patents, and outputs a CSV containing:
    * Official Patent number
    * Title
    * Priority Date
    * Abstract
    * Filing Date
    * Publication Date
    * Number of Forward References
    * URL to Google Patent entry

Setup:

pip3 install scrapy

Run:

scrapy crawl patent_scrabbler -a inputfile="input.txt" -o "output.csv"