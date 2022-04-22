# Web-Form-Filler
Filling web form and dealing with exceptions

This script automates the manual job of filling forms in a web browser taking its data from any data source 

## Dependencies
Install **chocolatey** following the installation instructions from [here](https://chocolatey.org/install#individual/)

Use **choco** to install any browser package e.g [Chocolatey Firefox](https://community.chocolatey.org/packages/Firefox/) or [Chocolatey Google Chrome](https://community.chocolatey.org/packages/GoogleChrome) 

```sh
choco install Firefox
```
or
```sh
choco install googlechrome
```


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install selenium and pandas. 

```bash
pip install selenium
pip install pandas
```

## Usage

```python
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import math
import time

# Adjust the rest of the script to suit your data source and web form
```
Check my target form [here](https://itcentre.iita.org/add-new-extension/?ign_skip=itoms) and check out selenium webdriver docs from [here](https://selenium-python.readthedocs.io/getting-started.html) 
