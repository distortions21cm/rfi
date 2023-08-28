# STARFIRE – Simulation of TerrestriAl Radio Frequency Interference in oRbits around Earth

STARFIRE provides a Python-based framework to evaluate radio frequency interference (RFI) levels in the FM band at different altitudes and locations around Earth for low frequency cosmological experiments at radio wavelength. Using a geographically distributed (limited as of now) database of FM transmitters, STARFIRE can generate a spectral cube containing RFI (FM) power with dimension N_altitude × N_pixel × N_frequency. The output spectral cube can be sliced along appropriate axes to provide useful metrics of RFI (FM) occupancy, including all-sky RFI heatmaps 

![RFI(heatmap)](https://github.com/distortions21cm/rfi/assets/86597094/b4570da3-997e-4871-86a8-bb623088a59f)

at specific frequencies and altitudes, variation in total RFI power with height over a specific pixel, or an RFI frequency-spectrum over a particular location at a specific altitude. 
![RFI_spectrum](https://github.com/distortions21cm/rfi/assets/86597094/503e3190-58f6-40c3-ae02-873bdc90bc30)

This algorithm can be also be used for any application that may require an understanding of the RFI environment in Earth-orbit, as desired by the end-user, and maybe readily be extended to other range of frequency based on the availability of datasets.

"Clean version.ipynb" - This notebook briefly introduces how STARFIRE can be used to generate RFI (FM) spectrum and RFI (FM) heatmap.

