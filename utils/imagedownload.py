import os
import requests
from bs4 import BeautifulSoup

Google_Image = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

u_agnt = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

Image_Folder = 'Images'
Parent_dir = "D:\pythons\discord_bot\data"
path = os.path.join(Parent_dir, Image_Folder)


def main(name, number):
    if not os.path.exists(Image_Folder):
        os.mkdir(Image_Folder)
    download_images(name, number)


def download_images(name, number):
    data = name
    num_images = number

    search_url = Google_Image + 'q=' + data  # 'q=' because its a query

    # request url, without u_agnt the permission gets denied
    response = requests.get(search_url, headers=u_agnt)
    html = response.text  # To get actual result i.e. to read the html data in text mode

    # find all img where class='rg_i Q4LuWd'
    # html.parser is used to parse/extract features from HTML files
    b_soup = BeautifulSoup(html, 'html.parser')
    results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})

    # extract the links of requested number of images with 'data-src' attribute and appended those links to a list 'imagelinks'
    # allow to continue the loop in case query fails for non-data-src attributes
    count = 0
    imagelinks = []
    for res in results:
        try:
            link = res['data-src']
            imagelinks.append(link)
            count = count + 1
            if (count >= num_images):
                break

        except KeyError:
            continue

    for i, imagelink in enumerate(imagelinks):
        response = requests.get(imagelink)

        imagename = Image_Folder + '/' + data + str(i+1) + '.jpg'
        with open(imagename, 'wb') as file:
            file.write(response.content)
