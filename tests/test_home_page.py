from pages.home_page import HomePage
import allure


@allure.feature('Homepage')
@allure.story('Homepage url')
@allure.title('Homepage url test')
def test_home_page_url(driver):
    home_page = HomePage(driver)
    home_page.navigate()
    expected_url = "https://www.twitch.tv/"
    assert driver.current_url == expected_url


@allure.feature('Homepage')
@allure.story('Homepage title')
@allure.title('Homepage title test')
def test_home_page_title(driver):
    driver.get("https://www.twitch.tv/")
    home_page = HomePage(driver)
    assert home_page.get_title() == "Twitch"


@allure.feature('Homepage')
@allure.story('Homepage load time')
@allure.title('Homepage load time test')
def test_home_page_load_time(driver):
    import time
    start_time = time.time()
    driver.get("https://www.twitch.tv/")
    end_time = time.time()
    load_time = end_time - start_time
    assert load_time < 10.0, f"Home page load time was too long: {load_time}"
