# GUI-phase-tracking

## What is it? 
GUI-phase-tracking is a software useful for plotting mathematical functions and other stuffs.

## Getting Started



### Prerequisites

* Python (>=3)
* Tkinter (tested on 8.6)
	To install tkinter you should use your package manager:
    * Debian:
    
    ```
    apt-get install python3-tk
    ```
    
    * openSUSE
    
    ```
    zypper in python3-tk
    ```
    * To install on other OS (E.G. mac, Windows) refers to:
    
    	[tkdocs.com/tutorial/install.html](https://tkdocs.com/tutorial/install.html)

* NumPy & SciPy python modules

```
pip install numpy scipy
```

* NumExpr python module (tested on version 2.6.8)

```
pip install numexpr 
```

## Running 

Open a terminal and go to the GUI-phase-tracking directory.

Next launch `GUI-phase.py`

```
python GUI-phase.py
```
**ACHTUNG!** Make sure  your `python` command is a symbolic link to `Python3` (not to `python2`).

You can easily check running:

```
ls -l $(which python)
```
if it isn't you HAVE to run this software with:

```
python3 GUI-phase.py
```

## Built With

* [PAGE](http://page.sourceforge.net/) - Python Automatic GUI Generator
* [NUMPY](http://www.numpy.org/) - Package for scientific computing with Python
* [NUMEXPR](https://github.com/pydata/numexpr) - Fast numerical expression evaluator for NumPy

## Authors

* [**Stefano PARAcchino**](https://github.com/spara7C5) - *Initial work* and main developer


