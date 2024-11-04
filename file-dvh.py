import googlemaps
from geopy.geocoders import Nominatim

def geolocate(address):
    """
    Geolocate an address using Google Maps API.
    """
    gmaps = googlemaps.Client(key='YOUR_API_KEY')
    geolocator = Nominatim(user_agent="geolocate")

    geocode_result = gmaps.geocode(address)
    if geocode_result:
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        return lat, lng
    else:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None

# Example usage
address = '1600 Amphitheatre Parkway, Mountain View, CA'
lat, lng = geolocate(address)
if lat and lng:
    print(f'Latitude: {lat}, Longitude: {lng}')
else:
    print('Address not found')