import numpy as np
import healpy as hp
import requests

def get_lat_lon(nside):
    """Returns the pixel index of the user specified location w.r.t. the NSIDE of the healpy map

    Args:
         nside (int): NSIDE of the healpy map

    Returns:
         int: Pixel index of the user specified location
    """
    user_place = input("Enter a place name: ")

    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": user_place,
        "format": "json",
        "limit": 1
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data:
        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])
        print(f"Latitude: {lat}, Longitude: {lon}")
        pixNo = hp.ang2pix(nside, lon, lat ,lonlat=True)
        return pixNo
    else:
        print("Place not found or error occurred.")
        return None
        
def altitude_index(altitudes):
    """Returns the pixel index of the user specified altitude of the satellite

    Args:
         altitudes (array): user-defined altitudes of the satellite

    Returns:
         int: Pixel index of the user specified altitude
    """
    user_input = float(input("Enter an altitude in km: "))
    if user_input in altitudes:
        return np.where(altitudes==user_input)[0][0]
    else:
        print("Altitude not found")

def freq_index(freq_range):
    """Returns the pixel index of the user specified frequency 

    Args:
         freq_range (array): User-defined frequency range

    Returns:
         int: Pixel index of the user specified frequency
    """
    f0 = float(input("Enter the frequency: "))
    if f0 < freq_range[0] or f0 > freq_range[-1]:
        return "Frequency not found"
    else:
        f_idx = np.abs(freq_range-f0).argmin()
        if not f0 in freq_range:
            print(f"The nearest frequency is {freq_range[f_idx]} MHz.")
        return f_idx

