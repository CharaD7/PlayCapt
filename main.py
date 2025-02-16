from playwright.sync_api import sync_playwright

pw = sync_playwright().start()
browser = pw.chromium.launch()
page = browser.new_page()

page.goto("https://www.google.com/")
print(page.title())
