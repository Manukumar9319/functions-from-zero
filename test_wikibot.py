from wikibot import scrape

def test_wiki():
    assert "Microsoft" in scrape("Microsoft")