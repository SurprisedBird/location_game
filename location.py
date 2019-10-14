import requests

class Location():

    def get_coordinats(self, url, api_key):
        address = str(input("Print address "))

        full_url = f"{url}?address={address}&amp&key={api_key}"
        request = requests.get(full_url)
        response = request.json()

        lat = response["results"][0]["geometry"]["location"]["lat"]
        lng = response["results"][0]["geometry"]["location"]["lng"]
        print(lat, lng)
    
    def get_location(self, url, api_key):
        lat = float(input("Print latitude "))
        lng = float(input("Print longitude "))

        fool_url = f"{url}?latlng={lat},{lng}&amp&key={api_key}"
        request = requests.get(fool_url)
        response = request.json()
        address = response["results"][0]["formatted_address"]
        print(address)







