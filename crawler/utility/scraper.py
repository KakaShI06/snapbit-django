from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from crawler.utility.clean_price import clean_and_convert

def getProductDetails(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'productTitle')))

    product_title = driver.find_element(By.ID, 'productTitle')
    product_price = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')
    original_price = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[2]/span/span[1]/span/span/span[2]')
    productImgWrapper = driver.find_element(By.ID, 'imgTagWrapperId')

    imgtag = productImgWrapper.find_element(By.TAG_NAME, 'img')
    imgUrl = imgtag.get_attribute('src')

    payload = {
        "img_url": imgUrl,
        "original_price": original_price.text,
        "current_price": product_price.text,
        "title": product_title.text
    }

    driver.quit()

    return payload