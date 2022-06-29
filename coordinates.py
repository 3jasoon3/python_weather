from typing import NamedTuple
from geopy.geocoders import Nominatim
import config
from exceptions import IncorrectCityName
class Coordinates(NamedTuple):
    longitude: float
    latitude: float


def get_coordinates(city_name: str) -> Coordinates:
    geolocator = Nominatim(user_agent="coordinates.py")
    try:
        location = geolocator.geocode(f"{city_name}")
        long = location.longitude
        lat =location.latitude
        if config.USE_ROUNDED_COORDINATES: 
            lat, long = map(lambda c: round(c, 1), [lat,long])
        return Coordinates(longitude=long, latitude=lat)
    except:
        raise IncorrectCityName
    