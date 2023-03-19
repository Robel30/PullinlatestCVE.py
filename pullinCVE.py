import requests
import json

def main():

    content = requests.get("https://cve.circl.lu/api/last")
    json = content.json()

    for item in json:
        print("{} {}".format("Vuln Number:", item['id']))
        print("{} {} \n".format("Description:", item['summary']))

main()
