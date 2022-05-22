import time
from urllib.request import urlretrieve
from PIL import Image
import pytesseract
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#셀레니움 드라이버
options = webdriver.ChromeOptions()
options.add_argument('headless') 
driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.amazon.com/Death-Ivan-Ilyich-Nikolayevich-Tolstoy/'
url += 'dp/1427027277'
driver.get(url)
time.sleep(3)

#미리보기 버튼을 클릭합니다.
driver.find_element_by_id('imgBlkFront').click()
imageList = []

#페이지 불러올 때
time.sleep(5)

while 'pointer' in driver.find_element_by_id('sitbReaderRightPageTurner').get_attribute('style'):
    #오른쪽 화살표를 누를 수 있다면 페이지를 계속 넘깁니다.
    driver.find_element_by_id('sitbReaderRightPageTurner').click()
    time.sleep(2)
    #새 페이지를 모두 가져옵니다. 동시에 여러 페이지를 가져올 수 있지만,
    #세트에는 중복이 저장되지 않습니다.
    pages = driver.find_elements_by_xpath('//div[@class=\'pageImage\']/div/img')
    if not len(pages):
        print('No pages found')
    for page in pages:
        image = page.get_attribute('src')
        print('found image: {}'.format(image))
        if image not in imageList:
            urlretrieve(image, 'page.jpg')
            imageList.append(image)
            print(pytesseract.image_to_string(Image.open('page.jpg')))

driver.quit()