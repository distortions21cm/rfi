import numpy as np
import healpy as hp
import requests
from src.power_3D_cube_param import altitude_index, get_lat_lon, freq_index

def get_PS(power_output, altitudes, nside):
     """Returns the two-dimensional data cube along the altitude - pixel number plane

    Args:
         power_output (array): A three dimensional array of values of RFI (FM) power
         altitudes (array): user-defined altitudes of the satellite
         nside (int): NSIDE of the healpy map

    Returns:
         array: A two dimensional array of values of RFI (FM) power along the altitude - pixel number plane
    """
     ind_alt = altitude_index(altitudes)
     ind_loc = get_lat_lon(nside)
     return power_output[ind_alt, ind_loc, :]
    
def get_heatmap(power_output, altitudes, freq_range):
     """Returns the two-dimensional data cube of the total beam averaged RFI (FM) power per-pixel

    Args:
         power_output (array): A three dimensional array of values of RFI (FM) power
         altitudes (array): user-defined altitudes of the satellite
         freq_range (array): User-defined frequency range

    Returns:
         array: A two dimensional array of values of the total beam averaged RFI (FM) power per-pixel
    """
     ind_alt = altitude_index(altitudes)
     ind_freq = freq_index(freq_range)
     return freq_range[ind_freq], power_output[ind_alt, :, ind_freq]

