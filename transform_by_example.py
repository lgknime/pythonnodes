
import math
import pandas as pd
import numpy as np
import random
import requests as re
from bs4 import BeautifulSoup
import os



knime_data = pd.read_csv("data/missingdata.csv")
obj = knime_data.loc[0, "Company"].lower().replace(" ", "_")




x = re.get(f'https://wikipedia.org/wiki/KNIME').content

soup = BeautifulSoup(x, 'html.parser')


print(soup.find("table").find_all("td"))