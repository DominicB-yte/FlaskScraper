import scraper
from decimal import Decimal

def test_scraper1():
    trademe = "https://www.trademe.co.nz/gaming/playstation-4/consoles"
    trademe_listings = scraper.process(scraper.scrape(trademe))
    mini, maxi, avg, prices = scraper.priceProcess(trademe_listings)
    assert mini < avg
    assert maxi > mini
    assert avg == sum(prices) / len(prices)

def test_scraper2():
    result = scraper.scrape("nothing")
    assert result is None
