# Scrapy settings for scrapy_site project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_site'

SPIDER_MODULES = ['scrapy_site.spiders']
NEWSPIDER_MODULE = 'scrapy_site.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_site (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
   'scrapy_site.pipelines.DuplicatesPipeline': 300,
   'scrapy_site.pipelines.ScrapySiteSavePipeline': 300,
}

CONNECTION_STRING = 'sqlite:///scrapy_site.db'