import urllib2

def download_image(url):
    request = urllib2.Request(url)
    img = urllib2.urlopen(request).read()
    with open (file_name + '.jpg', 'w') as f: f.write(img)

url = input('Please enter image URL (string):')
file_name = input('Please enter file name (string):')

download_image(url)