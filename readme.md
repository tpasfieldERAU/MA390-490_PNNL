MA390/490 PNNL Project Spring 2024
---
Repository containing code and Jupyter notebooks facilitating the data science work of our project. This repo will contain example files for working with the data and libraries in various ways.

A `requirements.txt` file will be added in the future in order to aid in setting up the Python environment needed to execute the code. It is suggested that you have the following packages installed *at the bare minimum*:
- Numpy
- Scipy
- `itk-io`
- `itkwidgets`
- `jupyter`

Some work will already be using OpenCV, but isn't necessarily needed for opening or viewing the data. If needed, install it with `pip install opencv-python`.

Similarly, if you plan to work directly with the TIFF files instead of the `.npy` matrix files within the team drive, you will need the `pylibtiff` library. If you encounter problems installing this library, you may need to install Microsoft Visual C++ Build Tools through the Visual Studio Installer.