import json
import requests 
import sys 

#Chicago Art API
def main():
    response = requests.get("https://api.artic.edu/api/v1/artworks/search")
    content = response.json()
    for result in content["data"]:
        print(result["title"])
main()


#itunes API
if len(sys.argv) != 2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent = 2))
o = response.json()
for result in o["results"]:
    print(result["trackName"])