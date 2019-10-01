import requests

dst_folder = "OGS_SRC_IMGS"

if __name__ == '__main__':
    src = open('img_urls.txt', 'r')
    urls = src.read().split(', ')
    src.close()
    i = 0
    for url in urls:
        try:
            i += 1
            with open(dst_folder+"\\src_{}.jpg".format(i), "wb") as f:
                f.write(requests.get(url).content)
                f.close()
        except:
            print("Something went wrong, skipping url: {}".format(url))
