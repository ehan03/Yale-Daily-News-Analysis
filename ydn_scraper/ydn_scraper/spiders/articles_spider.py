# standard library imports

# third party imports
import pandas as pd
from scrapy.spiders import SitemapSpider
from unidecode import unidecode
from w3lib.html import remove_tags

# local imports
from ..items import Article


class ArticlesSpider(SitemapSpider):
    name = "ydn_articles"
    sitemap_urls = ["https://yaledailynews.com/sitemap_index.xml"]
    sitemap_follow = ["/post-sitemap"]
    sitemap_rules = [
        ("/blog/", "parse_article"),
    ]
    custom_settings = {
        "ROBOTSTXT_OBEY": False,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 1,
        "CONCURRENT_REQUESTS": 1,
        "COOKIES_ENABLED": True,
        "DOWNLOADER_MIDDLEWARES": {
            "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
            "scrapy_user_agents.middlewares.RandomUserAgentMiddleware": 400,
        },
        "REQUEST_FINGERPRINTER_IMPLEMENTATION": "2.7",
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "FEED_EXPORT_ENCODING": "utf-8",
        "DEPTH_PRIORITY": 1,
        "SCHEDULER_DISK_QUEUE": "scrapy.squeues.PickleFifoDiskQueue",
        "SCHEDULER_MEMORY_QUEUE": "scrapy.squeues.FifoMemoryQueue",
        "RETRY_TIMES": 1,
        "RETRY_HTTP_CODES": [500, 502, 503, 504, 400, 403, 404, 408, 429],
        "LOG_LEVEL": "INFO",
        "ITEM_PIPELINES": {},
        "CLOSESPIDER_ERRORCOUNT": 1,
        "DOWNLOAD_DELAY": 0.2,
        "DOWNLOAD_TIMEOUT": 600,
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_START_DELAY": 0.2,
        "AUTOTHROTTLE_TARGET_CONCURRENCY": 1,
        "AUTOTHROTTLE_MAX_DELAY": 5,
        "DEFAULT_REQUEST_HEADERS": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "max-age=0",
            "Priority": "u=0, i",
            "Sec-Ch-Ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        },
    }

    def parse_article(self, response):
        # TODO: fix this shit
        # plan: split into four cases
        # 1) typical articles
        # 2) ytv articles
        # 3) features
        # 4) all other cases just skip (should be very small percentage)

        pass

        # title = response.css("div.article-header > h1::text").get()
        # if "/ytv" not in response.url and title:
        #     article_item = Article()

        #     article_item["url"] = response.url

        #     date = response.css("date::text").get()
        #     article_item["date"] = (
        #         pd.to_datetime(date.replace("|", "").strip()).strftime(
        #             "%Y-%m-%d %H:%M:%S"
        #         )
        #         if date
        #         else None
        #     )

        #     article_item["title"] = unidecode(title.strip()) if title else None

        #     subtitle = response.css("div.article-header > p.subtitle::text").get()
        #     article_item["subtitle"] = unidecode(subtitle.strip()) if subtitle else None

        #     metadata = response.css(
        #         "meta[name^='twitter:data']::attr(content)"
        #     ).getall()
        #     article_item["estimated_reading_time_minutes"] = None
        #     for data in metadata:
        #         if "minute" in data:
        #             article_item["estimated_reading_time_minutes"] = int(
        #                 data.split(" ")[0].strip()
        #             )
        #             break

        #     content = [
        #         remove_tags(p).strip()
        #         for p in response.css("section.article-text > p").getall()
        #     ]
        #     article_item["content"] = (
        #         "\n".join([unidecode(p) for p in content if p]) if content else None
        #     )

        #     yield article_item
        # else:
        #     self.logger.info(f"Skipping {response.url}")