from selenium import webdriver
import sys

n = len(sys.argv)
data = f"{sys.argv[1]}"
for i in range(2,n):
	data = f"{data}+{sys.argv[i]}"

	
url = f"https://www.youtube.com/results?search_query={data}"
browser = webdriver.Firefox()
browser.get(url)

browser.find_element_by_xpath('//*[@id="video-title"]').click()
