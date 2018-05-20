import requests
from bs4 import BeautifulSoup as bs
import sys
import urllib
import datetime
import os

now        = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
m_folder   = 'data_' + now
img_folder = m_folder + os.sep + 'images'
headers  = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 OPR/44.0.2510.857'}

images_list = []
url      = sys.argv[1]
res      = requests.get(url, headers=headers)
if res.status_code == 200:
	os.makedirs(m_folder)
	os.makedirs(img_folder)
	soup     = bs(res.content, "lxml")
	all_img  = soup.find_all('img')
	for img in all_img:
		try:
			image_url = img['src']
			if image_url.startswith('http') and not image_url.endswith('.svg'):
				if image_url.endswith('png') or image_url.endswith('jpg') or image_url.endswith('jpeg') or image_url.endswith('bmp') or image_url.endswith('gif')  :
					images_list.append(image_url)
		except:
			pass
	print(images_list)

else:
	print('Not able to open URL !')


text_file_name = m_folder + os.sep + 'data.txt'
with open(text_file_name, 'a') as ff:
	for i,img in enumerate(images_list):
		try:
			filename  = img_folder + os.sep + str(i+1) + '.jpg'
			urllib.urlretrieve(img, filename)
			ff.write(str(i+1) + '.jpg' + ','+ img + '\n' )
		except:
			pass

