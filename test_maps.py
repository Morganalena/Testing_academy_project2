import pytest
from playwright.sync_api import sync_playwright
import time

@pytest.fixture(scope="module")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)  
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture(scope="module")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()

def reject_cookies(page):
    cookies_button = page.locator("//*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div/div/button")
    if cookies_button.is_visible():
        cookies_button.click()

def reviews_section(page, search):
    reviews_button_locator = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[2]'
    page.locator(reviews_button_locator).click()
    time.sleep(5)  

    reviews_section_locator = "//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div[2]/div[3]"
    reviews_section = page.locator(reviews_section_locator)
    assert reviews_section.is_visible(), "Reviews section is not visible"
    
    review_count_element = reviews_section.locator('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div[2]/div[3]') 
    if review_count_element.is_visible():
        review_count = review_count_element.text_content()
        print(f"Number of reviews for '{search}': {review_count}")

def map_type_change(page):
    minimap_button_locator = '//*[@id="minimap"]/div/div[2]/button'
    page.locator(minimap_button_locator).click()
    time.sleep(5)  

    map_info_locator = '//*[@id="LFaNsb"]'
    map_info = page.locator(map_info_locator)
    text_content = map_info.text_content()
    
    text_words = text_content.replace(',',' ').split()
    specific_words = ["Maxar", "Technologies"]
    
    found_words = []
    for word in specific_words:
        if word in text_words:
            found_words.append(word)
    
    assert found_words == specific_words, f"Expected words 'Maxar Technologies' not found in '{text_content}'"

def directions(page):
    back_tab_locator = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div/div/button[1]'
    page.locator(back_tab_locator).click()
    time.sleep(2)

    directions_button_locator = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button'
    page.locator(directions_button_locator).click()
    time.sleep(2)

    start_point_locator = '//*[@id="sb_ifc50"]/input'
    start_point = page.locator(start_point_locator)
    start_point.fill("Prague")
    page.keyboard.press("Enter")
    time.sleep(7)

    directions_panel_locator = '//*[@id="section-directions-trip-0"]/div[1]'
    directions_panel = page.locator(directions_panel_locator)
    assert directions_panel.is_visible(), "Directions panel is not visible"

@pytest.mark.parametrize("search", [
    "Snowdon, Wales",
    "Arthur's Seat"
])
def test_google_maps_search(page, search):
    page.goto("https://www.google.com/maps", timeout=50000)
    reject_cookies(page)

    search_box = page.locator('//input[@id="searchboxinput"]')
    search_box.fill(search)
    page.keyboard.press("Enter")

    reviews_section(page, search)
    map_type_change(page)
    directions(page)


if __name__ == "__main__":
    pytest.main()
