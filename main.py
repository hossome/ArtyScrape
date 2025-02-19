from scrapers.aaartsalliance_scraper import Site1Scraper
# from scrapers.site2_scraper import Site2Scraper
import json


def run_scrapers():
    scrapers = [Site1Scraper()]
    all_data = []   # this is a list

    for scraper in scrapers:
        try:
            data = scraper.scrape()
            all_data.append(data)
        except Exception as e:
            print(f"Error scraping: {e}")
        finally:
            scraper.close()

    # Save scraped data
        with open("data/scraped_data.json", "w") as f:
            json.dump(all_data, f, indent=4)


if __name__ == "__main__":
    run_scrapers()
