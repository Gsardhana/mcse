import requests
import webbrowser
from selenium import webdriver

def googleim(img):
	filePath = img
	searchUrl = 'http://www.google.hr/searchbyimage/upload'
	multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
	response = requests.post(searchUrl, files=multipart, allow_redirects=False)
	fetchUrl = response.headers['Location']
	#webbrowser.open(fetchUrl, new=0, autoraise=False)
	#print(fetchUrl)
	chrome_path = 'chromedriver.exe'
	chrome_options = webdriver.ChromeOptions()
	#chrome_options.add_argument("--start-maximized")
	#agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
	#chrome_options.add_argument("user-agent="+agent)
	chrome_options.add_argument("--headless")
	driver = webdriver.Chrome(chrome_path,options = chrome_options)
	driver.get(fetchUrl)
	b1  = driver.find_elements_by_class_name('st') 
	b2  = driver.find_elements_by_class_name('r')
	googleim.dekh = ''
	googleim.dek = ''
	for i in b2:
		googleim.dekh = googleim.dekh + i.find_element_by_tag_name('h3').text

	for i in b1:
		googleim.dek = googleim.dek + i.text
	yehai = (googleim.dekh + ' ' + googleim.dek).lower()


	# To find the infection 
	inf =['sporotrichosis','aspergillosis','blastomycosis','blastomyces','coccidioidomycosis','histoplasmosis','malassezia pachydermatis','pneumocystosis','rhinosporidiosis']

	#print(yehai)
	infcount=[]
	for i in inf:
		#print(i,yehai.count(i))
		infcount.append(yehai.count(i))

	maxinf = max(infcount)
	if maxinf>0:
		googleim.infection  = inf[infcount.index(maxinf)]
	else:
		googleim.infection = 'unknown'

	#print(googleim.infection)            

	return 0

#googleim('a6.jpg')


