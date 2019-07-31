from selenium import webdriver





driver = webdriver.Firefox()
url = 'https://www.autoscout24.de/lst/land-rover/range-rover-evoque?sort=standard&desc=0&eq=140%2C155%2C23&gear=A&fuel=B&doorfrom=4&doorto=5&ustate=N%2CU&page=1&powerfrom=147&powertype=hp&cy=D&kmto=10000&ptype=M&atype=C'
driver.get(url) #open web browser with specific url

filter_result = driver.find_elements_by_xpath('//span[@class="sc-tag__label"]')
#filter_result = driver.find_elements_by_xpath('/<span class=" cl-filters-summary-counter"')
# <div class="sc-tag" data-test="tag-make-model-0"><span class="sc-tag__label">Land Rover Range Rover Evoque</span><div class="sc-tag__close"><as24-icon type="close"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><path d="M.031 14.142L14.173 0l1.414 1.414L1.445 15.556z"></path><path d="M1.415.031l14.142 14.142-1.415 1.414L0 1.445z"></path></svg></as24-icon></div></div>

print(filter_result[0].text)

filter_result
for i in filter_result:
    text = i.text
    print(text)
driver.close() #close web browser
