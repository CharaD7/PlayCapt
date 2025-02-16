from playwright.sync_api import sync_playwright

pw = sync_playwright().start()
browser = pw.chromium.launch()
page = browser.new_page()

page.goto("https://www.arxiv.org/search")
page.get_by_placeholder("Search term...").fill("neural network")
page.get_by_role("button", name="Search").nth(1).click()

# Get all links that contain "arxiv.org/pdf" with xpath
links = page.locator("xpath=//a[contains(@href, 'arxiv.org/pdf')]").all()

print(f"Page title: { page.title() }")
print(f'PDF Links: { [ link.get_attribute("href") for link in links ] }')

# close browser
browser.close()
