## Universidad Del Norte
## Image Registration Software - Regim

Regim is a desktop app developed with python in order to 
ease medical image registration processes.

Our team was in charge of optimizing the image registration 
methods provided by [SimpleITK](http://www.simpleitk.org/), 
as well as validating and checking the correct result.
- [Documentation](#documentation)
- [Download](#download)
- [Setup](#setup)
- [Contributors](#contributors)
- [References](#references)

___

### Documentation
Project structure:
```
Regim
|
+--assets/
|
+--src
|   |
|   +--RegistrationMethods.py
|   |
|   +--Tools.py
|   |
|   +--Visualizer.py
|   |
|   +--ZoomAdvanced.py
|
+--App.py
|
+--requirements.txt
```
The module ``App.py`` contains all the user interface elements
and events. 


In the src folder, ``RegistrationMethods.py`` have a class that
implements 2 image registration methods from SimpleITK. 


``Tools.py`` have a list of methods that supports the program
such as image resizing and DICOM to PNG converter.


``Visualizer.py`` is the image visualization window, which allow you
to adjust the brightness, contrast and color of each image, also,
implements ``ZoomAdvanced.py``.    

___

### Download

You can download the software through the following options:

- Download the software in our [Regim web page](https://fabirt.github.io/Regim-project/Regim-Web/)
- Download it from our repository [releases](https://github.com/fabirt/Regim-project/releases)

___

### Setup
In order to run the source code, 
you need to have python and pip installed in your machine, 
after that, install the project dependencies using 
the following  command:

```
$ path/to/project/Regim> pip install -r requirements.txt
```

And then run the main module:

```
$ path/to/project/Regim> python App.py
```

___

### Contributors
- Fabián Diartt
- Ricardo Martín

___

### References
>1. Z. Yaniv, B. C. Lowekamp, H. J. Johnson, R. Beare, "SimpleITK Image-Analysis Notebooks: a Collaborative Environment for Education and Reproducible Research", J Digit Imaging., https://doi.org/10.1007/s10278-017-0037-8, 2017.
