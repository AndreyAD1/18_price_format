# Price Formatter

This program gets a string containing a number and returns this
number in the comfortable to read format.

# How to Install

The program requires Python v3.5.

# Quick Start

You can use this program as either console script or 
Python module.

A price is the positional argument of the script.
To run script in Linux terminal:
```bash
$ python format_price.py 1234567.98701
1 234 567.99
```
Windows usage is the same.

The input parameter of **`format_price`** function
should be a number or a string with a number. In case input 
parameter has other type, the function will return **`None`**.

Using program as Python module:
```python
>>> from format_price import format_price
>>> format_price('12345.7634')
'12 345.76'
```

# How to Test

Put the file **`tests.py`** in the directory containing 
**`format_price.py`** and launch **`tests.py`** from console.
To run tests on Linux:
```bash
$ python3 tests.py
..............
----------------------------------------------------------------------
Ran 14 tests in 0.005s

OK
```
Windows usage is the same.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
