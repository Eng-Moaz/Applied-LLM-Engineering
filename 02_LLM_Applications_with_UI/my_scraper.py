from scrapling import Fetcher, StealthyFetcher

def fetch_website_contents(url):
    """
    Return the title and contents of the website at the given url;
    truncate to 2,000 characters as a sensible limit
    """
    page = Fetcher.get(url)
    title = page.css('title::text').get() or ""
    text = page.get_all_text(separator="\n", ignore_tags=('script', 'style', 'img', 'input')) or ""

    return (title + "\n\n" + text)[:2_000]

def fetch_website_links(url):
    """
    Return the links on the website at the given url
    """
    page = Fetcher.get(url)
    links = page.css("a::attr(href)").getall()

    return list(links)

if __name__ == "__main__":
    print(fetch_website_contents_mine("https://edwarddonner.com/"))
    print("-"*40 + "Mine" + "-"*40)
    print(fetch_website_links_mine("https://edwarddonner.com/"))