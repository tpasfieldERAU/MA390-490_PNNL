MA390/490 PNNL Project Spring 2024
---
Repository containing code and Jupyter notebooks facilitating the data science work of our project. This repo will contain example files for working with the data and libraries in various ways.

**To install all packages needed for this project, please use:** 

`pip -r requirements.txt`!!

If you wish to manually manage packages, here is a condensed list.

Bare Minimum:
- `numpy`
- `scipy`
- `matplotlib`
- `jupyter`

Visualization:
- `seaborn`
- `itk-io`
- `itkwidgets`

Dimensioning:
- `opencv-python`

Segmentation:
- `scikit-learn`

Some work will already be using OpenCV, but isn't necessarily needed for opening or viewing the data. If needed, install it with `pip install opencv-python`.

Similarly, if you plan to work directly with the TIFF files instead of the `.npy` matrix files within the team drive, you will need the `pylibtiff` library. If you encounter problems installing this library, you may need to install Microsoft Visual C++ Build Tools through the Visual Studio Installer.