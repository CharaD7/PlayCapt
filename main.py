from playwright.sync_api import sync_playwright
from urllib.request import urlretrieve

pw = sync_playwright().start()
browser = pw.chromium.launch()
page = browser.new_page()

page.goto("https://www.arxiv.org/search")
page.get_by_placeholder("Search term...").fill("neural network")
page.get_by_role("button", name="Search").nth(1).click()

# Get all links that contain "arxiv.org/pdf" with xpath
links = page.locator("xpath=//a[contains(@href, 'arxiv.org/pdf')]").all()

# for link in links:
#   urls = link.get_attribute("href")
#   urlretrieve(urls, "data/" + urls[-5:] + ".pdf")

urls = [ link.get_attribute("href") for link in links ]
[ urlretrieve(url, "data/" + url[-5:] + ".pdf") for url in urls ]

print(f"Page title: { page.title() }")

# close browser
browser.close()
