import sys
import wget
from urllib.error import HTTPError

# All images are served from this base CDN url
BASE_URL = 'https://cdn.pics-x.com/gallery-images/galleries/'

# Grab the listing/index URL argument
url = sys.argv[1]

# split the url so we can find the magic ID
split_url = url.split('/')
gallery_id = split_url[4]


i = 1;
while i < 200:
    try:

        # this cdn uses a funky structure. basically, it uses the first 3 characters of the 
        # gallery id and also the full gallery id as parameters. it then has sequentially ordered
        # .jpg images that are padded with 0s until reaching 4 characters.
        #
        # example:
        # [BASE_URL]/[first 3 chars of id]/[full id]/[img name.jpg]
        # https://cdn.pics-x.com/gallery-images/149/1497/0001.jpg
        # 
        # build up the url using the 2 IDs and then increment the counter with padded 0s
        # and keep scraping until we hit a 404 meaning there are no more images left.

        first_3 = gallery_id[0 : 3]
        img_url = BASE_URL + str(first_3) + '/' + str(gallery_id) + '/' + str(i).zfill(4) + '.jpg'
        
        print('...retieving: ' + img_url)
        filename = wget.download(img_url)

        i = i + 1
    except HTTPError:
        # todo remove this
        print('404')
        break

print("################################")
print('Finished scraping: ' + str(i - 1) + ' images')
